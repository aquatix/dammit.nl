Title: isso commenting system in a subdirectory on nginx
Started: 2018-12-17 13:58:11
Date: 2018-12-17 13:58:11
Slug: isso-subdirectory-nginx
Location: Work
Authors: Michiel Scholten
Category: howto
Tags: dev, howto, linux, python, web

I very recently moved this weblog to a new host, and in the process finally changed from Apache running mod_wsgi to nginx with uWSGI and supervisor (well, at least for the Python based web apps, as dammIT is a flat site). I'm using [isso](https://posativ.org/isso/) as commenting system, which runs as an application in uWSGI, using a socket, and is managed by uWSGI. This is all fine, dandy, and documented by their documentation, but running it in a subdirectory (in the URL) is not. After some hair pulling and numerous web searches, I arrived at this working configuration:

    location /comments {
        include uwsgi_params;
        uwsgi_param HTTP_X_SCRIPT_NAME /comments;
        uwsgi_pass unix:/var/local/socket/isso.sock;
    }

Mind the line with `HTTP_X_SCRIPT_NAME` here, as that's what tells isso it runs under that subdirectory instead of in the webroot.

For completeness, the uWSGI configuration I use is as follows:

    [uwsgi]
    # use Python 3.7 plugin; change to python36 or similar, depending on the Python version in your venv
    plugins = python37
    project = isso
    base = /srv/www/isso

    # the virtualenv (full path), in which isso is installed through `pip install isso`
    home = %(base)/venv
    # wsgi file
    module = isso.run

    env = ISSO_SETTINGS=/srv/www/isso/dammit.nl.ini
    #spooler = %d/mail

    master = true
    # maximum number of worker processes
    processes = 4

    socket = /var/local/socket/%(project).sock
    chmod-socket = 666
    # clear environment on exit
    vacuum = true

    # make sure that uWSGI doesn't hard kill the app on termination
    die-on-term = true
