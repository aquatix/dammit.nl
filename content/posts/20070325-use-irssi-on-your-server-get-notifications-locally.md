Title: Use irssi on your server, get notifications locally
Date: 2007-03-25 15:17:46
Slug: 20070325-use-irssi-on-your-server-get-notifications-locally
Location: Home
Authors: Michiel Scholten
Tags: rant

<p>I've been using <a href="http://www.irssi.org/">irssi</a> for quite a while as my primary IRC client, running in a screen session on my server so I'm always online. However, when someone says my nick, I only notice when looking at the terminal it's running in, and it shouldn't have scrolled out of sight yet [when it's in the current channel]. So, a way of notifying me would be cool. Today however, I ran across <a href="http://www.pthree.org/2007/03/21/irssi-gui-notify/">Irssi GUI Notify</a>, which was exactly what I was looking for. It uses <a href="http://thorstenl.blogspot.com/2007/01/thls-irssi-notification-script.html">a perl script</a> [<a href="http://aquariusoft.org/~mbscholt/files/fnotify">download from my server</a>, and rename to fnotify.pl] in irssi to add lines containing your nick to the file 'fnotify' in your ~/.irssi/ dir. This is then read by a bash script you run locally, which uses a notification daemon to show popup notifications [see the linked pages for screenshots]. The one that works best for me [there are several posted on those weblogs], is this version, taken from <a href="http://blog.nixternal.com/2007.03.22/notify-works-in-kubuntu/">this weblog</a>:</p>

<pre>
#!/bin/bash
ssh user@host ": > .irssi/fnotify ; tail -f .irssi/fnotify " |
sed -u 's/[<@&amp;]//g' | while read heading message;
do /usr/bin/notify-send -u critical -i /usr/share/icons/Tango-xfce/scalable/apps/terminal.svg -t 30000 -- "${heading}" "${message}";
done
</pre>

<p>Just save it to a convenient place and start it automatically; it'll keep running and monitoring the notifications file. You may want to adjust the 30000 to a timing you like; it's the amount of milliseconds the popup will stay visible. Also, you may want to change the icon path from that terminal icon to something else. You'll need this package to get the notifications working:</p>

<pre>
sudo apt-get install libnotify-bin
</pre>

<p>and of course a notification-daemon. By default, Irssi only highlights the nick that mentioned your nick if your nick is first on the line. Otherwise, it is not the case. This can be fixed highlighting the nick that mentions your nick anywhere in the text. Do the following in Irssi:</p>
<pre>/hilight -nick (your_nick)</pre>