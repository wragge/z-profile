# Z-Profile

Build your own research profile using [Zola](https://www.getzola.org) and [Zotero](https://www.zotero.org/).

Example site: <https://wragge.github.io>

See [the documention](https://wraggelabs.com/z-profile-docs/) for a full explanation of how you can generate your own profile.

## Features

* Automatically generates a personal home page with biographical note, photo, social media accounts, and selected publications.
* Individual page for each publication, with embedded PDF viewer for attached green open access versions.
* Embedded metadata in publication pages for easy capture by Zotero.
* Generates a static site that can be published using GitHub Pages or any web host.

## What is Z-Profile?

Z-Profile helps non-technical researchers create their own simple, online research profile that shares biographical details and a list of publications. It's deliberately minimalist in design and function. Z-Profile is intended for people who want to share their research, but don't have the time, energy, or knowledge to build or maintain a website.

Z-Profile is really just some templates and a bit of data plumbing. It gets data from Zotero, does of bit of processing, then generates a static website using Zola. All you do is set up a collection in Zotero and configure a few things in GitHub.

## Getting started

### Requirements

The only requirements are:

* to have [Zotero](https://www.zotero.org) installed
* to [create a free Zotero account](https://www.zotero.org/user/register/)
* and to use your Zotero account to set up [data and file syncing](https://www.zotero.org/support/sync)

If you want to use GitHub to build and publish your site, you'll also need a [free GitHub account](https://github.com/join).

### Your Zotero library

The first step is to [prepare your Zotero Library](https://wraggelabs.com/z-profile-docs/zotero/).

### Building

Once your Zotero library is ready, you have a choice. You can:

- build your site with the [Z-Profile Builder](https://wraggelabs.com/z-profile-docs/z-profile-builder/)
- or build your site using [GitHub](https://wraggelabs.com/z-profile-docs/github-build/)

The Z-Profile Builder is the easiest option – all it takes is a couple of clicks and you'll have a zip file containing your new site.

The GitHub option requires more setup and configuration, but can be useful if you're planning to publish using GitHub Pages.

### Publishing

Once you've built your site, you'll have a collection of HTML files and associated assets. This is what's called a 'static site' and can be published just about anywhere with minimal configuration.

[GitHub Pages](https://wraggelabs.com/z-profile-docs/github-publish/) is free, and if you use the GitHub build option, publishing is just a matter of flicking a few switches in your GitHub repository.

But, of course, we've learnt not to trust in the longevity of tech services. Who knows how long GitHub (owned by Microsoft) will continue to support GitHub Pages? Also, using a custom domain name adds considerably to the complexity.

If you're willing to pay a small amount for a web hosting account (or already have access to a web server), you'll probably find [self-hosting an easier option overall](https://wraggelabs.com/z-profile-docs/web-host-publish/). Many web hosting companies, such as [Reclaim Hosting](https://www.reclaimhosting.com/), can quickly set you up with your own domain name and a CPanel account. Then it's just a matter of uploading your site to their servers.

## Licence

Z-Profile was created by [Tim Sherratt](https://timsherratt.au) in 2026. All original code is dedicated to the public domain under a CC0 1.0 Universal Deed.