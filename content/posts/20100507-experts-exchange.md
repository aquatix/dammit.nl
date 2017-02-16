Title: Experts Exchange
Date: 2010-05-07 14:25:23
Slug: 20100507-experts-exchange
Location: Work
Authors: Michiel Scholten

<p><a href="http://stackoverflow.com/">Stack Overflow</a> is a lot nicer as a source for good technical advice, but Experts Exchange still has quite some answers too; might come in handy for a second opinion/solution on which you can base your own. expert-sexchange is much less annoying with this bit of CSS added to Firefox's userContent.css file:</p>

<pre>
@-moz-document domain(experts-exchange.com) {
    div.qStats {display: none !important;}
    div.blurredAnswer {display: none !important;}
    div.allZonesMain {display: none !important;}
}
</pre>

<p>[<a href="http://arstechnica.com/web/news/2010/05/googles-search-results-get-a-much-needed-makeover.ars?comments=1#comment-20378318">source</a>]</p>