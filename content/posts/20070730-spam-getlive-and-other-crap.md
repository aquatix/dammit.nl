Title: Spam, GetLive and other crap
Date: 2007-07-30 12:31:35
Modified: 2007-07-30 13:27:04
Slug: 20070730-spam-getlive-and-other-crap
Location: Home
Authors: Michiel Scholten
Tags: rant

<p>I just reached the 15000 spam messages for this year in my spam folder. That's about 15007/211 = 71.12 messages a day. Fun, fun. Thanks the Light for SpamAssassin.</p>

<p>In other news, I just installed <a href="http://sourceforge.net/projects/getlive">the GetLive script</a> in replacement for the trusty old <a href="http://sourceforge.net/projects/gotmail/">gotmail script</a> to retrieve messages from my ancient hotmail address, and an address from a basketball club I maintain the site for. It works quite well, but you have to take care when you do the <code>Processor=cat - >> your_mailbox</code> trick, as those nice HTML emails tend *not* to have a linefeed after them, which results in the first line of next messages being put at the same line, resulting in you not seeing that message and b0rkage in general. I fixed this by doing <code>Processor=echo -e "\n\n" ; cat - >> your_mailbox</code> instead, so I get a config like this:</p>

<pre>
UserName=my_ancient_email
Password=123:)
Mode=live
Domain=hotmail.com
FetchOnlyUnread=No
Folder=Inbox
Folder=Another folder
MarkRead=Yes
Downloaded=/home/myuser/.config/getlive/my_ancient_email.downloaded
Processor=echo -e "\n\n" ; /bin/cat - >> /home/myuser/mail/hotmail_inbox
</pre>

<p>... which I saved in ~/.config/getlive/myuser.conf to prevent my homedir from cluttering up. The file mentioned under Downloaded contains the ID's of the messages already downloaded, which nicely prevents it from downloading email over and over again.</p>

<p>I also have been setting up the <a href="http://funambol.com">Funambol SyncML server</a> to sync my SonyEricsson M600i symbian smartphone with *something* [preferably Evolution with <a href="http://www.estamos.de/projects/SyncML/">SyncEvolution</a>]. However, it has some problems with the Symbian [EPOC] styled fields regarding recurrent items and kinds of entries, like Anniversaries and Allday. Funambol seems to have filters for those, but they don't quite work yet, resulting in anniveraries not recurring in Evolution and not being an all-day event, for example. Oh well, more research to do next to my Bachelor thesis and such :)</p>

<div class="edit">edited at 2007-07-30 13:05</div>
<p>Heh, I found a nice piece of info on that ancient account: "Registered since: 25 November 1998" which I think isn't entirely correct, as I remember having registered it before Hotmail was bought by microsoft :)</p>

<div class="edit">edited at 2007-07-30 13:25</div>
<p>A note on the GetLive.pl Processor: if you want it to go through your mail subsystem [for scanning on spam, or because you have a nice .forward with all kinds of exim filters like I have], use <code>Processor=/usr/sbin/sendmail -i myuser</code></p>