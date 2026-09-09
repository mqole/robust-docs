---
sidebar_position: 1
---
# Guide to Editing Docs

Hello! As you may be able to notice, this docs site is completely open source and free to edit on GitHub. You can see the GitHub page for this site at [https://github.com/mqole/robust-docs](https://github.com/mqole/robust-docs).

If you want to get an idea of what features are at your disposal when writing documentation, go to the [Docs Example Page](./docs-example-page).

## Style

Documentation should be written in a [technical communications style](https://ohiostate.pressbooks.pub/feptechcomm/chapter/3-writing-style/). Effective technical communications are [concise, precise, direct, and well organized](https://ohiostate.pressbooks.pub/feptechcomm/chapter/3-writing-style/) and should be written in an appropriate [voice and tone](https://ohiostate.pressbooks.pub/feptechcomm/chapter/3-1-voice-tone/) using [correct mechanics and grammar](https://ohiostate.pressbooks.pub/feptechcomm/chapter/3-2-mechanics-grammar/), citing relevant sources where needed.

## Making basic edits

If you just want to make a basic edit of a page, simply follow these steps:

1. Create an account on GitHub, or log in if you already have one.

2. Fork the [mqole/robust-docs](https://github.com/mqole/robust-docs) repo on GitHub. *(Yes, I know it's the wrong link in this image. I don't want to get a new image.)*

![](/img/meta/create-fork.png)

3. Click the 'View & Edit Page on GitHub` icon in the very top right of any page on this site.

![](/img/meta/edit-page-button.png)

4. Click the 'Edit this file' button at the top right of the file view.

![](/img/meta/edit-file.png)

5. Make your changes, then commit & create a pull request! We'll handle the rest.

## Building

If you want to locally build the docs, you'll need to download [Node.js](https://nodejs.org/en/download/) version 20.0 or above (which can be checked by running node -v).

`cd` into the root of the directory and run `npm run start` to build and locally host the documentation at `localhost:3000`.

## Testing changes

If you've made a PR, the easiest way to test your changes, since they're just markdown, is to view them in GitHub's own markdown viewer in the `Files changed` tab. You can also use a local markdown previewer extension for something like [VSCode](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced). 

If you want to see what your changes will look like on the site, you'll have to locally build the docs as instructed above.