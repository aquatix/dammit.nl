Title: Minimal xorg.conf with composition
Date: 2007-02-16 20:36:39
Slug: 20070216-minimal-xorg-conf-with-composition
Location: Home
Authors: Michiel Scholten
Tags: rant

<p>I really like Xfce 4.4's compositor [giving me nice shadows, transparent windows et al], and I wanted to clean up, so I requested <a href="http://aquariusoft.org/~mbscholt/files/xorg.conf.mephisto.20070216">Mephisto's really minimal xorg.conf</a> [which he uses with X.org 7.2 and an nvidia 9746 driver]. I added some modules that wheren't automatically loaded by my X.org 7.1, and some stuff to get composition. This is the result:</p>

<pre>
Section "ServerLayout"
	Identifier	"Default"
	Screen		"Screen" 0 0
	Option		"AllowDeactivateGrabs" "1"
	Option		"AllowClosedownGrabs" "1"
EndSection
Section "Device"
	Identifier	"Nvidia"
	Driver		"nvidia"
	Option		"NoLogo" "1"
	Option		"DynamicTwinView" "0"
	Option		"AddARGBGLXVisuals" "1"
	# Composite stuff
	Option		"RenderAccel" "true"
	Option		"AllowGLXWithComposite" "true"
EndSection
Section "Screen"
	Identifier	"Screen"
	Device		"Nvidia"
EndSection

Section "Module"
	Load		"glx"
	Load		"dbe"	 # Double buffer extension
	Load		"extmod"
EndSection

Section "Extensions"
        Option		"Composite" "true"
EndSection
</pre>

<p>I hope this may be of use for someone else out there :) It works on my Debian sid workstation with X.org 7.1 and nvidia binary 9631 driver.</p>