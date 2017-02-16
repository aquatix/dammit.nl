Title: .plan
Authors: Michiel Scholten
Date: 2006-04-28
Modified: 2014-04-01

<h1>.plan</h1>

<h2>Todo</h2>
<ul>
	<li>Check for things like non-encoded &gt; and &lt; signs in weblog postings and blogmark entries</li>
	<li><a href="http://www.w3.org/QA/Tips/use-links">use links in the pages</a></li>
</ul>
<ul>
	<li>Finish the edit functionality :) Shouldn't be that difficult ;)</li>
	<li>Implement log viewing utility</li>
</ul>

<h2>Done</h2>
<ul>
	<li>[2006 April]
		<ul>
			<li>Added "Close comments for this posting" support. Thanks, spammers...</li>
			<li>Added "Blogmarks of last 7 days ['this week'] to posting", and support for doing this automatically. Maybe someone will read my blogmarks now ;)</li>
			<li>Added support for guessing your current location when adding a new rant or blogmark; IP's are configurable through the config file</li>
			<li>Did some renaming in the database: simplog_ as prefix for the table names, lowercase for the names of tables and their columns</li>
			<li>As can be derived of the previous point, the software behind dammIT now officially is called "simplog", after "simple [web]log"</li>
			<li>General code cleanup/optimalizations</li>
			<li>Cleanups in the CSS, and some tweaks of the layout [mostly for the rants; are easier on the eye now]</li>
		</ul>
	</li>
	<li>[2005-10-02]
		<ul>
			<li>Expanded the right navigation bar, so it's extra width would cause the "distracted by" links to take up less vertical space</li>
			<li>Let the "distracted by" links link directly to the sites again, with an added "[more]" linking to the blogmark with my comment</li>
			<li>Changed the listing-arrow graphic to a dotted one</li>
			<li>Added a stylesheet rule to add an "external link" graphic to links going to pages outside this weblog. Causes the stylesheet to not validate any longer, but is quite cool. Ah yes, doesn't work with <acronym title="Internet Exploder">IE</acronym> of course...</li>
		</ul>
	</li>
	<li>[2005-09-22]
		<ul>
			<li>Implemented navigating from posting to posting in detailed view [e.g., the view where you see one posting and its comments]</li>
			<li>Moved "distracted by" links block to the top of the right navigation bar, so people will notice it ;)</li>
			<li>Search field remembers the text you where looking for now</li>
		</ul>
	</li>
	<li>[2005-09-21] Updated link to Roosje's weblog</li>
	<li>[2005-09-07] Added an Autumn logo [stones background, picture taken on vacation in Belgium this year]</li>
	<li>[2005-06-19] Added a 'Thanks Dave' icon linking to <a href="http://www.scripting.com/">Scripting News</a>, because of Dave Winers nice applications and efforts to push those technologies</li>
	<li>[2005-02-01]
		<ul>
			<li>Fixed base href, which broke IE's CSS loading</li>
			<li>Fixed automatic e-mails [broken uri's]</li>
			<li>Fixed comment preview [didn't show line breaks</li>
		</ul>
	</li>
	<li>[2005-01-28]
		<ul>
			<li>Relicensed dammIT under the <a href="http://creativecommons.org/">Creative Commons</a> <a href="http://creativecommons.org/licenses/by-nc-sa/2.0/">Attribution-NonCommercial-ShareAlike 2.0</a> license [former one was the 1.0 version of the same license]</li>
			<li>$site structure variable changed to wider used $skel variable. I use $skel in almost every other project, so why not here</li>
		</ul>
	</li>
	<li>[2005-01-11]
		<ul>
			<li>Implemented search functionality for weblog postings and webmarks</li>
			<li>Some minor bugfixes [non-initialized vars]</li>
			<li>Moved <acronym title="Internet Exploder">IE</acronym> warning markup to stylesheet, where it belongs</li>
			<li>A whole lot of code clean up</li>
			<li>Added some content to the <a href="index.php?page=about">about page</a>, shuffled some paragraphs on it and updated this .plan</li>
			<li>Removed the bitrotted error page, which isn't needed anyway</li>
		</ul>
	</li>
	<li>[2005-01-08] Implemented Preview functionality for comments</li>
	<li>[2004-12-14]
		<ul>
			<li>Fixed the list-arrow-bullet-thingee and made it a bit darker</li>
			<li>Some internal fixes [finally a reliable comment-permalink]</li>
		</ul>
	</li>
	<li>[2004-11/12]
		<ul>
			<li>Lots of layout changes [quite frequently caused by <acronym title="Internet Exploder">IE</acronym>'s inability of displaying <acronym title="Cascading Style Sheets">CSS</acronym> right</li>
			<li>Moved a lot of navigation stuff [links to external pages] and <em>distracted by</em> to a new bar at the right</li>
			<li>Rewrote the <a href="blogmarks.php">blogmarks</a> code</li>
		</ul>
	</li>
	<li>[2004-10-24]
		<ul>
			<li>Fixed <acronym title="Internet Explorer">IE</acronym> related bugs: Archive was borked [dates wheren't shown properly] and main navigation buttons didn't show as expected. <acronym title="Internet Explorer">IE</acronym> should teach some <acronym title="Cascading Style Sheets">CSS</acronym>...</li>
			<li>Added "Edit posting" and "Disable comment" functionality [with dynamic session checking: no cookies when no need to!]</li>
		</ul>
	</li>
	<li>[2004-10-22] Added option to receive a notification by e-mail when someone comments to the posting you commented to. Fixed some e-mail related bugs while at it</li>
	<li>[2004-10-21]
		<ul>
			<li>Modified a lot of the GUI: changed main navigation links to button-like links, finished adding accesskeys to them [try Alt+key-between-square-brackets].</li>
			<li>Made the menu user configurable [in the config file]</li>
			<li>Made some other things user configurable too</li>
			<li>Cleaned up code</li>
		</ul>
	</li>
	<li>[2004-10-16] Changed background color of the main body to white. Better contrast with the text</li>
	<li>[2004-08-29]
		<ul>
			<li>Added linefeeds to the comments in the feed with comments</li>
			<li>Added comments RSS tag to feeds</li>
			<li>Added location to RSS feeds</li>
			<li>Cleaned up some things</li>
		</ul>
	</li>
	<li>[2004-06-28]
		<ul>
			<li>Implemented the <a href="index.php?page=archive">Archive</a></li>
			<li>Improved the page navigation [well, made it smaller, and somewhat better looking in it's smallness]</li>
			<li>Added a <a href="blog_comments.rdf">third feed</a>, now with the blogpostings and comments from readers. Thought it may be fun to have</li>
		</ul>
	</li>
	<li>[2004-06-22]
		<ul>
			<li>Created a navigation for the blogmarks, like I already had for old rant entries</li>
			<li>Let the nav for old rants start at the second page [no need for getting the current page again]</li>
			<li>When clicked on Blogmark link, you get that blogmark on it's own; finally a working permalink for blogmarks :)</li>
			<li>Made the blogmark navigation default; e.g., no "old marks" link or something, but navigation links by default</li>
		</ul>
	</li>
	<li>[2004-06-21] New summer, new logo :)</li>
	<li>[2004-05-23/24]
		<ul>
			<li>Fixed some postings with &amp;'s in urls, rendering the xhtml invalid</li>
			<li>Added some blogs to the nav, removed the one from the other Michiel [didn't know him anyway]</li>
			<li>Added link to Technorati, some site that crawls blogs to map interrelations [inbound and outbound links]</li>
			<li>Added link to <a href="http://chongq.blogspot.com/">spam chongqing</a>, because I don't like spammers :)</li>
			<li>Tweaked a little</li>
		</ul>
	</li>
	<li>[2004-04-18]
		<ul>
			<li>Cleaned up the comments layout. Let it add breaks at end of lines too, so basic formatting is possible.</li>
			<li>Cleaned up the layout of this .plan</li>
			<li>Made a site variable with all config items in it. Changed lots of functions and function calls to use this simpler way of config.</li>
			<li>Added "Comment is added" email support</li>
			<li>Reversed the order comments where sorted at: now it's chronological and that's far more logical ;)</li>
		</ul>
	</li>
	<li>[2004-04-16] Fixed a typo in an html tag</li>
	<li>[2004-04-15]
		<ul>
			<li>Implemented comment functionality [check for html and escape it]</li>
			<li>Implemented blogmarks feed. Made the style a lot cleaner by some simple modifications.</li>
		</ul>
	</li>
	<li>[2004-03-10/11]
		<ul>
			<li>blogmarks [including pics; 2 different types of blogmarks, one for urls, one for images] -- just normal blogmarks [hyperlinks to pages or images]</li>
			<li>cleaned up the <a href="about">About</a>/<a href="faq.php">faq</a> pages</li>
		</ul>
	</li>
	<li>[2004-03-06] Renamed permalink to link. Cleaned up some inc_html stuff</li>
	<li>[2004-03-04] Upgraded [?] the RSS feed to version 2.0, and moved the body of the text from the description to the content node</li>
	<li>[2004-02-27] Cleaned up some code, added some entities to the RSS feed [btw, renamed it to blog.rdf, instead of blog.rss]</li>
	<li>[2004-02-26] Putted the revamped rantbox online
		<ul>
			<li>And there it is: <a href="blog.rdf">a nice RSS feed for you reading pleasure</a> :)</li>
			<li>Modded the xhtml1.0 icon to a xhtml1.1 icon</li>
			<li>Make the Firefox icon transparant [really ugly white background at that crappy <acronym title="Internet Explorer">IE</acronym> thing]. Turns out to be hopeless... Used another banner instead. Too bad :(</li>
			<li>[2004-02-26] Removed html functions from inc_methods.php, and included the inc_html.php. Splitted giveRants into getRants [returns array] and buildRants [html]. Fixed typo in main.css [it validates again :)]</li>
		</ul>
	</li>
	<li>[2004-02-25] Proceeded with extending the nav. Renamed Archive to Browse and created the beginnings of a real Archive function :) . Extended the navigation for Browse. Started on a RSS feed generator function. Moved about text from home page to <a href="about.php">about page</a></li>
	<li>[2004-02-24] Added RSS, Valid xhtml, Valid CSS and Mozilla Firefox icons to the nav</li>
	<li>[January/February] Some small enhancements</li>
	<li>[2004-01-14] Finally found a decent name for this blog. Behold, here is "dammIT" :)</li>
	<li>[2004-01-05] validated content with the <a href="http://validator.w3.org">W3 validator</a>. It should be valid xhtml 1.1 after all ;)</li>
	<li>[2003-12-25] location [home/work/train/bed, whatever]</li>
	<li>[2003-12-25] archive</li>
	<li>[2003-12-27] cleaned up lots of code and tweaked the CSS a little more. No, not tweaked; completely cleaned it up, validated and beautified the source :)</li>
	<li>[2003-12-27] Extended the <a href="faq.php">faq</a></li>
</ul>
