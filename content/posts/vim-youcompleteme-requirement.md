Title: YouCompleteMe requiring a rather new vim
Started: 2021-01-08 10:16:38
Date: 2021-01-08 10:16:38
Slug: vim-youcompleteme-requirement
Location: Home
Authors: Michiel Scholten
Status: published
Category: howto
Tags: dev, howto, opensource, tech, vim

If you are even remotely using the same workflows as me, you will be using vim quite a bunch, and not limited to one machine with a given operating system. You might also have taken a liking to YouCompleteMe to serve as the code/word completion solution of choice.

The [YouCompleteMe project](https://github.com/ycm-core/YouCompleteMe) has a policy to support the Vim version that's in the latest LTS of Ubuntu. That's currently Ubuntu 20.04 which contains vim-nox at v8.1.2269. Which is fine, and enables their codebase to move forward and not be burdened with a lot of if-else's for older versions of vim and such.

However.

I am also using Debian 10 and CentOS machines, which are not as fly as the latest Ubuntu release. Debian 10 Buster for example (among other places used as the Linux VM on Chrome OS), has 8.1.0875 which is an amount of patch levels below the minimal requirement set by YCM. Commit '[d98f896](https://github.com/ycm-core/YouCompleteMe/commit/d98f896)' of YCM is the latest compatible with this version, so I could pin the plugin on that revision with a `Plug 'Valloric/YouCompleteMe', { 'commit':'d98f896' }`. On the other hand, as mentioned, I'm using multiple devices, quite some actually having a more recent vim, so on those I want the latest and greatest YCM available to me.

Enter the patch-level/version check available to be used in vim config files. In `~/.vimrc` I changed my regular `Plug` line into the following:

```
if has('patch-8.1.2269')
    " Latest YCM needs at least this version of vim
    Plug 'ycm-core/YouCompleteMe'
else
    " Version compatible with the vim in Debian 10 buster
    Plug 'ycm-core/YouCompleteMe', { 'commit':'d98f896' }
endif
```

And done :)

On the older machines, manually check out the relevant YCM commit, or just remove `~/.vim/plugged/YouCompleteMe` and update your vim plugins (`:PlugUpdate` with [vim-plug](https://github.com/junegunn/vim-plug)).

[Relevant bugreport](https://github.com/ycm-core/YouCompleteMe/issues/3764).
