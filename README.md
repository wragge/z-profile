# Z-Profile

Build your own research profile using [Zola](https://www.getzola.org) and [Zotero](https://www.zotero.org/).

Example site: <https://wragge.github.io>

## Features

* Automatically generates a personal home page with biographical note, photo, social media accounts, and selected publications.
* Individual page for each publication, with embedded PDF viewer for attached green open access versions.
* Embedded metadata in publication pages for easy capture by Zotero.
* Generates a static site that can be published using GitHub Pages or any web host.

## What is Z-Profile?

Z-Profile helps non-technical researchers create their own simple, online research profile that shares biographical details and a list of publications. It's deliberately minimalist in design and function. Z-Profile is intended for people who want to share their research, but don't have the time, energy, or knowledge to build or maintain a website.

Z-Profile is really just some templates and a bit of data plumbing. It gets data from Zotero, does of bit of processing, then generates a static website using Zola. All you do is set up a collection in Zotero and configure a few things in GitHub.

## Why did I create Z-Profile?

One of the main reasons I created Z-Profile was to make it easier for researchers who want to share green open access versions of their publications. Publishers will often allow authors to make the author accepted manuscript (AAM) version of a publication available through a 'personal website' without any embargo. Using Z-Profile, you just attach a PDF of the AAM version to an item record in Zotero, and it will make your publication available for reading and download. It's a great way of getting your research out to the public as soon as possible.

I also think it's important for researchers to have online profiles that are not wholly dependent on their employer or a company that wants to exploit their data – to have 'a domain of your own' (in the words of the excellent folks at [Reclaim Hosting](https://www.reclaimhosting.com)). Of course, there are some other great options for building a research profile. In particular, I'd strongly suggest you set yourself up on the [Knowledge Commons](https://hcommons.org). But having your own site, under your own domain, gives you extra control and flexibility.

## Requirements

To use Z-Profile you need:

* [Zotero](https://www.zotero.org/) installed and synced to a free Zotero online account
* a [free GitHub account](https://github.com/join)

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

![](https://updates.timsherratt.org/uploads/2026/zotero-bio-item.png)

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

You might already have your publications you want to include in your Zotero library. If so, just drag them to the `z-profile` collection. If not, either capture them from the publisher's site using Zotero, or enter them manually. You can add as many publications to the collection as you want.

If the final, published version of a publication is open access (both free to read and download *and* openly licensed), add the tag `open access` to the Zotero item. This will add an open access badge when the item's details are displayed on the site.

You can choose to display a list of selected publications on the home page. Just add the tag `selected` to any item you want to be included.

### 4. Add green open access versions

If you have green open access versions of articles that you want to share through your site, you can attach PDF copies of the open access versions to publications, and/or point to their location in a repository. If you attach PDFs, they'll be embedded in the article page for easy reading.

First add the publication to your collection (as described above). To attach a PDF right click on the Zotero item and select **'Add Attachment > File'**. Once it's added, tag the attachment to indicate the open access version type. The tag should be one of:

* `aam`: author accepted manuscript
* `preprint`: preprint

**The PDF will only be added to your profile if it has one of these tags.**

If your article is fully open access, you could also add a PDF of your version of record as an attachment and tag it `vor`. However, you might prefer that people access the publication through the publisher's site so that the download stats are collected.

If you have a green open access version in a repository, you can add a link to it. Just right click on the Zotero item and select **'Add Attachment > Web Link'**. Once it's added, tag the attachment to indicate the open access version type as described above. You can also add a title to indicate the name of the repository.

> [!TIP]
> **Version of record**: The final published version of your work, as it appears in the book or journal. Unless the publication is open access, you're probably not allowed to share this online.
>
> **Author Accepted Manuscript**: The version of your work after you have made any changes required by peer review, but before it is copy edited and formatted by the publisher. Under publishers' green open access or 'self archiving' policies, you can probably share this, though there may be restrictions or conditions.
>
> **Preprint**: The version of your work that you originally submitted for publication, before any peer review or editorial comments. You can share this.

### 5. Get your Zotero credentials

Once you've added all your publications to your `z-profile` collection, it's time to build the site. First you need to gather some information from Zotero that will allow your site to access the collection data – an API key, and your user ID.

* Go to the Zotero log in page and enter your details.
* Once you're logged in, click on your account name in the top menu and select 'Settings'.
* On the 'Settings' page click on 'Security' in the side menu.
* Scroll down the 'Security' page until you get to the section headed 'Applications'.
* Click on the **Create new private key** button.

![](https://updates.timsherratt.org/uploads/2026/zotero-newapi-key.png)

* Give your key a meaningful name, eg. `z-profile key`.
* Under 'Personal Library', tick the boxes next to 'Allow library access' and 'Allow notes access'.
* Click on the **Save Key** button.
* Your API key will then be displayed – **copy it immediately** as it won't display again!
* Back on the 'Security' page, look for the 'User ID' heading in the 'Applications' section and copy your user ID.

![](https://updates.timsherratt.org/uploads/2026/zotero-api-key.png)

Make sure you have your API key and user ID saved and ready, as you'll need to share them with GitHub.

### 6. Generate your GitHub repository

Now you can create your own `z-profile` GitHub repository.

* Make sure you're logged in to your GitHub account.
* Go to the [Z-Profile GitHub repository](https://github.com/wragge/z-profile/).
* Click on the green **Use this template** button and select 'Create a new repository'.
* In the 'Repository name' box, enter a name that has the format `[your GitHub username].github.io`. My user name is `wragge`, so I'd enter `wragge.github.io`. Using this as a repository name will make it easy for you to publish your site using GitHub Pages.
* Click on the green **Create repository button**

![](https://updates.timsherratt.org/uploads/2026/z-profile-create-repo.png)

You'll be redirected to your new repository.

### 7. Add your Zotero credentials to GitHub

Now you need to add your Zotero credentials to your new repository so that it can access your data in Zotero.

* Click on 'Settings'.
* Click on 'Secrets and variables > Actions'.

![](https://updates.timsherratt.org/uploads/2026/github-secrets.png)

* Click on the green **New repository secret** button.
* In the 'Name' box enter `ZOTERO_ID` and in the 'Secret' box enter your Zotero user ID.

![](https://updates.timsherratt.org/uploads/2026/github-add-secret.png)

* Click on the green **Add secret** button to save it.
* Now repeat this process to add a secret named `ZOTERO_KEY` that contains your Zotero API key.

Under 'Repository secrets' you should now have two secrets named `ZOTERO_ID` and `ZOTERO_KEY`.

![](https://updates.timsherratt.org/uploads/2026/github-zotero-secrets.png)

### 8. Run the GitHub action

Ok, you're now all set. It's time to generate your site!

* Click on 'Actions' in the top menu of your GitHub repository.
* Click on 'Build Z-Profile site' in the left hand menu.
* First click on the **Run workflow** dropdown and then click on the green **Run workflow** button.

Z-Profile will now pull your data from Zotero and generate your site. To view the status of the current process, click on 'Actions' again. You'll see 'Build Z-Profile site' listed. Once the icon next to the action goes green, you'll know it's finished successfully.

The process saves your site in two places – in the `gh-pages` branch of your repository, and in a zip file. To view them:

* Click on 'Code' to go back to your repositories home page.
* To download the zip file, click on 'profile.zip', then click on the download icon.
* To view the files in the `gh-pages` branch, click on the 'main' dropdown and select `gh-pages`.

Your site has now been generated, but it's not published yet.

## Publishing your site

Z-Profile builds a 'static' site – it's basically just a collection of HTML files, with associated assets, that can be published on almost any web server. Here's a couple of options.

I'll be adding some more documentation to this section.

### Option 1: GitHub Pages

Publishing on GitHub Pages is quick and easy, but might not be the best long-term option.

* Go to your Z-Profile GitHub repository (where your files were generated)
* Click on 'Settings'.
* Click on 'Pages'.
* Look at the 'Build and deployment' section.
* Under 'Source' select 'Deploy from a branch'.
* Under 'Branch' select `gh-pages` from the first dropdown.
* Click on the **Save** button.

A process will run to publish your site, you can check the status by clicking on 'Actions'. Once it's finished you can visit your site by pointing your browser at: `[your GitHub username].github.io`. You'll notice that the web address is the same as the repository name. My GitHub username is `wragge`, so my site is at <https://wragge.github.io>.

But, of course, we've learnt not to trust in the longevity of tech services. Who knows how long GitHub (owned by Microsoft) will continue to support GitHub Pages? To guard against this danger, and to assert your own online identity, I'd strongly suggest you register a domain name and [link it to your GitHub Pages site](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages). That way you can move your site at any time without breaking any links. Unfortunately, this does add to the complexity, as you'll need to register your domain with a domain registrar, update your domain records to point to your GitHub site, and then make some changes to your GitHub repository.

### Option 2: A web host with CPanel

Many web hosting companies, such as [Reclaim Hosting](https://www.reclaimhosting.com), can quickly set you up with a domain name and a CPanel account. Using CPanel's file manager you can upload the `profile.zip` and extract the files into the `public_html` folder.

## Updating your site

To update your site:

* Make your changes in Zotero (you can change your bio information and add or remove publications).
* Run the GitHub action again.

If you're publishing through GitHub Pages you don't need to do anything else. Your updated site will be published automatically.

If you're using another web host you'll need to download the zip file and upload it to your host, replacing any existing files.