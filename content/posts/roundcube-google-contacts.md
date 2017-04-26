Title: Roundcube webmail and Google contacts
Started: 2014-10-25
Date: 2017-04-26 15:48:00
Slug: roundcube-google-contacts
Location: Home
Authors: Michiel Scholten
Category: howto
Tags: linux, howto
Status: draft

[Google Addressbook for Roundcube](https://github.com/stwa/google-addressbook)
[Plugin in Roundcube's plugin library](http://plugins.roundcube.net/packages/stwa/google-addressbook)

The [howto for installing plugins in Roundcube](http://plugins.roundcube.net) tells you how to install those plugin bundles. It works with [Composer](https://getcomposer.org/download/), which uses a really bad anti-pattern to install (`curl -sS https://getcomposer.org/installer | php`, so piping code straight from the internet through an interpreter. This is _NOT_ something you want to do, really).

