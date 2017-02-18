Title: Debugging Voice over IP
Date: 2008-04-08 10:40:25
Slug: 20080408-debugging-voice-over-ip
Location: Home
Authors: Michiel Scholten
Tags: rant

<p>Yesterday our provider [Speedlinq, or Telfort Internet or GreenISP or whatever they want to call themselves nowadays] switched to another VoIP platform for ADSL connections. They sent a letter with a cd-rom for changing the settings in VoIP-enabled ADSL modems, but we have a VoIP phone, with SIP routed through to it. No problem, <a href="http://www.speedlinq.nl/html/beterbellen/anderemodem.html">their help site had settings</a>. Except that they didn't work and did not map well on the configuration fields of our SIP phone - an E-Tech.</p>

<p>So after fiddling around, I discovered I should just ignore the sip.telefoniedienst.nl server completely, and only use tel.telefoniedienst.nl:</p>

<pre>
Domain:       tel.telefoniedienst.nl
SIP Proxy:    tel.telefoniedienst.nl:5060
Phone number: 10-numbered phone number, like in the letter, starting with 0
Account:      Same number
Password:     Provided in the letter
</pre>

<p>... with domain being the SIP server [registrar/realm] you log into. This worked! <a href="http://aquariusoft.org/~mbscholt/images/content/voip_phone_config_anon.png">See the complete settings for the E-Tech VPPH01 VoIP phone</a> [anonymised a bit, be sure to set the correct IP addresses etc too].</p>