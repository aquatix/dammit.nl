Title: EuroPython 2017, part 2
Started: 2017-07-12 10:41:00
Modified: 2017-08-07 15:28:00
Date: 2017-08-07 15:28:00
Slug: europython2017-part2
Location: Rimini, Italy
Authors: Michiel Scholten
Category: conferences
Tags: python, europython, trip, conference
Image: https://shuttereye.org/images/0f/0f1332a16d8f3130_2000-2000.jpg

<!--
[![IMG_20170711_182348](https://shuttereye.org/images/0f/0f1332a16d8f3130_2000-2000.jpg)](https://shuttereye.org/goingout/2017_europython/IMG_20170711_182348.jpg/view/)
-->

Photos of the whole [EuroPython 2017](https://ep2017.europython.eu/en/) conference are available at [the EuroPython 2017 flickr group](https://www.flickr.com/groups/3845891@N22/), the [EuroPython 2017 website](https://ep2017.europython.eu/en/europython/photos/), and [my photo gallery](https://shuttereye.org/goingout/2017_europython/).

Videos (lifestream captures for now) are at [YouTube](https://www.youtube.com/playlist?list=PL8uoeex94UhEP1C94Fgdn3PdXitS8RtOV), more will go live later at the [EuroPython YouTube Channel](https://www.youtube.com/c/EuroPythonConference). Recommended.


## Day three, Wednesday

We kicked off with the keynote ['If Ethics is not None'](https://ep2017.europython.eu/conference/talks/if-ethics-is-not-none) by Katharine Jarmul with a lot of food for thought.

[![Expert system spoof on 'do you know where your children are?'](https://shuttereye.org/images/47/47594d4d25361f1f_2000-2000.jpg)](https://shuttereye.org/goingout/2017_europython/IMG_20170712_094331.jpg/view/)

[Some good quotes were used](https://dammit.nl/computer-ethics-quotes.html), and the book [Cybernetics or Control and Communication in the Animal and the Machine](https://books.google.nl/books?id=NnM-uISyywAC&pg=PA27&dq=wiener+It+may+very+well+be+a+good+thing+for+humanity&sa=X&redir_esc=y#v=onepage&q=wiener%20It%20may%20very%20well%20be%20a%20good%20thing%20for%20humanity&f=false) by Norbert Wiener seems like a good read. As community, we should take care to keep thinking about the implications of the technology we create, as we should not blindly trust it or its users.


Next up the ['Mary had a little lambda' talk](https://ep2017.europython.eu/conference/talks/mary-had-a-little-lambda) was a really fun (re)introduction to lambda calculus. Yes, the calculus, not the lambda functions in Python, but Anjana Vakil continued with implementing the Church Numerals in lambda functions and we did some arithmetic with Python in Church Encoding. Fun and energetic talk, which I would have loved to have at university, instead of the long dry one I got there on the same material. [Lambda calculus](https://en.wikipedia.org/wiki/Lambda_calculus) was invented by Alonzo Church, starting in 1932, for 'expressing computation based on function abstraction and application using variable binding and substitution' and is Turing complete.


Lee Sheng's talk on ['Teeing up Python: Code Golf'](https://ep2017.europython.eu/conference/talks/teeing-up-python-code-golf) (check out the slides there) had a lot of good points about writing sane, short and readable code. For example, try using a default: `to_mail = my_contact.get("address", "UNKNOWN")` instead of checking if a key exists and then getting it from the list. See the slides on why this is less strokes (less assignments, lookups and more). Automatically cleaning up resources by using the (well-known, right?) `with open('myfile', 'r') as infile:` and such also make for less error-prone code.

A (list) comprehension also safes you some strokes, and can result in better readable code:

    result = []
    for item in things:
        if condition(item):
            result.append(transform(item))
    # 14 strokes

    result = [ transform(item) for item in things if condition(item) ]
    # 12 strokes

In [the slides](https://docs.google.com/presentation/d/e/2PACX-1vQ5ymUw7j58oEU0pTsTL-OUNMNrTq_HUE8_Z-tsKgFPo8FwNfK_EgWmUtn0oEG11MCM_259_aMmLdSY/pub?start=false&loop=false&delayms=3000#slide=id.p) ([PDF](https://ep2017.europython.eu/media/conference/slides/teeing-up-python-code-golf.pdf)) are some more tips.


<!--
Even the speakers were nerding out:

[![TARDIS speaker](https://shuttereye.org/images/7e/7efd3717937e9fad_2000-2000.jpg)](https://shuttereye.org/goingout/2017_europython/IMG_20170711_092517.jpg/view/)
-->

An interesting Big Data/distributed computing talk was [Realtime Distributed Computing At Scale (in pure Python!): Storm And Streamparse](https://ep2017.europython.eu/conference/talks/realtime-distributed-computing-at-scale-in-pure-python-storm-and-streamparse) by Alexander Lourenco from Parse.ly.

Storm is a distributed real-time computation system, which simplifies workers and queues. Streamparse is basically Pythonic Storm; Nimbus and Storm UI are visual frontends.

You can install the Storm environment from the Apache Storm site.

Streamparse is even easier, just use pip:

    pip install streamparse
    sparse quickstart
    sparse run



The [Infrastructure design patterns with Python, Buildbot, and Linux Containers](https://ep2017.europython.eu/conference/talks/infrastructure-design-patterns-with-python-buildbot-and-linux-containers) talk was a bit disappointing. It was basically David Liu's hobby project of (ab)using Dask (a distributed task system) and buildbot (normally known to be a continuous integration (CI) framework) for things it is not really intended, like remotely executing random scripts.

I better could have gone to [How to make money with your Python Open-Source Project](https://ep2017.europython.eu/conference/talks/how-to-make-money-with-your-python-open-source-project) by Max Tepkeev, which would have been relevant for my own projects and probably for some of Sanoma's efforts too.


[![Roman bridge](https://shuttereye.org/images/ce/ce5a3519d519279d_2000-2000.jpg)](https://shuttereye.org/goingout/2017_europython/IMG_7069_crop.jpg/view/)



## Day four, Thursday


Kicking off with [Type Annotations in Python 3: Whats, whys & wows!](https://ep2017.europython.eu/conference/talks/type-annotations-in-python-3-whats-whys-wows) by Andreas Dewes, Thursday was in for a good line-up.

Executive summary: Python 3.6 is great, start using it. However, in older 3.x versions and also in 2.7, some nifty things can be done with hints about variable types.

- Gradual typing, where you add annotations to code where it makes sense (so you don't have to rewrite your complete codebase)
- Function annotations were the first step in Python 3.0 in 2006 (PEP 3107)
- In 3.5 Type Hints were introduced (including the theory and such)
- Python interpreter stores those annotations in `__annotations__` and ignores it otherwise
- External tools like [_mypy_](http://mypy-lang.org/) and _pycharm_ do the heavy lifting
- Deliberate choice to do it like this, so it can evolve; eventually we might want to have internal tools
- We lose Python 2 compatibility though, but then we can use _type comments_, which are backported to 2.7
- A third approach is stub files, ending with .pyi, which _mypy_ will also look at, ignoring the .py file for type checking. This way, we can add only the annotations there. Feels a bit like writing a header file
- Check the documentation of the typing module for more info, lots of usecases (new in 3.5)
- The [slides are on Slideshare](https://www.slideshare.net/japh44/type-annotations-in-python-whats-whys-and-wows)



[Inside Airbnb: Visualizing data that includes geographic locations](https://ep2017.europython.eu/conference/talks/inside-airbnb-visualizing-data-that-includes-geographic-locations) by Guillem Duran Ballester provided some interesting visualisations of Airbnb locations (specifically Barcelona and Mallorca). By doing so, he introduced quite some useful tooling for drawing maps, drawing shapes on them (for example for area's to aggregate datapoints to densities) and various shaders. Everything was demoed through [Jupyter notebooks](https://github.com/Guillem-db/Inside-Airbnb-EP17). Data from [insideairbnb](http://insideairbnb.com/) was used.

Some take-aways:

- [bokeh](https://github.com/bokeh/bokeh) is a great library to work with Google Maps (take a look at lat & lon, zoom and map_type)
- [shaolin](https://github.com/HCsoft-RD/shaolin) for colormaps
- shapefiles with [shapely](https://github.com/Toblerity/Shapely) (for drawing overlays on the map, for example to colour an area of a town)
- holoviews and geoviews (matplotlib, bokeh and shapely as backends)
- [datashader](https://github.com/bokeh/datashader): plotting big data made easy; lots of Jupyter notebooks as examples
- `dynamic=True` will recalculate the bins that datashader makes, making it nicer to look at when zooming in (with dynspread/datashade)
- one of the downsides of datashader is that when tweaking, it errors until you get everything right (for example in Jupyter)
- [Working with Bokeh documentation](http://geo.holoviews.org/Working_with_Bokeh.html)
- integrating openstreetmaps with bokeh should be possible, speaker needs to look into it (but Google Maps is default)
- [The code of the rent status of Airbnb venues](https://github.com/dsolanno/BarcelonaRentsStatus).


[![Conference location artifact](https://shuttereye.org/images/61/613362cc8eb23616_2000-2000.jpg)](https://shuttereye.org/goingout/2017_europython/IMG_20170712_170046.jpg/view/)


The [An introduction to PyTorch & Autograd](https://ep2017.europython.eu/conference/talks/an-introduction-to-pytorch-autograd) talk from Paul O'Grady provided some tools to do deep learning with Python.

Tensor (ndarray) operations on the GPU (instead of being constrained to CPUs) are a lot faster.

`pytorch` is the new kid on the block. It follows Lua torch, with same underlying C libraries and is a define-by-run framework as opposed to define-and-run, leads to dynamic computation graphs, looks more Pythonic. The native data format is [tensors](https://en.wikipedia.org/wiki/Tensor), which is a bit different than what we are used to, but makes sense in these computations. Torch supports in-place adds and such (.add_() ) and plays well with numpy; it can bridge back and forth (for example having matrix operations and getting a tensor back). To get more insight in the data, you can reshape tensors using views. One of the nice optimalisation things is that tensor computation can be moved to and from GPU (CUDA). Support for variables is added through the [torch.autograd package](http://pytorch.org/docs/master/autograd.html).


Next up was [Developing elegant workflows in Python code with Apache Airflow](https://ep2017.europython.eu/conference/talks/developing-elegant-workflows-in-python-code-with-apache-airflow) where Michał Karzyński talked about creating data flows with Airflow.

The definition of a workflow is a sequence of tasks, started on a schedule or triggered by an event, frequently used to handle big data processing pipelines.

Apache Airflow is Open Source, based on Flask, using Celery.

A flow is a Directed Acyclic Graph (DAG). An Operator is a single task, which can be retried automatically, should be idempotent and is a Python task with an execute method. Airflow uses xcom as a means of communication between task instances; a task is saved in the database as a pickled object; it is best suited for small objects. An introductory Airflow tutorial can be found on the speaker's weblog: [Developing workflows with Apache Airflows](http://michal.karzynski.pl/blog/2017/03/19/developing-workflows-with-apache-airflow/).


[Inspect (Or Gadget)](https://ep2017.europython.eu/conference/talks/inspect-or-gadget) by Hugues Lerebours and Renaud Bauvin introduced a really useful library: [`inspect`](https://docs.python.org/3/library/inspect.html) which provides quite some extra functions apart from the already useful Python buildins. The demo consisted of a piece of code that checks if docstrings are up-to-date, also validating against documented types. Good material to check out when needing to do some introspection.


Another talk about improving your code's quality was [Fixture factories for faster end-to-end tests](https://ep2017.europython.eu/conference/talks/fixture-factories-for-faster-end-to-end-tests) by Stephan Jaensch, speaking about creating better fixtures to improve tests in this age of microservices and other loosely coupled services.

When testing such a setup, you want end-to-end integration, replicating production as much as possible (above 'regular' integration tests). This results in slow, most expensive tests. Tools used in such a test setup are `pyramid`, `swagger`, `openapi`, and `sqlalchemy`. Creating it needs lots of db setup on all the components, lots of SQL scripts, and is hard to write, and maintain.

Taking inspiration from Django, fixture factories are introduced. They allow you to create fixtures, not only for your service, but for downstream services as well and without code duplication. These fixtures take care of common default values and make sure data is logically correct. They integrate nicely with `pytest`.

Why not use models? No foreign key (FK) checking used in this setup, so cannot use the PK and FK's.

This setup helps with test repeatability, as it eliminates dependability between tests (order). Use fixture factories for faster development and more correct test data; convert tests for test isolation and repeatability, take advantage of it by executing tests in parallel. A downside is that it is potentially slower (as you are not sharing data across tests).

[Slides](https://github.com/sjaensch/faster_end_to_end_tests_talk) (or [PDF](https://ep2017.europython.eu/media/conference/slides/fixture-factories-for-faster-end-to-end-tests.pdf)).


[![Rimini beach at night with the ferris wheel](https://shuttereye.org/images/01/01000b9b07c7898a_2000-2000.jpg)](https://shuttereye.org/goingout/2017_europython/IMG_6966.jpg/view/)


## Day five, Friday


Last day started with [Finding bugs for free: The magic of static analysis](https://ep2017.europython.eu/conference/talks/finding-bugs-for-free-the-magic-of-static-analysis) in which Mark Shannon talked about code analysis: finding facts about your code, without running it.

When you get to maintain a code base, you want to know where are the bugs, is this expensive to maintain; things you preferably want to get quantified by an automated code review.

What makes for good code analysis? It has to be flexible: can you extend it? Also, accurate: don't waste users time and insightful: find non-trivial things. This can be done for Python, but it's harder than for a statically-typed language, but can be more valuable as well.

So, what makes [lgtm](https://lgtm.com/) (automated code reviews service) flexible? It provides an object-oriented query language, in which queries can be simple, yet powerful. Also, a powerful library is provided.

Code is parsed into an abstract syntax tree (in contrast to concrete syntax tree), from which a control flow graph (CFG) is generated. By doing CFG splitting, you can deduct faulty code paths and drill down to bugs.


Next up was [Practical Debugging - Tips, Tricks and Ways to think](https://ep2017.europython.eu/conference/talks/practical-debugging-tips-tricks-and-ways-to-think) by Radoslav Georgiev, speaking about patterns and how stack traces are your friend.

He had a set of rules to live by as a developer, starting with the golden rule: if you find a bug, add a test for it (making it reproducible). Keep in mind tostay away from constant regression, and when debugging use ipdb/pdb (better than print of course) (by the way, `launch_ipdb_on_exception` as context manager, saves you a lot of 'cont, enter, cont, enter'), check tests, check input validation, check algorithms, check the system design and of course check your understanding of the problem space.

Another practical tip was to explain your problem to someone (the well-known rubber duck debugging).

He also proposed to do parallel debugging:

1. ask a question in StackOverflow
2. open GitHub issue
3. ask a co-worker for help
4. all of that while you are still debugging

However, I think that's not really a nice thing to do, because you are offloading your problem (possibly generating a lot of noise in the process). So, contribute your solutions back to the community by answering issues on StackOverlfow, writing on GitHub issues, opening PRs with bugfixes and examples, submitting documentation improvements, and... do a talk on a conference :)

- [https://github.com/RadoRado/EuroPython2017](https://github.com/RadoRado/EuroPython2017)
- [https://github.com/HackSoftware/](https://github.com/HackSoftware/)
- [hacksoft.io](https://hacksoft.io)


The 'Magic considered harmful' talk was cancelled, but there is [this recording of a previous version](https://www.youtube.com/watch?v=ZLfDpDG2fcU).


[Lessons learned in X years of parallel programming](https://ep2017.europython.eu/conference/talks/lessons-learned-in-x-years-of-parallel-programming) in which Michele Simionato told about lessons learned solving big problems.

Embarassingly parallel problems are common and may be more easy to solve than you think. It's generally not trivial though, which is to be expected. I recommend taking a look at [his (plain text) slides](https://ep2017.europython.eu/media/conference/slides/lessons-learned-in-x-years-of-parallel-programming.html).


Fergal Walsh had some intesting thoughts in [Rethinking how we build HTTP APIs](https://ep2017.europython.eu/conference/talks/rethinking-how-we-build-http-apis), in which he asked why API's need to be so rigid and REST, for example. One of his projects is [pico](https://github.com/fergalwalsh/pico), which is a really tiny framework to help you quickly create an API from a codebase without having to worry about correctness and such (REST).

It enables for easy interactive development (no need to set up all kinds of environment when you want to want to use ipython when developing for example). This is done by using decorators to fill function parameters that pico needs; this makes it possible to use and test pico from ipython and such.

Speaking about decorators, `wrapt` is a nice decorator library.


A great talk about the social aspects of technology an in IT specifically was [Overcoming Cognitive Bias](https://ep2017.europython.eu/conference/talks/overcoming-cognitive-bias) by Anna Martelli Ravenscroft (wife of Alex Martelli, writer of Python in a Nutshell; both authored Python Cookbook).

This is a subject that still needs a lot of attention and was a really good talk to raise awareness. If you ask 'are you a programmer?' to a woman at a conference, that's cognitive bias at work.

For more information, see this video: [Diversity as a dependency](http://pyvideo.org/pycon-us-2010/pycon-2010--diversity-as-a-dependency---49.html) and watch the ["Despicable machines: how computers can be assholes" talk](https://ep2017.europython.eu/conference/talks/despicable-machines-how-computers-can-be-assholes).



The lightning talks had a few interesting titbits:

- [A way of interacting with Jupyter notebooks](http://bit.ly/talk-to-jupyter).
- Run Python with warnings enabled. This tells about unclosed files and a lot more things. To do so, run `python3 -Wd -b` or for version 2: `python2 -Wd -t -3`.
- Some pointers when giving talks: structure beats slides (have 3-6 clear points); have a story; take-away value beats completeness (audience won't know what you left out anyway); speech_projects
- http://tinyurl.com/PerceptionMusic
- ssim for parsing flight schedule strings (in .sir files) to something usable: `pip install ssim`
- pyjok.es: `pip install pyjokes`
- [Manage GitHub by API instead of as a mere human with dothub](https://github.com/mariocj89/dothub).


[![Rimini yacht harbour](https://shuttereye.org/images/5f/5ff8861f3c1c164f_2000-2000.jpg)](https://shuttereye.org/goingout/2017_europython/IMG_7060.jpg/view/)
