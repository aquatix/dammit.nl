Title: Holiday vim tweaking
Started: 2020-01-04 10:38:21
Date: 2020-01-04 10:38:21
Updated: 2020-01-05 10:50:00
Slug: holiday-vim-tweaking
Location: Home
Authors: Michiel Scholten
Category: projects
Tags: dev, linux, tech, vim
Image: https://shuttereye.org/galleries/various/screenshots/20200104_vimrc_terminal.png
Status: published

![~/.vimrc in terminal, themed](https://shuttereye.org/galleries/various/screenshots/20200104_vimrc_terminal.png)

Some people binge-watch series when taking some time off, some read books, some enjoy comics, some take time off from computers for a bit, and some spend some hours cleaning up their vim configuration file.

This holiday, I did all of the above.

Yesterday, instead of spending one day gaming (which has become my yearly tradition) [I performed some spring cleaning to my .vimrc](https://github.com/aquatix/dotfiles/compare/002258322a9136bf50b5f00fa29bbda52d9be89d...b848174960d9777d5ec96d3fd18bbe5aec935a5a). This was a bit overdue, as it accumulated its share of cruft over the years, and the internal organisation was lacking. I removed old plugins, did some debugging, moved around settings so they are clustered by function, and moved from good ol' [Vundle](https://github.com/VundleVim/Vundle.vim) to [vim-plug](https://github.com/junegunn/vim-plug), which does its thing asynchronously, so faster, and has some other tricks up its sleeve (like the ability to clean up directories).

This all lead to a [tidier file](https://github.com/aquatix/dotfiles/blob/b848174960d9777d5ec96d3fd18bbe5aec935a5a/.vimrc), which I will use to finalise my follow-up to [the ancient post detailing my .vimrc from 2014]({filename}20140301-making-vim-even-more-cool.md).
