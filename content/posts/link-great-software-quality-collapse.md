Title: The Great Software Quality Collapse: How We Normalized Catastrophe
Started: 2025-10-12 10:42:13
Date: 2025-10-12 11:32:12
Slug: link-great-software-quality-collapse
Location: Home
Authors: Michiel Scholten
Status: published
Category: responses
Tags: dev, ethics, llm, tech, work
Tags-examples: autism, backups, books, communication, conference, copyright, covid-19, desktop, dev, digimarks, energy, ethics, europython, family, fosdem, gadgets, gaming, hackercamp, health, hosting, howto, journal, kids, life, link, linux, meta, mobile, music, networking, notifications, opensource, photography, python, rant (fallback), reading, science, secondbrain, social, space, sync, tech, trip, ubuntu, vim, web, work
Image: 
Link: https://techtrenches.substack.com/p/the-great-software-quality-collapse

Recently I came across an article I couldn't stop nodding along with while reading.

'[Enshittification](https://en.wikipedia.org/wiki/Enshittification)' is a term we have learned the last years about platform decay and things in general just become worse (hopefully after having peeked at all). The level of quality in software development is degenerating too however.

The author of the article I am sharing here - Denis - starts off with this example:

> The Apple Calculator leaked 32GB of RAM.
> 
> Not used. Not allocated. Leaked. A basic calculator app is hemorrhaging more memory than most computers had a decade ago.
> 
> Twenty years ago, this would have triggered emergency patches and post-mortems. Today, it's just another bug report in the queue.
> 
> We've normalized software catastrophes to the point where a Calculator leaking 32GB of RAM barely makes the news. This isn't about AI. The quality crisis started years before ChatGPT existed. AI just weaponized existing incompetence.

We do not even blink any more when such a thing happens and is shipped to production. This is just a simple example of a memory leak, but there are so many cases of buggy behaviour of tools we use daily that are not fixed for years if at all, of slow software, unusable search functionality in applications, operating systems or websites, inconsistent user interfaces, leaks of user information and so much more.

I mean, the amounts of issues we have at work with Microsoft Teams, even when running in its natural habitat 'Windows' is just baffling. It has one job (supporting communication between people) and it often fails at doing even that.

'Software development' has become a huge field, so it's unsurprising that not everything is of high quality, and not everything needs to be. Apart from that, there are budget constraints and not all developers are made alike.

However, developers using 'AI' (as computer scientist I do not like this term as it just is not [real artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence), but that is another matter entirely) by means of LLM's (large language models, basically statistical models trying to predict what words/tokens should follow next) for writing software make the field even more interesting. Subtle errors can be introduced fairly easily and when the developer itself is inexperienced and/or not capable of understanding the code that has been outputted by this predictor (which is *not* capable of real reasoning, even when it tells you that it is sorry that it made a mistake and will now do better), the functionality might contain major mistakes. At best, it will cost a lot of time for more senior co-workers to rectify, at worst it will ship to production and go unnoticed for ages.

> But the real pattern is more disturbing. Our research found:
> 
> - AI-generated code contains **[322% more security vulnerabilities](https://www.eenewseurope.com/en/report-finds-ai-generated-code-poses-security-risks/)**
> - **[45% of all AI-generated code](https://sdtimes.com/security/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/)** has exploitable flaws
> - Junior developers using AI cause damage **[4x faster](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)** than without it
> - **[70% of hiring managers](https://stackoverflow.blog/2025/09/10/ai-vs-gen-z)** trust AI output more than junior developer code

Yeah.

Also, that last one hurts. That brings me to something that I worry even more about and which will structurally break the whole software development field:

> Without juniors gaining real experience, where will the next generation of senior engineers come from? AI can't learn from its mistakes—it doesn't understand why something failed. It just pattern-matches from training data.
> 
> We're creating a lost generation of developers who can prompt but can't debug, who can generate but can't architect, who can ship but can't maintain.
> 
> **The math is simple:** No juniors today = No seniors tomorrow = No one to fix what AI breaks.

We might be headed into a world where we will not even be capable of [vibe coding](https://en.wikipedia.org/wiki/Vibe_coding).

Something that people might not be aware of, is the stupid amounts of energy those word generators are using:

> **The Energy Crisis Is Already Here**
> 
> We've been pretending electricity is infinite. It's not.
> 
> Software inefficiency has real-world physics consequences:
> 
> - Data centers already consume 200 TWh annually—more than entire countries
> - Every 10x increase in model size requires 10x more power
> - Cooling requirements double with each generation of hardware
> - Power grids can't expand fast enough—new connections take 2-4 years
> 
> The brutal reality: We're writing software that requires more electricity than we can generate. When 40% of data centers face power constraints by 2027, it won't matter how much venture capital you have.

I want to close with this banger:

> We've created a perfect storm: tools that amplify incompetence, used by developers who can't evaluate the output, reviewed by managers who trust the machine more than their people.

I recommend to read the rest of this link, you might find some handy links to answer/temper your boss's "we need to use AI!" calls with :)
