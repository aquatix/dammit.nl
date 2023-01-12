Title: Transplanting files and directories to other repository keeping Git history
Started: 2023-01-12 10:26:47
Date: 2023-01-12 10:26:47
Slug: transplanting-files-keeping-git-history
Location: Home
Authors: Michiel Scholten
Status: published
Category: howto
Tags: dev, howto, linux, tech

Recently, I wanted to split off a few files from a Git repository in which I keep notes to a repository of their own. Reason was that they served an entirely different purpose than the rest, so it made more sense to separate the two sets.

However, they had quite some commit history in the original repository, and I didn't want to lose that. Thankfully, I found a neat way of doing just that.

If your history is sane, you can take the commits out as patch and apply them in the new repository:

```bash
cd repository
git log --pretty=email --patch-with-stat --reverse --full-index --binary -m --first-parent -- path/to/file_or_folder > patch
cd ../another_repository
git am --committer-date-is-author-date < ../repository/patch 
```

In the `patch` file (which you can of course name however you like), you can edit the paths if you like before importing again in the other repository; it is just a text file with all the commits in email format. Editing paths is for example useful when you have files in some subdirectory, and now want them in the root of the new repository, or in another subdirectory, or rename the files altogether.

Alternatively, you can do it in one line (of course skipping any renaming this way):

```bash
git log --pretty=email --patch-with-stat --reverse --full-index --binary -m --first-parent -- path/to/file_or_folder | (cd /path/to/new_repository && git am --committer-date-is-author-date)
```

[source](https://stackoverflow.com/a/11426261)
