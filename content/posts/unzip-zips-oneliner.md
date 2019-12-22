Title: Unzip a bunch of zips in a oneliner
Started: 2019-12-22 15:21:42
Date: 2019-12-22 15:21:42
Slug: unzip-zips-oneliner
Location: Home
Authors: Michiel Scholten
Category: howto
Tags: desktop, howto, linux, tech
Status: published

Ever needed to unzip a bunch of zip files into their own directory and you don't want to do so one by one? No? Well, here I have a oneliner for you anyway:

```
ls -1 *.zip | while read zf; do echo ${zf::-4}; unzip "$zf" -d "${zf::-4}"; done
```

This lists all the zip files in the current directory, and pipes them to unzip, which creates a directory with their filenames without the `.zip` extension in the process with the `-d` command line argument. `${zf::-4}` here echoes the contents of the `$zf` variable without its last four characters (the `.zip` in this case).

Piping the results of `ls` this way also takes care of the issues that bash has with spaces in file names. Be sure to double quote the `$zf` variable though when using it so no space escapes.

This command is especially useful when the zips do not contain a toplevel directory themselves, so they would uncompress in your current working directory, creating a nice little mess (looking at you, Bandcamp).

Of course, when you have a bunch of zips that actually behave, it could be simplified to:

```
ls -1 *.zip | while read zf; unzip "$zf"; done
```

Done :)
