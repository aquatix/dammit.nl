Title: Git-based versioning
Started: 2019-02-13 20:09:09
Date: 2019-02-13 20:09:09
Slug: git-based-versioning
Location: Home
Authors: Michiel Scholten
Category: howto
Tags: dev, howto, python, web

So you have this (web) application and you are growing a bit tired of having to manually bump the version number it tells to its users. Also, you would like to see if you are using an up-to-date edition of said app.

Enter your Git repository. When you are running your application from a Git repository (which is fine in my opinion as long as you of course do *not* expose the .git directory to the world), you can leverage (*cringe*) Git to create the version number for you.

Try it yourself: in a terminal, enter a directory in a project that is checked out from Git, then enter the following command:

    git describe --always --tags

This will return a string that is based on the latest tag it could find, the amount of commits following that tag (if any) and the short commit hash of the latest revision. For example `20190213a-3-abc42def`.

Now, you would like to use that in your Python program:

    import os

    # Make sure the working directory is our project
    cwd = os.path.dirname(os.path.realpath(__file__))
    try:
        version = subprocess.check_output(["git", "describe", "--always", "--tags"], stderr=None, cwd=cwd).strip()
    except subprocess.CalledProcessError:
        version = ''

    try:
        # byte string needs to be converted to a string
        version = version.decode("utf-8")
    except AttributeError:
        # version already was a str
        pass

This snippet runs Git in a sub process, makes sure it uses the directory your program resides in as the working directory (web applications and such can have a completely different cwd than you expect), and makes sure the resulting `version` is a proper string.

This code is tested under Python 3 on several Linux distributions.
