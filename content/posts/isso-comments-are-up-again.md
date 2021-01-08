Title: isso comments are up again
Started: 2021-01-08 11:45:48
Date: 2021-01-08 11:45:48
Slug: isso-comments-are-up-again
Location: Home
Authors: Michiel Scholten
Status: published
Category: howto
Tags: communication, dev, hosting, howto, tech, web

Commenting had been broken since the 19th of December because of the host having upgraded to Python 3.9 and [isso](https://github.com/posativ/isso) breaking. I tried installing it anew from pip, but there is still a really old version on there; installing it as egg directly from its Git repository[^1] kind of works, but the Javascript needs to be compiled, otherwise it will not work. `require.js` and such have been removed from the codebase, so just linking to the regular JS files does not work. Also, on my Ubuntu 20.10 machine, somehow `make js` does not want to build the minified Javascript files either.

Instead, I borrowed the [embed.min.js](https://raw.githubusercontent.com/redradishtech/isso/master/isso/js/embed.min.js) from jefft linked from [this isso bug](https://github.com/posativ/isso/issues/656). Now comments are back, to not be used like before ;)

[^1]: `pip install git+https://github.com/posativ/isso.git@master#egg=isso`
