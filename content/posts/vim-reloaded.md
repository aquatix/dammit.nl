Title: vim reloaded
Started: 2014-11-28, 2015-01-24, 2017-04-26 15:48:00, 2017-05-19, 2018-01-05, 2019-11-26
Date: 2017-04-26 15:48:00
Slug: vim-reloaded
Location: Home
Authors: Michiel Scholten
Category: howto
Tags: linux, desktop, howto, vim
Status: draft


An update about what I do with vim, making it more powerful and taking away some of the envy I have for the excellent IDE's out there (for example PyCharm and the rest of the IntelliJ family by JetBrains - try it, it's awesome).


I will be talking about my vim configuration as [it is currently in my dotfiles repository](https://github.com/aquatix/dotfiles/blob/49354e122a3b0bd902bd60123cd30307b79f0eb2/.vimrc). You can always find [the latest version here](https://github.com/aquatix/dotfiles/blob/master/.vimrc) and maybe have some inspiration from [the rest of my dotfiles](https://github.com/aquatix/dotfiles).

To get an impression how things currently look, take a look at this example:

[todo]

In the years since the [first time I showed my vim setup]({filename}../posts/20140301-making-vim-even-more-cool.md), I went through:

[![vim as python IDE](https://shuttereye.org/images/da/dad25a53d293b7d2_2000-2000.png)](https://shuttereye.org/various/screenshots/20170519_vim_python.png/view/)

and

[![vim with ctrl+p quick lookup](https://shuttereye.org/images/88/88a1a1a18185a8d0_2000-2000.png)](https://shuttereye.org/various/screenshots/20170519_vim_ctrlp.png/view/)

to arrive at the above.


## Vundle as plugin manager

There are various plugin managers, and I settled on [Vundle](https://github.com/VundleVim/Vundle.vim), like [I mentioned in 2014]({filename}../posts/20140301-making-vim-even-more-cool.md). This still serves me well.


## fzf

I bound looking through buffers to <kbd>;</kbd>, as I use buffers quite a lot. This way I can quickly switch to another file I have open.

Find more tricks to do with fzf and vim in this article: [Fuzzy finding with FZF.vim](http://tilvim.com/2016/01/06/fzf.html).

Quickly opening files is done through <kbd>leader</kbd>+<kbd>o</kbd>, and looking through the content of files is bound to <kbd>leader</kbd>+<kbd>f</kbd>. This file search leverages the awesome grepping powers of [ripgrep]():

```
" Find term where term is the string you want to search, this will open up a
" window similar to :Files but will only list files that contain the term
" searched
" https://medium.com/@crashybang/supercharge-vim-with-fzf-and-ripgrep-d4661fc853d2
command! -bang -nargs=* Find call fzf#vim#grep('rg --column --line-number --no-heading --fixed-strings --ignore-case --hidden --follow --color "always" '.shellescape(<q-args>).'| tr -d "\017"', 1, <bang>0)

" Files command with preview window
command! -bang -nargs=? -complete=dir FilesPreview
  \ call fzf#vim#files(<q-args>, fzf#vim#with_preview(), <bang>0)

" Simply type ; to search through buffers, leader-o to search through file
" names, leader-O to search through file names, showing a preview window,
" \t for tags, \c for (Git) commits and \f to search through contents of files
nmap ; :Buffers<CR>
nmap <Leader>o :Files<CR>
nmap <Leader>O :FilesPreview<CR>
nmap <Leader>t :Tags<CR>
nmap <Leader>c :Commits<CR>
nmap <Leader>f :Find<CR>
nmap <Leader>l :Lines<CR>

```


## ctrl+p

Alternatively, one can still quickly find and open files through the trusty ol' <kbd>ctrl</kbd>+<kbd>p</kbd>:

```
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
```

[![vim with ctrl+p quick lookup](https://shuttereye.org/images/88/88a1a1a18185a8d0_2000-2000.png)](https://shuttereye.org/various/screenshots/20170519_vim_ctrlp.png/view/)


## ctags is missing

You need exuberant-ctags installed, otherwise there will be an error. You can do this with `sudo apt install exuberant-ctags` or `brew install ctags`.


## Sanity checking of your projects

[Syntastic](https://github.com/scrooloose/syntastic) is fantastic. Sorry, I had to say it that way :) It uses all kinds of tools to check your code for errors, code conventions and more. For Python, you can do PEP-8 checking and such, for example.

However, I since moved on to [ale](https://github.com/dense-analysis/ale), which is even better. It's asynchronous and just has great support for a lot of linters and checkers, like pylint, flake-8, and bandit for Python.

My choice for Python and Django is to use pylint and the [pylint-django plugin](https://github.com/landscapeio/pylint-django):

    pip install pylint
    pip install pylint-django

Installing both in the virtualenv of your project will make vim pick up the right modules, so imports get recognised (very useful for imports from modules in your virtualenv, otherwise pylint will get *really* chatty).

Two other good checkers are flake8 and bandit. Flake8 does a lot of similar things to pylint, and bandit does security checking, notifying you of potentially unsafe ways of Doing Things&trade;.

    pip install flake8
    pip install bandit


## Further reading

Another good read is [Vim After 15 Years](https://statico.github.io/vim3.html), in which Ian Langworth describes his own setup. We have some similarities, and of course some differences.
