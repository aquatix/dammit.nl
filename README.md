dammit.nl
---------

[Pelican](https://blog.getpelican.com/) based source of [the dammIT weblog](https://dammit.nl/). This is the successor
to the [PHP based original](https://github.com/aquatix/dammit).


## Installation

*Create a virtualenv*, activate it and install the build requirements:

    pip install -r requirements.txt

or better yet, use uv which generated this `requirements.txt` file from `requirements.in`:

    # Install globally from https://github.com/astral-sh/uv/
    curl -LsSf https://astral.sh/uv/install.sh | sh

    # Or install in the virtualenv
    pip install --upgrade uv

    uv pip sync requirements.txt


## Building

Go to root of repository, make sure the correct virtualenv is used and do:

    make publish

This generates an `output` directory, which should be (copied/rsync'ed to and) served by a web server.


## Writing and/or developing

    make devserver

    # Or, with a custom port, 8888 in this case:
    make devserver -p 8888
