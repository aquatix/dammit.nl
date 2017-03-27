dammit.nl
---------

[Pelican](https://blog.getpelican.com/) based source of [the dammIT weblog](https://dammit.nl/). This is the successor
to the [PHP based original](https://github.com/aquatix/dammit).


## Installation

Create a virtualenv, activate it and install the build requirements:

    pip install -r requirements.txt


## Building

Go to root of repository, make sure the correct virtualenv is used and do:

    make publish

This generates an `output` directory, which should be (copied and) served by a web server.
