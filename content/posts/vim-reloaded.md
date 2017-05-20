Title: vim reloaded
Started: 2014-11-28, 2015-01-24, 2017-05-19
Date: 2017-04-26 15:48:00
Slug: vim-reloaded
Location: Home
Authors: Michiel Scholten
Category: howto
Tags: linux, desktop, howto, vim
Status: draft


An update about what I do with vim, making it more powerful and taking away some of the envy I have for the excellent IDE's out there (for example pycharm and the rest of the IntelliJ family by JetBrains - try it, it's awesome).


I will be talking about my vim configuration as [it is currently in my dotfiles repository](https://github.com/aquatix/dotfiles/blob/4fb7e926bf353fcf6d66bbcb8f936742f3034142/.vimrc). You can always find [the latest version here](https://github.com/aquatix/dotfiles/blob/master/.vimrc) and maybe have some inspiration from [the rest of my dotfiles](https://github.com/aquatix/dotfiles).

To get an impression how things look, take a look at this example:

[![vim as python IDE](https://shuttereye.org/images/da/dad25a53d293b7d2_2000-2000.png)](https://shuttereye.org/various/screenshots/20170519_vim_python.png/view/)


## Vundle as plugin manager





## ctrl+p

    " Full path fuzzy file, buffer, mru, tag, ... finder
    " Quickly open files, fuzzy search on name
    Plugin 'ctrlpvim/ctrlp.vim'
    "let g:ctrlp_map = '<Leader>t'
    let g:ctrlp_map = '<c-p>'
    " Search in Files, Buffers and MRU files at the same time:
    let g:ctrlp_cmd = 'CtrlPMixed'
    let g:ctrlp_match_window_bottom = 1
    let g:ctrlp_match_window_reversed = 0
    let g:ctrlp_custom_ignore = '\v\~$|\.(o|swp|pyc|wav|mp3|ogg|blend)$|(^|[/\\])\.(hg|git|bzr)($|[/\\])|__init__\.py'
    let g:ctrlp_working_path_mode = 0
    let g:ctrlp_dotfiles = 0
    let g:ctrlp_switch_buffer = 0


[![vim with ctrl+p quick lookup](https://shuttereye.org/images/88/88a1a1a18185a8d0_2000-2000.png)](https://shuttereye.org/various/screenshots/20170519_vim_ctrlp.png/view/)


## Ctags is missing

You need exuberant-ctags installed, otherwise there will be an error. You can do this with `sudo apt install exuberant-ctagsor` or `brew install ctags`.


## Sanity checking of your projects

[Syntastic](https://github.com/scrooloose/syntastic) is fantastic. Sorry, I had to say it that way :) It uses all kinds of tools to check your code for errors, code conventions and more. For Python, you can do PEP-8 checking and such, for example.

My choice for Python and Django is to use pylint and the [pylint-django plugin](https://github.com/landscapeio/pylint-django):

    pip install pylint
    pip install pylint-django

Installing both in the virtualenv of your project will make vim pick up the right modules, so imports get recognised (very useful for imports from modules in your virtualenv, otherwise pylint will get *really* chatty).

