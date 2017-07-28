Title: EuroPython 2017, part 2
Started: 2017-07-12 10:41:00
Modified: 2017-07-26 11:11:00
Date: 2017-07-14 20:17:00
Slug: europython2017-part2
Location: Rimini, Italy
Authors: Michiel Scholten
Category: conferences
Tags: python, europython, trip, conference
Image: TODO
Status: draft

[EuroPython 2017](https://ep2017.europython.eu/en/)

Photos of the whole conference are available at [the EuroPython 2017 flickr group](https://www.flickr.com/groups/3845891@N22/) and the [EuroPython 2017 website](https://ep2017.europython.eu/en/europython/photos/).

Videos (lifestream captures for now) are at [](https://www.youtube.com/playlist?list=PL8uoeex94UhEP1C94Fgdn3PdXitS8RtOV), more will go live later at the [EuroPython YouTube Channel](https://www.youtube.com/c/EuroPythonConference)


## Day three, Wednesday

We kicked off with the keynote ['If Ethics is not None'](https://ep2017.europython.eu/conference/talks/if-ethics-is-not-none) by Katharine Jarmul with a lot of food for thought.

(photo)

[Some good quotes were used](https://dammit.nl/computer-ethics-quotes.html), and the book [Cybernetics or Control and Communication in the Animal and the Machine](https://books.google.nl/books?id=NnM-uISyywAC&pg=PA27&dq=wiener+It+may+very+well+be+a+good+thing+for+humanity&sa=X&redir_esc=y#v=onepage&q=wiener%20It%20may%20very%20well%20be%20a%20good%20thing%20for%20humanity&f=false) by Norbert Wiener seems like a good read.


Next up the ['Mary had a little lambda' talk](https://ep2017.europython.eu/conference/talks/mary-had-a-little-lambda) was a really fun (re)introduction to lambda calculus. Yes, the calculus, not the lambda functions in Python, but Anjana Vakil continued with implementing the Church Numerals in lambda functions and we did some arithmetic with Python in Church Encoding. Fun and energetic talk, which I would have loved to have at university, instead of the long dry one I got there on the same material. [Lambda calculus](https://en.wikipedia.org/wiki/Lambda_calculus) was invented by Alonzo Church, starting in 1932, for 'expressing computation based on function abstraction and application using variable binding and substitution' and is Turing complete.


Lee Sheng's talk on ['Teeing up Python: Code Golf'](https://ep2017.europython.eu/conference/talks/teeing-up-python-code-golf) (check out the slides there) had a lot of good points about writing sane and readable code. For example, try using a default: `to_mail = my_contact.get("address", "UNKNOWN")` instead of checking if a key exists and then getting it from the list.

TODO: some more examples.


An interesting Big Data/distributed computing talk was [Realtime Distributed Computing At Scale (in pure Python!): Storm And Streamparse](https://ep2017.europython.eu/conference/talks/realtime-distributed-computing-at-scale-in-pure-python-storm-and-streamparse) by Alexander Lourenco from Parse.ly.

Storm is a distributed real-time computation system, which simplifies workers and queues.
- Streamparse is Pythonic Storm
- Nimbus and Storm UI

You can install the Storm environment from the Apache Storm site.

Streamparse is even easier, just use pip:

    pip install streamparse
    sparse quickstart
    sparse run



The [Infrastructure design patterns with Python, Buildbot, and Linux Containers](https://ep2017.europython.eu/conference/talks/infrastructure-design-patterns-with-python-buildbot-and-linux-containers) talk was a bit disappointing. It was basically David Liu's hobby project of (ab)using Dask (a distributed task system) for things it is not really intended, like remotely executing random scripts. - buildbot

I better could have gone to [How to make money with your Python Open-Source Project](https://ep2017.europython.eu/conference/talks/how-to-make-money-with-your-python-open-source-project) by Max Tepkeev, which would have been relevant for my own projects and probably for some of Sanoma's efforts too.




## Day four, Thursday


Kicking off with [Type Annotations in Python 3: Whats, whys & wows!](https://ep2017.europython.eu/conference/talks/type-annotations-in-python-3-whats-whys-wows) by Andreas Dewes, Thursday was in for a good line-up.

Executive summary: Python 3.6 is great, start using it. However, in older 3.x versions and also in 2.7, some nifty things can be done with hints about variable types.

- Gradual typing, where you add annotations to code where it makes sense (so you don't have to rewrite your complete codebase)
- Function annotations were the first step in Python 3.0 in 2006 (PEP 3107)
- In 3.5 Type Hints were introduced (including the theory and such)
- Python interpreter stores those annotations in __annotations__ and ignores it otherwise
- External tools like mypy and pycharm do the heavy lifting
- Deliberate choice to do it like this, so it can evolve; eventually we might want to have internal tools
- We loose Python 2 compatibility though, but then we can use type comments, which are backported to 2.7
- Third approach is stub files, ending with .pyi, which mypy will also look at, ignoring the .py file for type checking. This way, we can add only the annotations there. Feels a bit like writing a header file.
- Check the documentation of the typing module for more info, lots of usecases (new in 3.5)
- Slideshare: https://slideshare.com/japh44 -> https://www.slideshare.net/japh44/type-annotations-in-python-whats-whys-and-wows



11:20-12:05 Inside Airbnb: Visualizing data that includes geographic locations

https://ep2017.europython.eu/conference/talks/inside-airbnb-visualizing-data-that-includes-geographic-locations

Guillem Duran Ballester

- https://github.com/Guillem-db/Inside-Airbnb-EP17
- insideairbnb
- bokeh is a great library to work with Google Maps
- lat & lon, zoom and map_type
- shaolin for colour maps
- shapefiles with shapely
- holoviews and geoviews (matplotlib, bokeh and shapely as backends)
- datashader: plotting big data made easy; lots of jupyter notebooks as examples
- dynamic=True will recalculate the bins that datashader makes, making it nicer to look at when zooming in (with dynspread/datashade)
- one of the downsides of datashader is that when tweaking, it errors until you get everything right (for example in jupyter)
- http://geo.holoviews.org/Working_with_Bokeh.html
- integrating openstreetmaps with bokeh should be possible, speaker needs to look into it (but Google Maps is default)
- https://github.com/dsolanno/BarcelonaRentsStatus


12:10-12:55 Introduction to Nonparametric Bayesian Models

https://ep2017.europython.eu/conference/talks/introduction-to-non-parametric-models

Omar Gutiérrez

Some people just can't present. Seemed like an interesting subject, but could not concentrate on his really quiet rambling talk, instead playing with the Jupyter notebooks from the previous talks


14:00-14:30 An introduction to PyTorch & Autograd

https://ep2017.europython.eu/conference/talks/an-introduction-to-pytorch-autograd

Paul O'Grady

- tensor (ndarray) operations on the GPU (instead of being constrained to CPUs)
- pytorch is the new kid on the block
- follows Lua torch, with same underlying C libraries
- it's a define-by-run framework as opposed to define-and-run, leads to dynamic computation graphs, looks more Pythonic
- the native data format is tensors
- supports in-place adds and such (.add_() )
- Torch plays well with numpy and it can bridge back and forth (for example having matrix operations and getting a tensor back)
- you can reshape tensors using views
- tensor computation can be moved to and from GPU (CUDA)
- variables through torch.autograd package


14:35-15:05 Developing elegant workflows in Python code with Apache Airflow

https://ep2017.europython.eu/conference/talks/developing-elegant-workflows-in-python-code-with-apache-airflow

Michał Karzyński

- definition of a workflow:
  - sequence of tasks
  - started on a schedule or triggered by an event
  - frequently used to handle big data processing pipelines
- Apache Airflow is Open Source, based on Flask, using Celery
- A flow is a Directed Acyclic Graph (DAG)
- Operator is a single task, which can be retried automatically, should be idempotent and is a Python task with an execute method
- xcom is a means of communication between task instances
  - saved in database as a pickled object
  - best suited for small objects
- Introductory Airflow tutorial on speaker's weblog: http://michal.karzynski.pl/blog/2017/03/19/developing-workflows-with-apache-airflow/


15:45-16:15 Inspect (Or Gadget)

https://ep2017.europython.eu/conference/talks/inspect-or-gadget

Hugues Lerebours , Renaud Bauvin

- library: inspect, https://docs.python.org/3/library/inspect.html
- provides quite some extra functions apart from the already useful Python buildins
- demo consists of a piece of code that checks if docstrings are up-to-date, also validating against documented types


16:20-16:50 Fixture factories for faster end-to-end tests

https://ep2017.europython.eu/conference/talks/fixture-factories-for-faster-end-to-end-tests

Stephan Jaensch

- end-to-end integration, replicating production as much as possible (above 'regular' integration tests)
- slow, most expensive tests
- pyramid, swagger, openapi, sqlalchemy
- lots of db setup on all the components, lots of SQL scripts, hard to write, maintain
- taking inspiration from Django
- make sure data is logically correct
- pytest
- why not use models? No FK checking used in this setup, so cannot use the PK and FK's
- helps with test repeatability, as it eliminates dependability between tests (order)
- use fixture factories for faster development and more correct test data
- convert tests for test isolation and repeatability
- take advantage of it by executing tests in parallel
- https://github.com/sjaensch/faster_end_to_end_tests_talk



## Day five, Friday


10:30-11:15 Finding bugs for free: The magic of static analysis.

https://ep2017.europython.eu/conference/talks/finding-bugs-for-free-the-magic-of-static-analysis

Mark Shannon

- code analysis is finding facts about your code, without running it
- where are the bugs, is this expensive to maintain
- automated code review
- what makes for good code analysis?
  - flexible: can you extend it?
  - accurate: don't waste users time
  - insightful: find non-trivial things
- this can be done for Python, but it's harder than for a statically-typed language, but can be more valuable as well
- what makes lgtm flexible?
  - object-oriented query language
  - queries can be simple, yet powerful
  - powerful library is provided
- abstract syntax tree (in contrast to concrete syntax tree)
- control flow graph (CFG)
- CFG splitting


11:20-12:05 Practical Debugging - Tips, Tricks and Ways to think

https://ep2017.europython.eu/conference/talks/practical-debugging-tips-tricks-and-ways-to-think

Radoslav Georgiev

- patterns
- stack traces are your friend
- golden rule: if you find a bug, add a test for it (making it reproducible)
- stay away from constant regression
- ipdb/pdb (better than print of course)
- launch_ipdb_on_exception as context manager, saves you a lot of 'cont, <enter>, cont, <enter>'
- check tests
- check input validation
- check algorithms
- check system design
- check your understanding of the problem space
- practical tips:
  - explain your problem to someone (rubber duck debugging)
  - parallel debugging:
    1) ask a question in SO
    2) open GitHub issue
    3) ask a co-worker for help
    4) all of that while you are still debugging
  - the latter is not really nice, because you are offloading your problem. So, contribute your solutions back to the community by answering issues on SO, writing on GH issues, opening PRs with bugfixes and examples, documentation improvements
  - do talk on a conference
- https://github.com/RadoRado/EuroPython2017
- https://github.com/HackSoftware/
- hacksoft.io


## 12:10 Magic considered harmful

Cancelled, but https://m.youtube.com/watch?v=ZLfDpDG2fcU


## 12:10-12:55 Lessons learned in X years of parallel programming

https://ep2017.europython.eu/conference/talks/lessons-learned-in-x-years-of-parallel-programming

Michele Simionato

- embarassingly parallel problems are common and may be more easy to solve than you think
- generally not trivial though
- slides in 20170714_parallel_programming_slides.txt


14:35-15:05 Rethinking how we build HTTP APIs

https://ep2017.europython.eu/conference/talks/rethinking-how-we-build-http-apis

Fergal Walsh

- https://github.com/fergalwalsh/pico
- easy interactive development
- use ipython when developing
- decorators to fill function parameters that pico needs; makes it possible to use and test pico from ipython and such
- created to quickly create an API without having to worry about correctness and such (REST)
- wrapt is a nice decorator library


A great talk about the social aspects of technology an in IT specifically was [Overcoming Cognitive Bias](https://ep2017.europython.eu/conference/talks/overcoming-cognitive-bias) by Anna Martelli Ravenscroft (wife of Alex Martelli, writer of Python in a Nutshell; both authored Python Cookbook).

This is a subject that still needs a lot of attention

- if you ask 'are you a programmer?' to a woman at a conference, that's cognitive bias at work
- really good talk to raise awareness
- talk on youtube: diversity as a dependency
- watch the ["Despicable machines: how computers can be assholes" talk](https://ep2017.europython.eu/conference/talks/despicable-machines-how-computers-can-be-assholes).



Lightning talks

- bit.ly/talk-to-jupyter
- run Python with warnings enabled
  - tells about unclosed files
  - a lot more things
  - python3 -Wd -b
  - python2 -Wd -t -3
- giving talks:
  - structure beats slides (have 3-6 clear points)
  - story
  - take-away value beats completeness (audience won't know what you left out anyway)
  - speech_projects
- http://tinyurl.com/PerceptionMusic
- ssim for parsing flight schedule strings (in .sir files) to something usable
  - pip install ssim
- pyjok.es
  - pip install pyjokes

[Manage GitHub by API instead of as a mere human with dothub](https://github.com/mariocj89/dothub).

