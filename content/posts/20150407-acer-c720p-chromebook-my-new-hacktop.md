Title: Acer C720p Chromebook: my new hacktop
Date: 2015-04-07 21:39:43
Slug: 20150407-acer-c720p-chromebook-my-new-hacktop
Location: Home
Authors: Michiel Scholten
Category: gadgets
Tags: tech, desktop, linux, dev

After [Chromebook: for fun and profit? @ 2014-10-05]({filename}20141005-chromebook-for-fun-and-profit.md) I got myself an Acer C720p for cheap. It's new, just cheap, as that's how Chromebooks go :) It has a new-fangled touchscreen, which I actually tend to use while on Chrome OS. I hadn't thought I would do so (hey, it's a laptop, why would I smudge the screen?), but it's actually quite convenient when scrolling, pointing, selecting and such. I guess I use it more than on my full-fledged 15.6" laptop as the screen is a lot smaller (tablet-sized basically) and the distance to the screen is smaller, the device being quite small itself and lending for convenient lap-computing.

Apart from it being its ChromeOS self and being decent enough for browsing and tinkering around the web, I bought it as convenient, small, light hacktop. My definition of 'hacktop' is 'small laptop computer that I'm not afraid of throwing in my bag and on which I can do actual work, like programming with a real text editor'. Enter [crouton](https://github.com/dnschneid/crouton). Crouton creates a chroot environment on the Chromebook in which you're actually running (for example) a Ubuntu flavour. Myself, I chose xubuntu 14.04, which is small, fast and thus a great base for installing some development tools on.

As I got myself a model with 4GB ram (always get for the biggest amount of ram, it's so good to have) and SSD of 32GB, I got about 23GB (maybe more) to play with. Installing the `trusty` xubuntu chroot takes less than 1GB of drive space and after installing Python, vim with [my bunch of plugins](https://github.com/aquatix/dotfiles/blob/master/.vimrc), the [PostgreSQL database server (9.4 at the moment)](http://www.postgresql.org/download/linux/ubuntu/) and more, it takes barely more than that.

The last year or so I've been [using vim as my main coding platform/'IDE']({filename}20140301-making-vim-even-more-cool.md) (a follow-up is in the works) so I don't need that much from the device; it runs Firefox (because web development) and some terminals with tmux, tmuxinator and vim with my selection of helpful plugins:

![Hacktop with vim](//dammit.nl/images/content/20150407_hacktop_vim.png)
