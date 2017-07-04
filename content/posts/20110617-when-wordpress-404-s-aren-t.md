Title: When Wordpress 404's aren't
Date: 2011-06-17 15:23:30
Slug: 20110617-when-wordpress-404-s-aren-t
Location: Work
Authors: Michiel Scholten
Tags: rant, work

<p>Today I helped a colleague troubleshooting a form in one of our Wordpress websites that returned a "404 Page not found"-error when it was submitted to itself. Of course, this was rather puzzling as the address was exactly the same as the page where you just filled the form on. After a morning of digging into rewriting rules, Wordpress templating, disabling the numerous plugins and more debugging - partly helped by another colleague, the guy spoke an irritated "I really don't get this crap" (paraphrased ;) ).</p>

<p>I asked what was going on and together we dug into the code. After verifying the url was really correct and digging a bit through xdebug logs, I got the idea that the uri-routing was a red herring. After a good look at the form in question, we changed some of its field names and - oh miracle - things worked. It turned out that fields with names like "name" have some sort of reserved use and screw with the hidden Wordpress magic (or maybe some of the plugins in question).</p>

<p>I seem to be employee of the day now ^_^</p>
