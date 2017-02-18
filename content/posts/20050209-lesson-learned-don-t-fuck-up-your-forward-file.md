Title: Lesson learned: don't fuck up your .forward file
Date: 2005-02-09 10:05:33
Modified: 2005-02-09 10:18:50
Slug: 20050209-lesson-learned-don-t-fuck-up-your-forward-file
Location: Home
Authors: Michiel Scholten
Tags: rant

<p>OK, I'm feeling really stupid. I managed to change my exim .forward file [which filters my e-mail neatly into a lot of mail folders] in such a way that it doesn't deliver e-mail _at all_. Ouch. Such a stupid typo. Well, two of them. I hope these messages are still drifting somewhere in the mail subsystem and get delivered after all, because there are some very important ones among them. Gah.</p>

<div class="edit">edited at 2005-02-09 10:18 CET</div>

<p>W00t, just for the record: run <em>exim -qqff</em> as root, and you're just fine :D</p>