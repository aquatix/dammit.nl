Title: Firefox security goodness
Date: 2004-08-18 15:19:46
Slug: 20040818-firefox-security-goodness
Location: Work
Authors: Michiel Scholten

<p>There are now a couple of security spoofs out there for <a href="http://www.mozilla.org/products/firefox/">Mozilla Firefox</a>. Unlike IE there is an easy way to catch them that is not often mentioned.</p>
<p>Simply type in about:config into the address bar, then search for and change these settings to <em>true</em>:</p>
<p><em>recommended:</em></p>
<pre>
dom.disable_window_open_feature.location
dom.disable_window_open_feature.status
dom.disable_window_open_feature.titlebar
dom.disable_window_status_change
</pre>
<p><em>optional:</em></p>
<pre>
dom.disable_window_move_resize
  [good against user-initiated popups]
dom.disable_window_open_feature.close
dom.disable_window_open_feature.directories
dom.disable_window_open_feature.menubar
dom.disable_window_open_feature.minimizable
dom.disable_window_open_feature.personalbar
dom.disable_window_open_feature.resizable
  [handy against those tiny non-resizable popups too]
dom.disable_window_open_feature.scrollbars
dom.disable_window_open_feature.toolbar
</pre>

<p>Hope anybody thinks this useful. Of course, check out the "Web Features" settings dialog out first.</p>