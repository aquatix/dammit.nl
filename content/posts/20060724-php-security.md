Title: PHP security
Date: 2006-07-24 11:50:44
Modified: 2006-07-24 11:54:58
Slug: 20060724-php-security
Location: Home
Authors: Michiel Scholten

<p>As everybody and his dog can program in PHP nowadays, and -- worse ;) -- does without the proper programmer training in input validation and such things, here are some tips about hardened PHP, modsecurity, putting Apache in a chroot jail etc:</p>

<blockquote><p class="quote">Use security on multiple levels.
Code your stuff so it's invulnerable, but make it so even if it isn't,
the site doesn't collapse.  Put your administrative settings in a
different database, with different permissions, to your user stuff -
if possible using the administrator's password as the (my|pg)SQL user
password, so sql injections don't kill the site, just userland data.
Don't have write access where it's unnecessary, or read for that
matter: set permissions properly.  Store SQL connections strings and
other sensitive information in a file to be require_once()d from
outside the web-accessible directory, just in case php suddenly
becomes uninstalled.  Use php_flag and php_value in .htaccess, in case
your host changes php.ini without telling you.  Code so you don't rely
on anything within php.ini.  Initialise all variables before you use
them, access user input all within the $_GET, $_POST, $_COOKIE, $_FILE
superglobals.</p>

<p class="quote">Also configure your system properly.  Keep up to date!  Use hardened
php, modsecurity and apache in a jail for a start.  Give your php user
limited access only to those files it needs access to.  And then it
goes lower - secure your kernel.  use ACLs.</p>

<p class="quote">The key point here?  There are more entranceways to your server than
you think.  Block them all.  Secure your system in every place
possible.  Use encryption.  Never, ever, ever rely on a user, or
administrator, for security - have everything coded securely.  A good
administrator will keep it that way and add their own restrictions...
but a bad one might not.  Also don't be slack once you get into the
admin area.  just because it's only meant to be accessed by someone
with a vested interest in the site, that doesn't mean that's how it'll
happen.  Some stupid admin will use "d34db33f" as a password and think
they're funny - don't let this compromise the site.  And at all costs,
for the sake of humanity, make it so a site compromise can't turn your
server upside down, can't make your server a spammer, and can't modify
anything on the server other than that specific site.</p>
</blockquote>

<p><a href="http://www.securityfocus.com/archive/1/440842">Source: posting on bugtraq</a></p>

<div class="edit">edited at 2006-07-24 11:52</div>
<p>More tips:</p>
<blockquote>
<ol>
<li>Read the whole PHP security chapter <a href="http://www.php.net/manual/en/security.php">http://www.php.net/manual/en/security.php</a></li>
<li>Read about XSS, CSRF, SQL injections, session hijacking etc.</li>
<li>Always initialize your variables</li>
<li>Always escape anything going into an SQL query (if you don't use
prepared statements)</li>
<li>Do not use shell commands. Be very careful if you need to anyway</li>
<li>Never assume anything about input coming from the user.</li>
<li>Do not display data coming from the user before you are 100% sure
that the data is cleaned from XSS etc.</li>
<li><a href="http://phpsecurity.org/">http://phpsecurity.org/</a> (perhaps)</li>
<li>Do not give in to living a happy life  :-)  Stay cautious</li>
<li>This list is incomplete.</li>
</ol>
</blockquote>

<p><a href="http://www.securityfocus.com/archive/1/440150">Source: posting on bugtraq</a></p>
