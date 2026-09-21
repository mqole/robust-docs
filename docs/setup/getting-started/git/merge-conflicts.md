---
sidebar_position: 3
---
# Merge Conflicts

<WipHeader/>

*WIP i'll write a better guide for this later because it's important*

A nasty little maintainer has told you to 'resolve conflicts' or your PR 'wont be merged'. What an asshole! Thankfully, it's not too hard.

First, you're going to want to update your local `master branch`. See above for how to do that.

When you run `git merge master [local branch]`, it'll either do it cleanly (woohoo) or tell you you have to resolve conflicts (wahhhh). 

All you need to do to resolve conflicts manually is go into the files that are conflicting, remove all the `>>>>HEAD` and `===== <<<<master` nonsense (just notates where the changes originated) and then edit the file so that it properly integrates both sets of changes. Sometimes this is easy, sometimes it's hard. If it's hard, you probably know what you're doing. After that, just `git commit`.

Atlassian has a really good guide for this [here](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts)
