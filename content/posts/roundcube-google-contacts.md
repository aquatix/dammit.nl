Title: Roundcube webmail and Google contacts
Started: 2014-10-25, 2017-04-26 15:48:00
Date: 2020-01-25 13:48:00
Slug: roundcube-google-contacts
Location: Home
Authors: Michiel Scholten
Category: howto
Tags: linux, hosting, howto
Status: published

Draft digging time! Something I've had in my drafts since the 25th of October, 2014, apparently:

Roundcube is a decent self-hosted webmail solution, which benefits from integrating Google Contacts so you do not have to duplicate your address books (assuming you use Google for yours).

Luckily someone wrote a plugin:

- [Google Addressbook for Roundcube](https://github.com/stwa/google-addressbook)
- [Plugin in Roundcube's plugin library](http://plugins.roundcube.net/packages/stwa/google-addressbook)

The [howto for installing plugins in Roundcube](http://plugins.roundcube.net) tells you how to install those plugin bundles. It works with [Composer](https://getcomposer.org/download/), which uses a really bad anti-pattern to install: `curl -sS https://getcomposer.org/installer | php`, so piping code straight from the internet through an interpreter. This is _NOT_ something you want to do, really.

See the plugin page for further install instructions.

Now enable a repeated sync, so open the relevant crontab and enter a line like this:

```
0 */8 * * * /srv/www/example.com/roundcube/plugins/google_addressbook/sync-cli.sh
```

The above example downloads your Google Contacts to the Roundcube address book every 8 hours.
