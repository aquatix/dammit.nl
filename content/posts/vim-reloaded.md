Title: vim reloaded
Started: 2014-11-28, 2015-01-24
Date: 2017-04-26 15:48:00
Slug: vim-reloaded
Location: Home
Authors: Michiel Scholten
Category: howto
Tags: linux, desktop, howto, vim
Status: draft


An update about what I do with vim, making it more powerful and taking away some of the envy I have for the excellent IDE's out there (for example pycharm and the rest of the IntelliJ family by JetBrains - try it, it's awesome).


## Ctags is missing

You need exuberant-ctags installed, otherwise there will be an error. You can do this with `sudo apt-get install exuberant-ctagsor` or `brew install ctags`.


## Sanity checking of your projects

[Syntastic](https://github.com/scrooloose/syntastic) is fantastic. Sorry, I had to say it that way :) It uses all kinds of tools to check your code for errors, code conventions and more. For Python, you can do PEP-8 checking and such, for example.

My choice for Python and Django is to use pylint and the [pylint-django plugin](https://github.com/landscapeio/pylint-django):

    pip install pylint
    pip install pylint-django

Installing both in the virtualenv of your project will make vim pick up the right modules, so imports get recognised (very useful for imports from modules in your virtualenv, otherwise pylint will get *really* chatty).

