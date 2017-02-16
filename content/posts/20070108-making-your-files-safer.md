Title: Making your files safer
Date: 2007-01-08 14:18:26
Slug: 20070108-making-your-files-safer
Location: Home
Authors: Michiel Scholten

<p>When sharing a machine with users you gave an account, you'd better take some precautions for your precious files in general dirs [like /storage or whatever]. To do so, do:</p>

<pre>
Recursively setting files to 644 and dirs to 755:
chmod -R 644 *
find . -type d -exec chmod 755 '{}' ';'
</pre>

<p>... for example. This is good to remember anyway.</p>