Title: Feeds, channels, labels, tags...
Date: 2005-08-01 23:02:16
Modified: 2005-08-01 23:19:42
Slug: 20050801-feeds-channels-labels-tags
Location: Home
Authors: Michiel Scholten
Tags: olddammit

<p>OK, so I fixed some cross-browser issues of <a href="/page/html/overload/">overload feedreader</a>, put a <a href="https://aquariusoft.org/overload/">new version of it</a> online and was wondering about naming of several things now. As it's a feedreader, it reads RSS, Atom feeds. Those are not only used for weblogs, so I skipped mentioning "Blogs" altogether, unlike several other readers. However, the world "channel" seems nice to me too, as you're just tuning in to that news-channel, be it Slashdot, BBC, your local newspaper, or your favorite weblog.</p>
<p>So, what do you think about changing all references to "feeds" to "channels"?</p>

<p>Beside that, I want to implement tagging. Tagging is hot, but that's because it is handy. You can categorize pieces of information by putting a tag -- or label -- on it. And not one, but as many as you want, so you're not restricted to some weird rigid category tree-structure or something. And I like that. The word "tag" is quite common, but you can also use "label". I kinda prefer "tag" tho'.</p>

<p>Thoughts?</p>

<div class="edit">edited at 2005-08-01 23:16</div>
<p>Maybe nice to tell the issues I fixed where about the mark read/unread and flag/unflag buttons not working in other browsers than Firefox, because of the various ways XMLHttpRequest is executed. Beside that, I fixed the indention of the channel listing in other browsers than Firefox [indention was way too large]. Now only to propagate this functionality to the <a href="https://aquariusoft.org/overload/xul/">Rich client version</a> and implement tagging.</p>