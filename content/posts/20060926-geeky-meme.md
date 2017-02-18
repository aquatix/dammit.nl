Title: Geeky meme
Date: 2006-09-26 09:50:39
Slug: 20060926-geeky-meme
Location: Home
Authors: Michiel Scholten
Tags: rant

<p>Currently, a <a href="http://www.grep.be/blog/2006/09/25/#command_frequency">command frequency meme</a> seems to propagate through Planet Debian, and I thought I'd run that one-liner as well. Some interesting results yielded:</p>

<p>At my laptop:</p>
<pre>
09:43:23 mbscholt@galadriel:~$ history|awk '{print $2}'|awk 'BEGIN {FS="|"} {print $1}'|sort|uniq -c|sort -rn|head -10
    331 cd
     35 ll
     21 vim
     12 cp
     10 mc
      9 PROMPT_COMMAND='pwd>&amp;7;kill
      9 mv
      8 wget
      6 luna
      6 killall
</pre>

<p>As root on my server:</p>
<pre>
09:43:14 root@luna# history|awk '{print $2}'|awk 'BEGIN {FS="|"} {print $1}'|sort|uniq -c|sort -rn|head -10
    106 ll
     82 vim
     59 cd
     48 apt-get
     17 du
     16 /etc/init.d/apache2
     14 cp
     14 addgroup
     12 rm
     10 mc
</pre>
<p>One of my normal user screen sessions:</p>
<pre>
09:43:10 mbscholt@luna:~/projects/overload_iserv/server$ history|awk '{print $2}'|awk 'BEGIN {FS="|"} {print $1}'|sort|uniq -c|sort -rn|head -10
    108 vim
    102 ll
     67 cd
     46 svn
     46 cp
     17 du
     13 pine
     11 python
      9 wget
      9 grep
</pre>

<p>So it looks like I'm mostly moving from place to place looking what's there, and editing the hell out of it :) And it's funny, but I sometimes have <a href="http://kitenet.net/~joey/blog/entry/nervous_twitches.html">those nervous twitches</a> too.</p>