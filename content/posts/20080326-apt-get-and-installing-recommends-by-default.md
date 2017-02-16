Title: apt-get and installing recommends by default
Date: 2008-03-26 11:02:57
Slug: 20080326-apt-get-and-installing-recommends-by-default
Location: Work
Authors: Michiel Scholten

<p>Now for a geeky post.</p>

<p>Since a while, apt installs recommended packages by default too alongside the dependencies, like aptitude does. However, you might pull in quite a lot of packages you don't really need that way. Here's how to stop it:</p>

<pre>apt-get install -o APT::Install-Recommends=false [packagename you want to install]</pre>

<p>Or, better even, add a file to your <code>/etc/apt/apt.conf.d</code> directory. I named it <code>06norecommends</code> :</p>

<pre>
APT
{
	Install-Recommends "false";
	Install-Suggests "false";
};
</pre>