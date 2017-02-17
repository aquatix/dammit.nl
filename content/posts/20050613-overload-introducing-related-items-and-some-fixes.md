Title: overload: introducing related items and some fixes
Date: 2005-06-13 12:54:18
Slug: 20050613-overload-introducing-related-items-and-some-fixes
Location: Home
Authors: Michiel Scholten
Tags: olddammit

<p>OK, just put a new snapshot of this interesting project online. You may wonder why I call my own project "interesting", but it has earned this title because of the latest addition to it: related items. I've introduced a simple algorithm that looks for other items that have links in common and put them as links beneath the posting. This may bring up relations you didn't see yourself yet. Early iterations of this functionality where painfully slow, resulting in pageload times of over 5 minutes [sic]. And that by a simple <acronym title="Structured Query Language">SQL</acronym> query [well, not _that_ simple, but then again, only merging 6 tables or something]. However, I tweaked quite a bit and now it's very usable!</p>

<p>Ah, and I updated the icons :)</p>

<p>The <acronym title="eXtensible User-interface Language">XUL</acronym> version now works again [login form didn't work, but you already could switch to the 'Rich client' when logged in to the html version]. This version doesn't have the related items functionality yet, but I'm planning on resynching both UI's in functionality [html version still doesn't have a functional Search and 'Show read items' etc mode].</p>

<p>So, please take a look and report problems :) Anybody subscribed for his own account already? ;)</p>