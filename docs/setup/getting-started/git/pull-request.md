---
sidebar_position: 4
---
# Pull Requests

You've set up your local branch, made some changes, and committed them to your repository. But if you want your changes to be in-game, you'll need to submit a Pull Request (or PR).

A pull request is just a request that a codebase merge your branch's changes into one of their branches, usually their `master` branch.

:::note
If you're working on a downstream fork which uses a service other than GitHub, these steps may be different. This guide will assume you are using GitHub.
:::

## Making a Pull Request

If you've recently pushed changes to your repository, you may see this "Compare & pull request" popup when you visit your repository or a repository you've forked from on GitHub. Clicking it will autofill the branch that you're sending the pull request from.

![makingapullrequest.png](/img/general-development/setup/git-for-the-ss14-developer/makingapullrequest.png)

If you don't see this popup, you can also manually create a pull request by opening the repository's pull request page, and clicking the button in the top-right labelled "New pull request".

![](/img/general-development/setup/git-for-the-ss14-developer/pullrequest-page.png)

In order to see your branches, you'll need to click "compare across forks".

![](/img/general-development/setup/git-for-the-ss14-developer/pullrequest-forks.png)

From here, you can configure which branch your pull request aims to merge into which! In this example, you can see that I want to merge my `mqole/imp-station-14` repository's `wizden-random-patch` branch into the `space-wizards/space-station-14` repository's `master` branch. You might notice that my repository has a different name, and that's just because I have it set up to work on a downstream fork.

Once you've selected your two branches, you'll be able to see a list of the commits that the pull request will merge, as well as a differential (or 'diff') of all the files that the pull request will change.

![](/img/general-development/setup/git-for-the-ss14-developer/pullrequest-compare.png)

From the above image, clicking the "Create pull request" button will take you to a final page where you can write some information about your pull request that might be helpful for anyone who wants to review your changes.

Most repositories that you make pull requests to will have a pull request template that maintainers will expect you to fill out. WizDen's PR template, for example, asks for a description of your PR, instructions on how to test it, possible screenshots, and a changelog which a GitHub bot will automatically look for.

As a general rule of thumb, **be thorough in your PR description!** Adding images or videos can easily give maintainers or other users an idea of what your proposed changes will look like in game.

![](/img/general-development/setup/git-for-the-ss14-developer/pullrequest-template.png)

## Testing Someone Else's Pull Request

If you want to try out someone else's pull request in-game before it gets merged, you'll need to get a copy of the changes made in the pull request onto your local repository. The low-tech way of doing this is to just edit every file manually, but there are a few much easier methods available.

### The Remote Method

Since a pull request is just a request for branch A to be merged into branch B, by using [remotes](git-setup.md#remotes) to checkout branch A you can view all the contents of the pull request (minus any content that is on branch B but not branch A).

Let's say I want to checkout this pull request:

![](/img/general-development/setup/git-for-the-ss14-developer/pullrequest-example.png)

Here I can see that the repository I want to look at is `Princess-Cheeseballs/space-station-14`, and the branch I want is `fax-machine`. So I'll first add a new remote pointing to `Princess-Cheeseballs`'s repository. That username is a bit long for me to keep typing, so I'll shorten the name of my remote down to `princess`. Then I'll fetch from that remote, and finally checkout the branch:

```bash
git remote add princess https://github.com/Princess-Cheeseballs/space-station-14
git fetch princess
git checkout princess/fax-machine
```

Now that I've set up a remote for this user, I can also make pull requests to their repository if I want to. This method can be a bit tricky if you aren't used to using Git, but it's definitely the most versatile!

### The GitHub CLI Method

CLI stands for Command Line Interface, and there are lots of different ones out there. GitHub has its own [CLI](https://docs.github.com/en/github-cli/github-cli/quickstart) which you can install to make checking out PRs easier.

Once you've installed the CLI, just run this command to checkout the PR branch:

```
gh pr checkout [pr number]
```

And you'll be able to see the PR's changes. This method will create a new branch, but it won't create any additional remotes.

### The .git/config Method

This last method can be helpful if you're a maintainer, but be warned that it will fetch *every branch that's still up from every PR that's been opened*, which may not be ideal if you're working on a codebase with a lot of pull requests.

Go into your `.git` folder (this folder is hidden by default, so you may need to enable showing hidden folders), and open up the `config` file. There should be a section that looks something like:

```
[remote "upstream"]
    url = https://github.com/space-wizards/space-station-14
    fetch = +refs/heads/*:refs/remotes/upstream/*
```

Add a line to this: `fetch = +refs/pull/*/head:refs/remotes/upstream/pr/*`.

The file should now read:

```
[remote "upstream"]
        url = https://github.com/space-wizards/space-station-14
        fetch = +refs/heads/*:refs/remotes/upstream/*
        fetch = +refs/pull/*/head:refs/remotes/upstream/pr/*
```

What we're doing here is instructing Git to fetch from all pull requests in addition to all the remote's branches when we run `git fetch`. This is similar to what GitHub CLI does, but it's a bit more hacky.

