Title: Fixing samba on Ubuntu 14.04 (Trusty)
Date: 2014-03-23 14:18:25
Modified: 2014-04-06 21:30:41
Slug: 20140323-fixing-samba-on-ubuntu-14-04-trusty
Location: Home
Authors: Michiel Scholten

I recently built a new at-home server, which basically is just a self-built NAS. Sharing via NFS worked immediately and other services were set up soon after.

Then came Samba. Samba (or smb) is used for Windows shares, but in our home our Linux-based NAS speaks the protocol with things like our media streamer and our Android devices (watching a serie on a tablet can be quite nice, especially when your significant other is already watching something on the TV screen).

Whatever I tried, I could not get the shares to work. Basically, it refused to log in. I tried a lot of things, then noticed something odd with smb.conf: the section [homes] was commented out, but some config lines in it were not. Especially the one `valid users = %S` is of importance here.

I ended up commenting out all of the lines in the [home] section:

	read only = yes
	create mask = 0700
	directory mask = 0700
	valid users = %S

After a restart of samba (`sudo restart smbd`) everything suddenly worked as expected and we could access the shares again.