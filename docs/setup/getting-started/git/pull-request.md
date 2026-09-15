---
sidebar_position: 4
---
# Making a Pull Request

A **pull request** is a GitHub-specific thing. It just means that you want a codebase to merge your changes on one of your branches into one of their branches--usually to their `master` branch. Before we can do this, our remote GitHub repository (origin) needs to know about the beautiful branches and commits we've created locally, so we upload or **push** those changes to the remote.

### 5.2 Making a pull request

Now, the fun part. We'll go to GitHub now and make a pull request for our funny feature.

![makingapullrequest.png](/img/general-development/setup/git-for-the-ss14-developer/makingapullrequest.png)

Add a description, a nice title, some screenshots, and hopefully it gets merged.

## Checking out a PR's changes locally

Ok, this one is a little difficult. There's a couple ways to do this:

### Github CLI

Install github's fancy CLI and do this:

```
gh pr checkout [pr number]
```

Neat.

### Changing .git/config

Go into your .git folder (hidden by default--may need to enable showing hidden folders in Windows), and open up the 'config' file. There should be a bit that looks something like:

```
[remote "upstream"]
    url = https://github.com/space-wizards/space-station-14
    fetch = +refs/heads/*:refs/remotes/upstream/*
```

Add a line to this that reads `fetch = +refs/pull/*/head:refs/remotes/upstream/pr/*`, so that section should now look like:

```
[remote "upstream"]
        url = https://github.com/space-wizards/space-station-14
        fetch = +refs/heads/*:refs/remotes/upstream/*
        fetch = +refs/pull/*/head:refs/remotes/upstream/pr/*
```

Now, `git fetch upstream`. This method is great if you're a maintainer, but it also.. fetches every branch that's still up from every PR that's been opened, so not fantastic if you just wanted one thing. From here, you can `git checkout upstream/pr/[pr number]` to check out their branch. This is basically what GitHub CLI does but less sophisticated.

### Adding a new remote

This method kinda sucks because it takes a while but if you want to check out someone else's fork of the game and their branches it's pretty nice.

Not actually that hard but its confusing if you don't know Git very well. Set up a remote to the user's remote repository, fetch their branches, and then checkout their branch:

```
git remote add [username] https://github.com/[username]/space-station-14
git fetch [username]
git checkout [username]/[branch name]
```

This also lets you make PRs to their remote branch, if you so desired.