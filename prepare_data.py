#!/usr/bin/env python
# coding: utf-8

# In[19]:


from pyzotero import zotero
from dotenv import load_dotenv
import os
from pathlib import Path
import nh3
from slugify import slugify
import json
import re
import tomli_w

load_dotenv()

ZOTERO_KEY = os.getenv("ZOTERO_KEY")
ZOTERO_ID = os.getenv("ZOTERO_ID")

zot = zotero.Zotero(ZOTERO_ID, "user", ZOTERO_KEY)


# In[20]:


colls = zot.everything(zot.collections_top())
ZOTERO_COLLECTION = [c for c in colls if c["data"]["name"] == "z-profile"][0]["key"]


# In[21]:


items = zot.everything(zot.collection_items_top(ZOTERO_COLLECTION, include="data,bib", linkwrap=1))


# In[22]:


OA_VERSIONS = {
    "vor": {"name": "version of record", "position": 1},
    "aam": {"name": "author accepted manuscript", "position": 2},
    "preprint": {"name": "preprint", "position": 3}
}

def check_label(item, label):
    if item["data"]["title"].lower() == label or label in [t["tag"] for t in item["data"]["tags"]]:
        return True
    return False

def dump_attachment(attachment):
    parts = attachment["data"]["filename"].split(".")
    filename = f"{slugify(parts[0])}.{parts[1]}"
    zot.dump(attachment["key"], filename, "static")
    return filename

def get_version(attachments, version):
    versions = []
    version_label = OA_VERSIONS[version]["name"]
    version_position = OA_VERSIONS[version]["position"]
    for attachment in attachments:
        att_tags = [t["tag"].lower() for t in attachment["data"]["tags"]]
        if version in att_tags:
            if attachment["data"].get("contentType") ==  "application/pdf":
                att_filename = dump_attachment(attachment)
                versions.append({"title": attachment["data"].get("title", ""), "version": version_label, "type": "pdf", "url": att_filename, "version_position": version_position, "type_position": 1})
            elif attachment["data"].get("linkMode") == "linked_url":
                versions.append({"title": attachment["data"].get("title", ""), "version": version_label, "type": "link", "url": attachment["data"]["url"], "version_position": version_position, "type_position": 2})
    return versions

def get_extra(item):
    extra_data = {}
    fields = item["data"].get("extra", "").split("\n")
    for field in [f for f in fields if f]:
        try:
            key, value = field.split(":")
        except ValueError:
            pass
        else:
            extra_data[key.strip()] = value.strip()
    return extra_data

bio_fm = {"extra":{}}
zola_config = {
    "base_url": "/",
    "generate_feeds": True
}
articles = []
accounts = []

Path("content", "publications").mkdir(exist_ok=True, parents=True)

for item in items:
    # Get the bio item
    if check_label(item, "bio"):
        # Get name from creators
        author = item["data"]["creators"][0]
        bio_fm["title"] = author["name"]
        zola_config["author"] = author["name"]
        zola_config["title"] = f"{author["name"]}: research profile"
        # Get tagline from shortTitle
        if tagline := item["data"]["shortTitle"]:
            bio_fm["extra"]["tagline"] = tagline
        # Looping through all attachments to the bio
        for attachment in zot.children(item["key"], itemType="attachment"):
            print(attachment["data"].get("contentType"))
            # If it's a PDF use as CV
            if attachment["data"].get("contentType") ==  "application/pdf":
                filename = dump_attachment(attachment)
                bio_fm["extra"]["cv"] = filename
            # If it's an image use as avatar
            elif attachment["data"].get("contentType") ==  "image/jpeg":
                filename = dump_attachment(attachment)
                bio_fm["extra"]["portrait"] = filename
            # Handle accounts
            elif attachment["data"].get("linkMode") == "linked_url":
                accounts.append({"account": attachment["data"]["title"], "url": attachment["data"]["url"]})
        bio_fm["extra"]["links"] = accounts
        # Add fields from Zotero's extra field
        extra_data = get_extra(item)
        bio_fm["extra"].update(extra_data)
        # Add the first attached note as the text of the home page
        bio_note = zot.children(item["key"], itemType="note")[0]
        cleaned_note = nh3.clean(bio_note["data"]["note"], tags={"b", "i", "p", "a", "ul", "li", "quote"})
        # Write the content of the home page
        Path("content").mkdir(exist_ok=True)
        Path("content", "_index.md").write_text("+++\n" + tomli_w.dumps(bio_fm) + "+++\n\n" + cleaned_note)
        # Write the config file
        Path("zola.toml").write_text(tomli_w.dumps(zola_config))
    else:
        # Default page front matter
        pub_fm = {"extra":{}, "template": "article.html"}
        # Create slugified version of title for page name
        fileslug = f"{slugify(item["data"]["title"])}-{item["key"]}"
        filename = f"{fileslug}.md"
        # Clean unwanted tags from citation
        citation = nh3.clean(item["bib"], tags={"i", "a"}).strip()
        # Remove urls from citation
        citation_no_link = nh3.clean(item["bib"], tags={"i"})
        citation_no_link = re.sub(r"http[^\s]+", "", citation_no_link).strip()
        # List all tags
        tags = [t["tag"].lower() for t in item["data"]["tags"]]
        # Set page title
        pub_fm["title"] = item["data"]["title"]
        # This date will be used in the RSS feed
        pub_fm["date"] = item["data"]["dateModified"]
        # Publication date
        pub_fm["extra"]["date"] = item["meta"]["parsedDate"]
         # Publication year for grouping
        pub_fm["extra"]["year"] = int(item["meta"]["parsedDate"][:4])
        # Add other values to front matter
        pub_fm["extra"]["citation"] = citation
        pub_fm["extra"]["citation_no_link"] = citation_no_link
        pub_fm["extra"]["metadata"] = item["data"]
        # Set default OA status
        oa_status = ""
        if "open access" in tags:
            oa_status = "open access"
        # Get attachments to look for OA versions
        versions = []
        attachments = zot.children(item["key"], itemType="attachment")
        for version_type in ["vor", "aam", "preprint"]:
            version = get_version(attachments, version_type)
            if version:
                versions.extend(version)
                if not oa_status:
                    oa_status = f"open access: {OA_VERSIONS[version_type]["name"]}"
        pub_fm["extra"]["oa_status"] = oa_status
        pub_fm["extra"]["versions"] = versions
        Path("content", "publications", filename).write_text("+++\n" + tomli_w.dumps(pub_fm) + "+++\n")
        if "selected" in tags:
            articles.append({"filename": filename, "citation": citation_no_link, "oa_status": oa_status, "year": int(item["meta"]["parsedDate"][:4])})

Path("content", "articles.json").write_text(json.dumps(articles))


# In[ ]:




