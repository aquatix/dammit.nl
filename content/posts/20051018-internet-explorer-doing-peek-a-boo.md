Title: Internet Explorer doing Peek-a-boo
Date: 2005-10-18 21:16:33
Slug: 20051018-internet-explorer-doing-peek-a-boo
Location: Home
Authors: Michiel Scholten

<p>While I was redesigning the Dutch <a href="http://www.mapleleaves.nl/">Mapleleaves Basketball club site</a> [at this moment still the old, very ugly Fr***p*** generated version with a java menu], I noticed a very strange bug: in <acronym title="Internet Exploder">IE</acronym>6, text would vanish [or not appear at all], and [re]appear when hovering over a button, selecting the invisible text or scrolling. I was really baffled, but it turned out a well-known bug in our good friend <acronym title="Internet Exploder">IE</acronym>: the <a href="http://www.positioniseverything.net/explorer/peekaboo.html">IE6 Peekaboo Bug</a>. I fixed it by adding "line-hight: 1.2;" to the stylesheet for the block containing the content [and so, containing the floating sub navigation].</p>

<p><a href="/projects/mapleleaves/">Check the current beta version</a> for the real experience.</p>

<p>Sigh...</p>