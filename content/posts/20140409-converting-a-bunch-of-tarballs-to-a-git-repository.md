Title: Converting a bunch of tarballs to a Git repository
Date: 2014-04-09 12:07:35
Slug: 20140409-converting-a-bunch-of-tarballs-to-a-git-repository
Location: Work
Authors: Michiel Scholten
Tags: olddammit

We've all been there. Well, I've been there at least; before discovering the virtues of a real version control system, I just created a snapshot of my projects by tarring and compressing the directory tree. That way I've a bunch of histories locked inside `backup` dir per project. When I started using Subversion, I've already manually imported these archives into the first revisions of the relevant repositories (which you can see in the history log), but some old stuff was left unversioned.

I recently dusted off a really old directory with an [old project of mine I wrote at the university](http://dammit.nl/p/22) and tried to start it working again, just for fun. This also uncovered the `backup` dir containing its history. To skip manual labour, I wrote a little quick-n-dirty import script you can use with a (freshly `git init` Git repo):

<div class="embeddedobject">
<script src="https://gist.github.com/aquatix/10249476.js"></script>
</div>