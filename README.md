# Z-Profile

Build your own research profile using Zola and Zotero.

Example site: <https://wragge.github.io>

## Features

* Automatically generates a personal home page with biographical note, photo, social media accounts, and selected publications.
* Individual page for each publication, with embedded PDF viewer for attached green open access versions.
* Embedded metadata in publication pages for easy capture by Zotero.
* Atom feed with new or updated publication pages.
* Generates a static site that can be published using GitHub Pages or any web host.

## What is Z-Profile?

Z-Profile helps non-technical researchers create their own simple, online research profile that shares biographical details and a list of publications. It's deliberately minimalist in design and function. Z-Profile is intended for people who want to share their research, but don't have the time, energy, or knowledge to build or maintain a website.

Z-Profile is really just some templates and a bit of data plumbing. It gets data from Zotero, does of bit of processing, then generates a static website using Zola. All you do is set up a collection in Zotero and configure a few things in GitHub.

## Why did I create Z-Profile?

One of the main reasons I created Z-Profile was to make it easier for researchers who want to share green open access versions of their publications. Publishers will often allow authors to make the author accepted manuscript (AAM) version of a publication available through a 'personal website' without any embargo. Using Z-Profile, you just attach a PDF of the AAM version to an item record in Zotero, and it will make your publication available for reading and download. It's a great way of getting your research out to the public as soon as possible.

I also think it's important for researchers to have online profiles that are not wholly dependent on their employer or a company that wants to exploit their data – to have 'a domain of your own' (in the words of the excellent folks at Reclaim Hosting). Of course, there are some other great options for building a research profile. In particular, I'd strongly suggest you set yourself up on the Knowledge Commons. But having your own site, under your own domain, gives you extra control and flexibility.

## Requirements

To use Z-Profile you need:

* Zotero installed and synced to a free Zotero online account
* a free GitHub account

## Building your site

### 1. Create a Zotero collection

Z-Profile pulls data from a Zotero collection. To set it up you need to:

* Create a new collection in your Zotero library to contain the items needed for your site. Click on 'My Library' in the sidebar and then select **'File > New Collection'** from the Zotero menu. Name the new collection `z-profile` (use this exact name or the processing script won't be able to find it).
* Add a new item to the collection to contain your biographical details. Click on the `z-profile` collection in the sidebar and then select **'File > Add Item > Book'** (the item type doesn't actually matter).
* Add the tag `bio` to the new item (again this is necessary for the script to find your data). Just scroll down the item metadata until you get to the 'Tag' section and click on the '+' icon.
* In the title field of your 'bio' tagged item add **your name as you want it to appear** in the heading of the site.

That's the bare minimum and will produce a site that just has your name and nothing else! To fill out the content see the sections below.

### 2. Add biographical information

Once you have an item tagged `bio` you can add additional information and attachments to it.

#### Tag line

Add a one line introduction to yourself in Zotero's 'Short Title' field. For example: `Historian and hacker`, or `Associate Professor at the University of Tasmania`.

#### Email address

Add an email address in Zotero's 'Extra' field, using the format `email: tim@timsherratt.au`.

The email address will be linked from a mail icon on the home page.

#### Biography

Add a short biography by attaching a note to the 'bio' item. 

Just right click on the `bio` tagged item in Zotero and select **'Add Note'** from the menu. You can use Zotero's built-in editing tools to add links, lists, paragraphs, and bold and italic formatting to your biography. This will appear on the home page of your site.

#### CV

Add a CV to your profile by attaching a PDF of your CV to the `bio` item. 

Just right click on the `bio` tagged item in Zotero and select **'Add Attachment' > 'File'** from the menu. The processing script assumes that the first PDF attached to the `bio` item will be a CV, and it will create a download button on the home page.

#### Photo

Add a photo to your profile by attaching a jpeg image to the `bio` item.

Just right click on the `bio` tagged item in Zotero and select **'Add Attachment' > 'File'** from the menu. The image will be cropped square and displayed in a circle at the top of the home page.

#### Accounts and links

You can add links to social media services and other platforms. these are displayed as a row of icons on the home page.

Just right click on the `bio` tagged item in Zotero and select **'Add Attachment' > 'Web Link'** from the menu. Enter the name of the service in the 'Title' field. If the name matches any of the following (case insensitive) it will be displayed using a custom icon:

* ORCID
* Mastodon
* Knowledge Commons
* Bluesky
* GitHub
* Linkedin

Otherwise it will use a generic 'link' icon.

### 3. Add publications

You might already have your publications in your Zotero library. If so, just drag them to the `z-profile` collection. If not, either capture them from the publisher's site using Zotero, or enter them manually. You can add as many publications to the collection as you want.

If the final, published version of a publication is open access (both free to read and download *and* openly licensed), add the tag `open access` to the Zotero item. This will add an open access badge when the item's details are displayed on the site.

You can choose to display a list of selected publications on the home page. Just add the tag `selected` to any item you want to be included.

### 4. Add green open access versions

> [!TIP] Understanding versions
> **Version of record**: The final published version of your work, as it appears in the book or journal. Unless the publication is open access, you're probably not allowed to share this.
>
> **Author Accepted Manuscript**: The version of your work after you have made any changes required by peer review, but before it is copy edited and formatted by the publisher. Under publishers' green open access or 'self archiving' policies, you can probably share this, though there may be restrictions.
>
> **Preprint**: The version of your work that you originally submitted for publication, before any peer review or editorial comments. You can share this.

### 5. Get your Zotero credentials

### 6. Generate your GitHub repository

### 7. Add your Zotero credentials to GitHub

### 8. Run the GitHub action

## Publishing your site

### Option 1: GitHub Pages

### Option 2: A web host with CPanel

## Updating your site