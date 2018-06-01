Title: diskspacealarm.py
Started: 2018-06-01 15:51:12
Date: 2018-06-01 15:51:12
Slug: diskspacealarm
Location: Home
Authors: Michiel Scholten
Category: projects
Tags: dev, notifications, python, tech
Image: 
Status: draft

Because it's Friday, I was bitten by a filled-up volume on my VPS again, because [Prometheus](https://prometheus.io/) somehow is randomly crashing my VPS, and because I like thinkering, I wrote a little notification script.

Yes, it checks for available disk space on your nodes, with configuration per hostname (it's all contained in the source file).

Here it is:

    import http.client, urllib
    import os
    import socket
    import sys


    HOSTNAME = socket.getfqdn()

    APP_TOKEN = '<your_pushover_app_token>'
    USER_KEY = '<your_pushover_userkey>'

    FILESYSTEMS = {
        'host001.example.com': [
            ('/', 1),
            ('/var/local', 5),
            ('/home', 5),
        ],
        'host002': [
            ('/', 5),
            ('/stuff', 100),
        ],
    }

    def needs_notifying(size_trigger, size_available):
        """Checks whether we need to send a notification

        Args:
        size_trigger: minimum amount of free space in GB
        size_available: currently available free space in bytes
        """
        return size_available <= (size_trigger * 1024*1024*1024)


    def send_message(message):
        conn = http.client.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
          urllib.parse.urlencode({
            "token": APP_TOKEN,
            "user": USER_KEY,
            "message": message,
          }), { "Content-type": "application/x-www-form-urlencoded" })
        conn.getresponse()


    def send_lowdisk_message(messages):
        message = '[{}] Low disk space on the following volumes:\n{}'.format(HOSTNAME, '\n'.join(messages))
        send_message(message)


    try:
        filesystems = FILESYSTEMS[HOSTNAME]
    except KeyError:
        send_message('[spacealarm] No filesystem configuration found for {}'.format(HOSTNAME))
        sys.exit(1)

    messages = []

    for filesystem in filesystems:
        statvfs = os.statvfs(filesystem[0])

        #statvfs.f_frsize * statvfs.f_blocks     # Size of filesystem in bytes
        #statvfs.f_frsize * statvfs.f_bfree      # Actual number of free bytes
        #statvfs.f_frsize * statvfs.f_bavail     # Number of free bytes that ordinary users
                                                 # are allowed to use (excl. reserved space)

        if needs_notifying(filesystem[1], statvfs.f_frsize * statvfs.f_bavail):
            messages.append('{}: {:.1f}MB free'.format(filesystem[0], statvfs.f_frsize * statvfs.f_bavail / 1024/1024))

    if messages:
        send_lowdisk_message(messages)
