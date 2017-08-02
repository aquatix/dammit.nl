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
- The [slides are on Slideshare](https://www.slideshare.net/japh44/type-annotations-in-python-whats-whys-and-wows).



[Inside Airbnb: Visualizing data that includes geographic locations](https://ep2017.europython.eu/conference/talks/inside-airbnb-visualizing-data-that-includes-geographic-locations) by Guillem Duran Ballester provided some interesting visualisations of Airbnb locations (specifically Barcelona and Mallorca). By doing so, he introduced quite some useful tooling for drawing maps, drawing shapes on them (for example for area's to aggregate datapoints to densities) and various shaders. Everything was demoed through [Jupyter notebooks](https://github.com/Guillem-db/Inside-Airbnb-EP17). Data from [insideairbnb](http://insideairbnb.com/) was used.

Some take-aways:

- bokeh is a great library to work with Google Maps (take a look at lat & lon, zoom and map_type)
- shaolin for colour maps
- shapefiles with shapely (for drawing overlays on the map, for example to colour an area of a town)
- holoviews and geoviews (matplotlib, bokeh and shapely as backends)
- datashader: plotting big data made easy; lots of jupyter notebooks as examples
- dynamic=True will recalculate the bins that datashader makes, making it nicer to look at when zooming in (with dynspread/datashade)
- one of the downsides of datashader is that when tweaking, it errors until you get everything right (for example in jupyter)
- http://geo.holoviews.org/Working_with_Bokeh.html
- integrating openstreetmaps with bokeh should be possible, speaker needs to look into it (but Google Maps is default)
- [The code of the rent status of Airbnb venues](https://github.com/dsolanno/BarcelonaRentsStatus).


[Introduction to Nonparametric Bayesian Models](https://ep2017.europython.eu/conference/talks/introduction-to-non-parametric-models) by Omar Gutiérrez.

Some people just can't present. Seemed like an interesting subject, but could not concentrate on his really quiet rambling talk, instead playing with the Jupyter notebooks from the previous talks. TODO: keep this in?


The [An introduction to PyTorch & Autograd](https://ep2017.europython.eu/conference/talks/an-introduction-to-pytorch-autograd) talk from Paul O'Grady provided some tools to do deep learning with Python.

Tensor (ndarray) operations on the GPU (instead of being constrained to CPUs) are a lot faster.

`pytorch` is the new kid on the block. It follows Lua torch, with same underlying C libraries and is a define-by-run framework as opposed to define-and-run, leads to dynamic computation graphs, looks more Pythonic. The native data format is [tensors](https://en.wikipedia.org/wiki/Tensor), which is a bit different than what we are used to, but makes sense in these computations. Torch supports in-place adds and such (.add_() ) and plays well with numpy; it can bridge back and forth (for example having matrix operations and getting a tensor back). To get more insight in the data, you can reshape tensors using views. One of the nice optimalisation things is that tensor computation can be moved to and from GPU (CUDA). Support for variables is added through the [torch.autograd package](http://pytorch.org/docs/master/autograd.html).


Next up was [Developing elegant workflows in Python code with Apache Airflow](https://ep2017.europython.eu/conference/talks/developing-elegant-workflows-in-python-code-with-apache-airflow) where Michał Karzyński talked about creating data flows with Airflow.

- definition of a workflow:
  - sequence of tasks
  - started on a schedule or triggered by an event
  - frequently used to handle big data processing pipelines
- Apache Airflow is Open Source, based on Flask, using Celery
- A flow is a Directed Acyclic Graph (DAG)
- Operator is a single task, which can be retried automatically, should be idempotent and is a Python task with an execute method
- xcom is a means of communication between task instances; a task is saved in the database as a pickled object; it is best suited for small objects
- Introductory Airflow tutorial on speaker's weblog: http://michal.karzynski.pl/blog/2017/03/19/developing-workflows-with-apache-airflow/


[Inspect (Or Gadget)](https://ep2017.europython.eu/conference/talks/inspect-or-gadget) by Hugues Lerebours and Renaud Bauvin

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
- why not use models? No foreing key (FK) checking used in this setup, so cannot use the PK and FK's
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

[Manage GitHub by API instead of as a mere human with dothub](https://github.com/mariocj89/dothub).

