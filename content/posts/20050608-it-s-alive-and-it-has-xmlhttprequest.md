Title: It's alive and it has XMLHttpRequest :)
Date: 2005-06-08 17:03:55
Slug: 20050608-it-s-alive-and-it-has-xmlhttprequest
Location: Work
Authors: Michiel Scholten

<p>I've been working on <a href="https://aquariusoft.org/overload/">the overload RSS reader</a> a bit the last few days, and put a brandnew snapshot online. It's a great deal faster [calculating of the number of unread items was a tad slow, taking 6 seconds for my 69 feeds and 17000 items total and 5000 unread, now 0.09 seconds]. And... it has <a href="http://jibbering.com/2002/4/httprequest.html">XMLHttpRequest</a>, which some of you may know as <a href="http://en.wikipedia.org/wiki/AJAX"><acronym title="Asynchronous JavaScript and XML">AJAX</acronym></a>.</p>

<p>Now, what's the deal about that? And why do you introduce javascript when you don't like it? Well, it's about usability. Earlier versions of the html pages had to reload the whole page when saving an item, or marking it 'read'. Now you click the link [which calls a small javascript function], and the "set saved" or "set read" instruction is sent to the server in the background, while replacing the icon for feedback it went OK.</p>

<p>A very nice example of this technique is <a href="http://gmail.com/">GMail</a>, Google's mail service. All actions are [almost] instantly, because they happen in the background, and information is preloaded [hence the "Loading..." message when visiting]. I don't want to overdo it that way, but introducing it for some buttons happened to be working out very well.</p>

<p>Please take a look and give me some feedback! And yeah, I know the icons suck a little. Does anybody have ideas for better ones?</p>