Title: Debugging for fun and profit
Date: 2008-01-24 15:52:36
Slug: 20080124-debugging-for-fun-and-profit
Location: Home
Authors: Michiel Scholten

<p>Now and then I run into a crashed <a href="http://irssi.org/">irssi</a>. It crashes when the lag becomes way high [stupid adsl modem], or when doing an /upgrade or /quit. I narrowed it down to a Perl script I have that adds !command-style commands to irssi's list of commands for controlling a bot of mine.</p>

<p>So, I tried to debug it. I installed irssi on my laptop [normally, I have it 24/7 online in a screen session on my server], copied the config from my server and started to thinker around. As it segfaults, I would be able to get some info with <a href="http://sourceware.org/gdb/" title="GDB: The GNU Project Debugger">gdb</a>, so I tried to run irssi in gdb [<code>gdb irssi</code>]. That didn't work, as it didn't show an irssi window. So, I set <code>ulimit -c unlimited</code> in the bash terminal to be able to get a core dump, started irssi, logged into the channel, loaded the perl plugin and /quit. It neatly coredumped. Then I was able to do a <code>gdb irssi ./core</code>, which provided me some info. A <code>bt</code> didn't give me any useful info though. Also, the info gdb provided wasn't that useful because the binary I was running here [installed from the Debian repository] is stripped from debugging symbols... [And no irssi-dbg is provided]. Oh well, let's hope they fixed things in svn already [found a reference to other scripts segfaulting irssi similarly; an issue that seemed to be fixed for 0.8.13 in svn].</p>

<p>Someone have an idea what could cause the segfault? I think it has to do with the script adding commands, but how and why...</p>