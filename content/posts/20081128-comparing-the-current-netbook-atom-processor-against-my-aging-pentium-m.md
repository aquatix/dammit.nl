Title: Comparing the current netbook Atom processor against my aging Pentium-M
Date: 2008-11-28 15:46:29
Slug: 20081128-comparing-the-current-netbook-atom-processor-against-my-aging-pentium-m
Location: Home
Authors: Michiel Scholten
Tags: rant

<p>I have a nice and trusty <a href="http://aquariusoft.org/~mbscholt/images/content/acer_tm8000.jpg">15" Acer Travelmate from the 8000 series</a>. It has a 1400x1050 tft, dvd-rom/cd-rewriter, currently 80GB hdd and 1.25GB of RAM. Its keyboard is really nice for typing at long stretches, being curved a bit and having great keys. The machine also sports a 1.5GHz Pentium-M processor on the first Centrino platform. This is a <a href="http://en.wikipedia.org/wiki/Pentium_M#Dothan">Dothan core</a> known as the Pentium-M 715. This machine has been serving me for way over four years already, and I hope to have it around for some more. The original 60GB hdd already is replaced with a new one after it died, and one of the 256MB ram banks has been transferred to my girlfriend's laptop and replaced with a 1GB one.</p>

<p>Nowadays the <a href="http://en.wikipedia.org/wiki/Netbook">tiny laptops known as netbooks</a> are being in demand. Ever since Asus started this new type with the first 7" Eee, manufacturers crank out loads of them, almost all based on the Intel Atom processor (generally using the N270 single core, running at 1.6GHz). They vary in size, which results in some having a handy small formfactor and 7" screen with as con a cramped keyboard and others having a 10" screen and almost-full-sized keyboard. Of course everything in between can be found too.</p>

<p>I wouldn't consider using one of those as replacement for my current laptop, as working the whole day for a whole week on such a device would ruin your hands and maybe even your neck and eyes for sure. However, they are really portable and as such great tools for couch surfing/irc'ing and to drop into your bag when travelling a bit.</p>

<p>I found <a href="http://my.ocworkbench.com/2008/gigabyte/M912/g4.htm">a bunch of benchmarks of various netbooks</a> and went looking for the same numbers on my Dothan 1.5GHz machine. I found <a href="http://www.notebookcheck.net/Review-Acer-Aspire-1690WLMi.124.0.html">benchmarks of a similarly specced Acer</a>, which I added to the table I found on the first page (what kind of html editor that those guys use, it almost looked like some msword export...). The results are these:</p>

<table>
<tr>
<th width="16%">&nbsp;</th>
<th width="16%">Acer Aspire 1690WLMi (Intel Pentium-M Dothan 1.5GHz)</th>
<th width="16%">Gigabyte M912 (Intel Atom 1.6GHz)</th>
<th width="16%">MSI Wind (Intel Atom 1.6GHz)</th>
<th width="16%">ASUS Eee PC 901 (Intel Atom 1.68GHz)</th>
<th width="16%">ASUS Eee PC 900 (Intel Celeron 900 mobile)</th>
</tr>
<tr>
<td width="16%">Memory Bandwidth</td>
<td width="16%">n/a</td>
<td width="16%">2.85G/2.16G</td>
<td width="16%">2.84G/2.41GB</td>
<td width="16%">2.8G/2.4GB</td>
<td width="16%">2.05GB/2.08GB</td>
</tr>
<tr>
<td width="16%">Dhrystone</td>
<td width="16%">6431 MIPS</td>
<td width="16%">3897 MIPS</td>
<td width="16%">3846 MIPS</td>
<td width="16%">3883 MIPS</td>
<td width="16%">2635 MIPS</td>
</tr>
<tr>
<td width="16%">Whetstone</td>
<td width="16%">2076 MFLOPS (FPU) / 2659 MFLOPS (iSSE2)</td>
<td width="16%">3353 MFLOPS</td>
<td width="16%">3321 MFLOPS</td>
<td width="16%">3350 MFLOPS</td>
<td width="16%">2181 MFLOPS</td>
</tr>
<tr>
<td width="16%">Multimedia Int X8</td>
<td width="16%">14176 it/s (Integer x4 iSSE)</td>
<td width="16%">29558 it/s</td>
<td width="16%">29211 it/s</td>
<td width="16%">29614 it/s</td>
<td width="16%">8377 it/s</td>
</tr>
<tr>
<td width="16%">Multimedia Float X4</td>
<td width="16%">15671 fit/s</td>
<td width="16%">20017 fit/s</td>
<td width="16%">19746 fit/s</td>
<td width="16%">20041 fit/s</td>
<td width="16%">9522 fit/s</td>
</tr>
<tr>
<td width="16%">Super PI 1M</td>
<td width="16%">n/a</td>
<td width="16%">1 min 35 s</td>
<td width="16%">1 min 34 s</td>
<td width="16%">1 min 31 s</td>
<td width="16%">1 min 27 s</td>
</tr>
<tr>
<td width="16%">Random Access</td>
<td width="16%">18,9ms</td>
<td width="16%">18.1ms</td>
<td width="16%">16.9ms</td>
<td width="16%">0.5ms</td>
<td width="16%">0.5ms</td>
</tr>
<tr>
<td width="16%">CPU Utilisation</td>
<td width="16%">4.6%</td>
<td width="16%">4%</td>
<td width="16%">3%</td>
<td width="16%">2%</td>
<td width="16%">2%</td>
</tr>
<tr>
<td width="16%">Average Read</td>
<td width="16%">21,2 MB/sec (65,7 MB/sec burst)</td>
<td width="16%">51.1 MB/sec</td>
<td width="16%">38.7 MB/sec</td>
<td width="16%">26.7 MB/sec</td>
<td width="16%">28 MB/sec</td>
</tr>
</table>

<p>From the <a href="http://my.ocworkbench.com/2008/gigabyte/M912/g4.htm">netbook benchmarks</a>: "From the results, we can see that the Atom based machines all perform similarly in data crunching. The differences are largely due to the HDD used. In this case, the Gigabyte M912 does perform better in the disk performance tests. The Fujitsu HDD gives is an edge over the MSI Wind and Eee PC 901 (SSD) in terms of average Read. When it comes to random access, the SSD is no doubt the fastest and is noiseless."</p>

<p>So it seems the Atom is slightly faster overall, but not shockingly so. I think the experience will be quite on-par with what I'm used to on my full-sized laptop, except for a (much?) smaller form factor. The <a href="http://en.wikipedia.org/wiki/Aspire_One">Acer Aspire One</a> seems to have a nicely sized keyboard, and I'm also interested in the <a href="http://www.laptopmag.com/review/laptops/samsung-nc10.aspx">Samsung NC10</a>. Time will tell whether I will get me one of those, or whether I will skip on them and stick with my full-sized laptop, workstation and Nokia N810 internet tablet. Or get a 12" or 13" IBM/Lenovo. And <a href="http://www.engadget.com/2008/08/28/samsung-debuts-x360-lighter-than-air-ultraportable/">this Samsung X360</a> <a href="http://www.engadget.com/photos/samsung-x360-handled-fights-macbook-air-to-the-death/1004432/">looks really nice too</a>, and it's a lot faster than those Atoms. Fun times.</p>