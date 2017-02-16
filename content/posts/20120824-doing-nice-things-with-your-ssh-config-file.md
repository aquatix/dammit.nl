Title: Doing nice things with your SSH config file
Date: 2012-08-24 15:43:24
Slug: 20120824-doing-nice-things-with-your-ssh-config-file
Location: Home
Authors: Michiel Scholten

<p>If you are running a unix-like machine, like a Linux workstation, or BSD or Apple Mac, you might be acquainted with the ~/.ssh directory. SSH stores known hosts in their, as well as your public and private SSH keys and more important stuff. 

<p>The contents of a ~/.ssh/config look something like:</p>
<pre>
Host homeserv
	HostName home.mydomain.net
	Port 22
	User michiel

	# Routers, so I config them from on the road
	LocalForward localhost:8001	192.168.1.1:80
	LocalForward localhost:8002	192.168.1.2:80

	LocalForward localhost:

	# SickBeard
	LocalForward localhost:8081	localhost:8081

Host dev
	HostName dev.corp.net
	Port 22
	User mscholten
</pre>

<p>Of course you can add as many 'Host' configs as you like.</p>

<p>You can now use these configs from your terminal: <code>ssh dev</code> instead of <code>ssh mscholten@dev.corp.net</code> (or those long lines with port forwards you tended to create an alias for in ~/.bash_aliases).</p>

<p>Bonus: if you are running gnome-shell on your machine, you can install the <a href="https://extensions.gnome.org/extension/73/ssh-search-provider/">SSH search provider</a> extension, so you can directly launch a terminal with all settings in place from the overview page. Productivity boon in my not-so-humble opinion ;)</p>

<p>For more information, see <a href="http://magazine.redhat.com/2007/11/27/advanced-ssh-configuration-and-tunneling-we-dont-need-no-stinking-vpn-software/">Advanced SSH configuration and tunneling: We don't need no stinking VPN software</a>.</p>

<p>Also, if you want do some VPN-like stuff, you really need to check out <a href="http://rogueleaderr.tumblr.com/post/29855576743/never-again-be-thwarted-by-restrictive-guest-wifi">Never again be thwarted by restrictive "guest" wifi (e.g. on buses or airplanes)</a>. The <a href="https://github.com/apenwarr/sshuttle/">sshuttle proxy</a> they use is really nifty.</p>