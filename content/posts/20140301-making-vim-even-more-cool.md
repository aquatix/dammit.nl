Title: Making vim even more cool
Date: 2014-03-01 11:41:28
Modified: 2014-03-04 11:32:00
Slug: 20140301-making-vim-even-more-cool
Location: Home
Authors: Michiel Scholten
Category: howto
Tags: dev, howto, vim, work
Image: http://dammit.nl/images/content/20140301_vimrc.png

![Screenshot of vim with this article](http://dammit.nl/images/content/20140301_vimrc.png)

vim, the final editor. Well, for some people at least. People like me, we like to type their files, code and more inside of dark-coloured windows, mainly terminals and do not really care if those files are local on their laptop, on the server at their feet or on some virtual node on a cluster in a data center around the globe which they don't even really know the location of.

A lot of people think it's weird and a little bit daunting and steer clear from it. Others just miss functionality from their favourite IDE.

vim has a lot of functionality already built in, which is worth exploring in itself. Apart from that, it is extensible, something people take advantage of by creating extensions with nifty extra things.

Using [pathogen.vim](https://github.com/tpope/vim-pathogen) is the easiest way of installing extensions to vim. You can clone its repository to a directory and symlink pathogen.vim to ~/.vim/autoload/pathogen.vim but it's more contained if you clone to ~/.vim/bundle/ like so:

	mkdir -p ~/.vim/bundle

	cd ~/.vim/bundle

	git clone https://github.com/tpope/vim-pathogen.git

	# Really useful statusbar
	git clone https://github.com/bling/vim-airline

	# Version control 'added line', 'changed line', 'removed line' notes in the gutter (next to the line numbers)
	git clone https://github.com/mhinz/vim-signify

	# Better showing of open buffers (open files)
	git clone https://github.com/bling/vim-bufferline

	# Display tags of the current file ordered by scope
	git clone https://github.com/majutsushi/tagbar.git

	# The unite or unite.vim plug-in can search and display information from
	# arbitrary sources like files, buffers, recently used files or registers.
	git clone https://github.com/Shougo/unite.vim.git

	# Fuzzy file, buffer, mru, tag, etc finder (similar to unite)
	git clone https://github.com/kien/ctrlp.vim.git

The [airline.vim](https://github.com/bling/vim-airline/) page has a nice list of plugins. Some of these are 
[signify](https://github.com/mhinz/vim-signify),
[bufferline](https://github.com/bling/vim-bufferline),
[tagbar.vim](https://github.com/majutsushi/tagbar),
[unite.vim](https://github.com/Shougo/unite.vim),
[CtrlP.vim](https://github.com/kien/ctrlp.vim).

A simpeler version control gutter is [gitgutter](https://github.com/airblade/vim-gitgutter), which can be your choise if all you use is git.

*Update 20140304*: I found [Vundle](https://github.com/gmarik/Vundle.vim) which makes installing bundles even more simple. Be sure to check it out.

Install the [Zenburn colour scheme](https://github.com/jnurmine/Zenburn) for some nice colour highlighting: `git clone https://github.com/jnurmine/Zenburn.git` and symlink or copy the zenburn.vim file to `~/.vim/colors`. This also works in the Pathogen way, so you can also just clone that repository into ~/.vim/bundle and be done!

This all results in this ~/.vimrc

	" pathogen.vim for installing nifty stuffs
	runtime bundle/vim-pathogen/autoload/pathogen.vim
	execute pathogen#infect()

	syntax enable
	set number

	if &term == "xterm" || &term == "screen-bce"
	set t_Co=256
	colorscheme zenburn
	endif

	" paste and autoindent
	set pastetoggle=<F10>

	" create a bar for airline
	set laststatus=2
	let g:airline_powerline_fonts = 1

which makes vim look like this:

![vimrc](http://dammit.nl/images/content/20140301_vimrc.png)

To get the nice fonts in the airline bar at the bottom, get the Powerline repo and use its fonts. In some directory (temporary if you like), do a `git clone https://github.com/Lokaltog/powerline.git`.

Copy powerline/font/PowerlineSymbols.otf to `~/.fonts/` (or another X font directory, like a system-wide `/usr/share/fonts/truetype/Powerline`).
Run `fc-cache -vf ~/.fonts` to update your font cache (`fc-cache -vf  /usr/share/fonts/truetype/Powerline`).
Move 10-powerline-symbols.conf to either `~/.fonts.conf.d/` or `~/.config/fontconfig/conf.d/` or the system-wide `/etc/fonts/conf.d/`, depending on your fontconfig version.  [Read more on the Powerline fonts](https://powerline.readthedocs.org/en/latest/installation/linux.html#font-installation).
