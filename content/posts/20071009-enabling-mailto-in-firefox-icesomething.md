Title: Enabling mailto: in Firefox/Icesomething
Date: 2007-10-09 17:29:24
Slug: 20071009-enabling-mailto-in-firefox-icesomething
Location: Home
Authors: Michiel Scholten

<p>As simple as adding a new setting in your about:config :-</p>

<ol>
<li>Open Firefox, type "about:config" (no quotes) in the address window, and click enter</li>
<li>Right click on the window and choose 'New', then 'String' from the pop-up menu that appears</li>
<li>In the first pop-up box, enter: "network.protocol-handler.app.mailto" (no quotes, and it might just be easier to cut 'n paste this into the box)</li>
<li>In the next pop-up box enter the path to Thunderbird, or another email client (e.g. "/usr/bin/mozilla-thunderbird" - I entered "/usr/bin/claws-mail" without the quotes, of course)</li>
</ol>

<p>[<a href="http://www.cinlug.org/node/325">source</a>]</p>