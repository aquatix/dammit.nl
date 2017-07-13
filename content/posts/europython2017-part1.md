Title: EuroPython 2017, part 1
Started: 2017-07-11 10:51:00
Date: 2017-04-30 20:17:00
Slug: europython2017-part1
Location: Rimini, Italy
Authors: Michiel Scholten
Category: conferences
Tags: python, europython, trip, conference
Image: https://shuttereye.org/images/1c/1c1e0e87cba52524_2000-2000.jpg
Status: draft

[EuroPython 2017](https://ep2017.europython.eu/en/)

## Day zero, Sunday

After a rather pleasant flight on Sunday morning, where out of 80 passengers, I sat next to the only other EuroPython visitor, I took a nicely airconditioned train from Bologna to Rimini. I really hoped that airco was everywhere, otherwise the 33C would seriously hamper my capability of even remembering what was said just five minutes ago.

My newfound acquaintance and me got some good Italian food inside us, cooled down for a few minutes at the beach, breathing in the sea air and explored Rimini centre for a bit, where the heat was slowly leaking out of the stones.


## Day one, Monday

Moving on to Monday, I was thankfully doing just fine. The walk through the park (literally) to the venue was warm and lengthy but shady and beautiful, and the venue was well organised and cool, suiting my feeble brain.

Starting off with an enlightening keynote by Armin Ronacher, where we were reminded of the fact that files and other input still are not UTF-8 (even going beyond UTF-8 now we have emoticons, which are in an even higher byte space), making it hard to do string slicing and such. Also, don't subclass dictionaries. Just don't.

I moved on to a hands-on session with Django and Celery, as I wanted to see if there were some features I wasn't aware of yet, or pointers to solutions to some minor issues we are having at Sanoma.

Coming away with some remarks about just using chains and groups, as things like chords can act weirdly in certain circumstances (like on RabbitMQ, which surprise surprise is what we use at home), I thought that maybe some small refactoring is in order.

Next up was a talk about how you can know that the mocks you created for a (third party) API are valid. Vuforia (an image matching service) was used as example. `requests-mock` is of course a useful tool here, and the speaker made his mock into a Flask app, which translated requests-mock to something that could be used by their library.

The verifying part is done by running all the tests twice, once against the real service, and once against your mock. This checks if the responses are the same. By scheduling tests with for example Travis CI, you can then find out about (undocumented) changes to the third party service in a timely and targeted fashion (as the failing test points to the exact location), making it a lot more easy to fix your library.

Also, if you ship software, you really should ship it with a verified fake, so people can use that to test their own software; it adds a lot of value to your product.

After the lunch it was time to measure, don't guess. A nice hands-on presentation of how to profile your code, so you can optimise where needed. Premature optimisation is the root of all evil, so knowing where to actually put your efforts is really useful.

A string of tools were introduced, apart from the excellent Jupyter notebook software to experiment with (really, if you don't know it, or never used it, `pip install jupyter` and `jupyter notebook` it). Build into Python itself is timeit (`import timeit`, `timeit.default_timer`, don't use os_time or time_clock, as they will give different results depending on your OS platform). `snakeviz` is a browser based graphical viewer of the output of Python's cProfile module, representing time spent in various parts of the code as concentric circles, making it easy to zoom into troublesome parts. It can be run standalone, or as a module: `python -m snakeviz`, `python -m cProfile -o pi.stats simple_pi.py` for example ([example code](http://www.python-academy.com/download/europython2017/)), or just `snakeviz pi.stats`. Be aware that tool measures itself too of course.

In jupyter, you can load such modules to experiment with interactively:

    load profile_me.py <shift>-<enter>
    %load_ext snakeviz
    %snakeviz test()

Same with `timeit`:

    %timeit
    %%timeit  # multi-line version, where you can add more lines of code to test
    %timeit?  # to get help of course


The [line profiler](https://github.com/rkern/line_profiler) is another tool that gives information about what lines of code are troublesome:

- `pip install line_profiler`
- `kernprof (-v)`
- line-by-line profiling: -l
- `kernprof -v -l profile-me_use_line_profiler.py`
- in jupyter: `load_ext line_profiler`

For memory usage, [Pympler](https://pythonhosted.org/Pympler/) can be used. It keeps track of changes in the size of data structures, so you can see where your code balloons, or even where memory is leaking:

    from pympler import tracker
    t = tracker.SummaryTracker()
    t.print_diff()
    big = list(range(10**6))
    t.print_diff()  # shows how big the datastructure we just created is (as it shows the difference with the previous measurement)

With the Python functools one can create decorators (like in ./measuring/memory_size_pympler.py: measure_memory in the example code linked above). This one creates a decorator the create a measurement of a function, storing it in a variable.

matplotlib is another great library to visualise data.

Finally, there is another memory profiler:

`pip install memory_profiler`, `%load_ext memory_profiler` and then you can do something like:

    import use_mem  # an application
    %mprun -f use_mem.use_mem use_mem.use_mem(numbers)

So, enough pointers to play with and explore from.

The conference seems well balanced and organised and the participants are generally really social, making for interesting chats over food.

It's also refreshing to see the amount of female attendees. I really hope it's a good sign for the future, as in my opinion we need more of their talent in our field of work.


## Day two, Tuesday

Instead of walking, I decided to make use of the loaner bikes of the hotel, which was really an improvement.

Cooling down, the kickoff of the day was about data visualisation by Dutch visualiser Jan Willem Tulp. This was great to behold, seeing how he made big and complex datasets comprehensible and even beautiful, appealing to laymen too (his animated globe with number of trees was used in a nice demo from a news publication).

[IMAGE]

[animation]


After enjoying the nice visuals and inspirational talk, I was curious how to use and write decorators to eliminate the need for some classes.

There is a nice talk about why you should stop writing classes: https://www.youtube.com/watch?v=o9pEzgHorH0

Decorators are rather easy to use, not trivial to write, but also not that hard to do, and can be really helpful in making your code more clear.


Continuing with a smart use of metaclasses by using abstract base classes (ABCs). Those help with testing behaviour, not structure.

When trying to find out if some object is what you need, checking the type (isinstance() and such) is not really the intention, because some object or class can behave like a certain class, but is of course not exactly that implementation/type you are checking. A perfect solution would be something like: `if behaveslike(someobj, ListBehaviour):`

Abstract base classes are categories (like labels/tags, but it's just a promise to act in a certain way, no checks are done). Using them though, enables you to do the above comparison.

Python Collections has a lot of classes that represent interesting behaviours (go check them).

Some more notes:

- Python is based on delegation, which is good news; magic functions come into play.
- Virtual subclasses: ParentClass.register(ChildClass), with opposite relationship, where the ParentClass knows the ChildClass, but not the other way around like in regular subclassing. Useful for when you want to know all the subclasses of a certain class. Registering is a promise, no check done, so be careful.
- A metaclass can put things into the class that is linked to it.
- You can abstract base classes to build interfaces, but in the speaker's opinion this is not the way to go. Can be useful though.


After that I attended a slightly confused talk about design patterns and why we don't need them in Python. The idea was good, as design patterns were thought up in a time that programming languages were in a place where developers needed them to enforce certain restrictions, but then the speaker started showing where certain design patterns were still used or usable inside Python. All in all a good way to brush up on my old knowledge of them and seeing why I don't program in Java anymore.

Some of the points and design patterns:

- Java: design patterns! (general reusable solution to a commonly occurring problem; formalised best practices; just outlines though, not ready to use)
- Singletons in python? Modules!
- Visitor pattern: ASTs (abstract syntax trees, linters use those)
- Decorator patterns (not the @decorator in python)
- Is magic worth the effort? It depends, readability wins.

His take-away was good though: know your tools well, get inspiration from other languages and communities, know the business domain of your project.


After lunch there was a subject that I am really curious about: "There should be one obvious way to bring python into production" by Sebastian Neubauer.

[His slides](https://ep2017.europython.eu/conference/talks/there-should-be-one-obvious-way-to-bring-python-into-production) are available from the talk page, which are a good set of guidelines.

It talked about the various stages inside the delivery pipeline. When a software product has to be shipped, it has to be built and packaged. Some requirements here are that it should be built once, used everywhere, the possibility to compile it for the target systems and that versions should be really unique, preferably signed. You should not have a version 1.0.2 without $fileX and one with $fileX (because you forgot to include it in the first build).

Nice to have: upload the build to an artifact repository.

A risk is that the build environment is misconfigured.

Testing should be automated, with near production-like and reproducible conditions, and minimal changes should be done for testing reasons. Nice to have are of course fast feedback and having the tests run after each commit on all branches (something that we are already doing in quite some projects in Sanoma).

A risk here is that the tests test the test env, not production (e.g., pytest pulls in $package that turns out to be missing when deploying to production).

After that, Staging/QA has to receive an automated deploy in a production-like environment, with nearly no changes for testing purposes. It has the risk of being an outdated, manually maintained setup, so be sure to take care of this stage.

Nice to haves for a staging environment are that it is a real clone of the production system and the possibility to run A/B tests on the system.

Production should have all kinds of restrictions, like no compiler, no internet, health monitoring and preferably have automated deploys, automated monitoring, self-healing and automatic rolling updates and roll-backs.

Because of the ecosystem of software, we frequently run into the dependency hell. We have multiple layers of package managers (from OS-level, to the Python world (`pip`) and of course the JavaScript world).

Within the Python package management there's still much confusion around setuptools, distutils, eggs and such.
  - Many outdated 'best practices' on StackOverflow etc
  - pyscaffold, versioneer (templates for packages)

Possible solution: Nix inside a container? Someone from the audience proposed using Flatpak or Snappy instead, which sound to me better candidates, seeing how mainstream Linux distro's are already including support for them.



Energy started running low, so the interesting, but fast talk about [Descriptors](https://docs.python.org/2/howto/descriptor.html) left me with some notes that I really should look into them a bit more.


After that, Django and GraphQL seemed like a nice break from the de-facto REST standard (not that I dislike DjangoRestFramework). This new API standard, [created by Facebook](https://facebook.github.io/react/blog/2015/02/20/introducing-relay-and-graphql.html), has one endpoint and uses queries instead of paths to retrieve data. This was not new for me, but I was curious to the current state of integration with Django. Turns out that using `graphene` and `graphene-django` gets you going quite nicely. Enable the app and then it's only adding some glue to be able to retrieve data from your models.

Authentication is handled, as is usage/viewing permission per field. Apparently there are still issues when also using DjangoRestFramework, but a pull request is in review.

Good to know that you should limit the nesting you can have, as queries can get rather deep otherwise. GitHub does something like that already.

Frontends that can be used in concert with your shiny GraphQL are Facebook's Relay for React, and the really [Open Source Apollo](https://github.com/apollographql).



### Lightning talks


Reporting security issues: if someone reports to you, take it seriously. Create a howto in your README too.

If reporting yourself, do it privately, you might take someone off guard, also possibly endanger users.


Don't document your experiences for others, experience your vacations and such for yourself (you can still take pictures and souvenirs, but do it for yourself).


gitmate.io
gitmate-bot
coala
IGitt (an exclamation of disgust)
Interface for Git{Hub|Lab}
https://gitlab.com/gitmate/open-source/IGitt


Quickly create/publish packages on pypi: flit
https://pypi.python.org/pypi/flit
https://pypi.org/

