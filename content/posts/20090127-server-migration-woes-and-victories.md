Title: Server migration woes and victories
Date: 2009-01-27 17:21:55
Slug: 20090127-server-migration-woes-and-victories
Location: Work
Authors: Michiel Scholten

<p>Yesterday evening the server hosting aquariusoft.org's services was scheduled for migration to another machine in another data center. As it is a virtual private server (better known as a virtual machine) on a <a href="http://en.wikipedia.org/wiki/Xen">Xen</a> host, this would mean shutting it down, copying the image over the interconnect to the other data center (at a nice rate), configuring the proper Xen and network magic on that machine and booting it online again. However, because of some tweaking of the network settings on the dom0 (the host machine), things went haywire there and the migration was aborted. So, after a downtime of about two hours, aquariusoft.org (and diginaut.net) came up again at the exact same location as it started out, still at the first server of <a href="http://soleus.nu/">our nice hosting club Soleus</a>.</p>

<p>So today the network stack was fixed (something to do with ethernet jumbo frames and the driver not liking them) and by lunchtime we decided to try again. It took a while to get things right (mine was the first member domU that was migrated), but after working out some kinks in networking it's zooming along happily now. So if you noticed some breakage, it was the server flying down the tubes to another place and another IP address.</p>

<p>Thanks guys of the Soleus core team, and good luck with migrating the rest of Soleus to those nice machines!</p>

<p>PS: if you still encounter something broken, please notify me :)</p>

<div class="edit">edited at 2009-01-27 21:21</div>
<p>I forgot to include the visualisation of a server jumping from host to host (at the 10 mark; that's 14GB of `higgs' being moved):</p>

<div class="content-image"><div><img src="http://aquariusoft.org/~mbscholt/images/content/195852253_70-day.png" alt="Spike denoting higgs being transferred" title="Spike denoting higgs being transferred" /></div></div>
<br style="clear: both;" />

<p>The big chunk of data the night before is both my server `higgs' and another one, <a href="http://rock-y.org/post/migratie-vps/">which was also successfully migrated today</a>.</p>