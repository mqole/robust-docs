---
sidebar_position: 9
---
# Git Command Cheat Sheet

Just need a quick reference for what command does what? Here's a (non-exhaustive) cheat sheet.

If something is in `[]` square brackets, it means that you should replace that content with your own arguments. If something is in `()` regular brackets, you can optionally omit that argument.

## Setup

- `git init`: Creates a new Git repository in the current folder.
- `git clone [GitHub repository URL]`: Initializes a new git repository from the URL in the current folder.

## Branches & Remotes

- `git branch`: View all existing branches.
- `git branch [new branch name]`: Creates a new branch with the specified name from the working tree, but does not switch to it.
- `git branch -d [branch name]`: Deletes the specified branch.
- `git checkout [branch name]`: Switches your working tree to the selected branch.
- `git checkout -b [new branch name]`: Creates a new branch with the specified name from the working tree and switches to it.
- `git remote (-v)`: List all current remotes, with the option to additionally view the associated URLs.
- `git remote add [remote name] [GitHub repository URL]`: Creates a new remote with the desired name, pointing to the specified URL.
- `git push [remote name] [local branch]`: Pushes the specified branch to the specified remote, potentially creating a new branch on the remote repository if no such branch exists.
- `git merge [local branch] ([local branch])`: Merges changes from the first specified local branch to the second specified local branch. If no second branch is listed, the command will default to using the current branch.

## Staging

- `git status`: View all staged and non-staged changes made in the working tree.
- `git add [filepath]`: Add a specific file modified in the working tree to the staging area.
- `git add -a`: Add all modified files in the working tree to the staging area.
- `git rm [filepath]`: Remove a specific file from the staging area.
- `git commit (-m [commit message])`: Commit staged changes to the current branch. Not including a commit message will prompt you to enter a commit message in the command line.

## Updating

- `git submodule update --init --recursive`: Updates all submodules within your repository.
- `git fetch [remote]`: Fetches the latest changes from the specified remote.
- `git pull [remote] [remote branch]`: Pulls changes from the specified branch to your working tree.

## Other Helpful Commands

- `git reset --hard HEAD ([file])`: Reverts the specified file (or all files, if unspecified) in the working tree to the state they were at the most recent commit. **You cannot undo this command**.
- `git revert HEAD`: Reverts your working tree to the current commit. `HEAD` just means the commit you're currently on.
- `git revert HEAD~1`: Reverts your working tree to the previous commit. `HEAD~1` means "`1` commit before `HEAD`". You can replace `1` with whatever value you need.
- `git revert [commit hash]`: Reverts your working tree to the specified commit hash.
- `git log --oneline`: Shows a list of short commit hashes (unique IDs for commits), their messages, and their branches and tags.

## Example of a Possible Git Workflow

To get everything in your head and to summarize it all, here's an example workflow for making several pull requests using Git Bash commands.

```python
git checkout master # Before we create a new branch, we should be on master.
git fetch upstream # We'll fetch any new changes from the SS14 repo..
git merge upstream/master # ..and merge them into our master branch.

git checkout -b my-new-feature # Make a new branch for the feature
# ...local changes later...
git add -A # Add all of our local changes to the staging area
git commit -m "Fix spaghetti explosions" # Commit them
git push origin my-new-feature # and push them to our remote

# Now, I want to work on a different pull request.

git checkout master

# It hasn't been too long, and nothing important was merged,
# so I won't fetch and merge changes again, just make a new branch.

git checkout -b another-feature
# ...local changes later...
git add -A
git commit -m "Deletes nuclear operatives"

# I committed, but then I realized my commit was entirely wrong 
# and I'll try again later.

git revert HEAD
git checkout master

# ...a week later...

# A lot of new stuff was merged, so let's update our branch.

git fetch upstream
git merge upstream/master master
git checkout another-feature
git merge master

# Now we'll make changes and push again, this time correctly.

# ...local changes later...
git add -A
git commit -m "Adds Highlander gamemode"
git push origin another-feature

# Made both PRs, both were merged, so we're done here

git checkout master
git branch -d my-new-feature # Delete both old branches
git branch -d another-feature

```