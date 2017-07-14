Title: EuroPython 2017, part 2
Started: 2017-07-12 10:41:00
Modified: 2017-07-13 10:47:00
Date: 2017-07-14 20:17:00
Slug: europython2017-part2
Location: Rimini, Italy
Authors: Michiel Scholten
Category: conferences
Tags: python, europython, trip, conference
Image: TODO
Status: draft

[EuroPython 2017](https://ep2017.europython.eu/en/)

## Day three, Wednesday


## 09:00-10:00 If Ethics is not None

https://ep2017.europython.eu/conference/talks/if-ethics-is-not-none

Katharine Jarmul

(photo)

Lots of good thoughts.

Copied and typed some to:
https://dammit.nl/computer-ethics-quotes.html

https://books.google.it/books?id=NnM-uISyywAC&lpg=PA27&ots=xgTxeBeiHn&dq=wiener%20It%20may%20very%20well%20be%20a%20good%20thing%20for%20humanity&pg=PA27#v=onepage&q&f=false



## 10:30-11:15 Mary had a little lambda

https://ep2017.europython.eu/conference/talks/mary-had-a-little-lambda

Anjana Vakil

- lambda calculus, of course invented by Alonzo Church, starting in 1932
- fun talk about doing lambda calculus, Church Numerals and Encoding, corresponding arithmetic in Python
- feels like being at the university again, but a lot more fun, great talk by an energetic Anjana


## 12:10-12:40 Teeing up Python: Code Golf

https://ep2017.europython.eu/conference/talks/teeing-up-python-code-golf

Lee Sheng

(really would like to have the slides)

- try using a default: to_mail = my_contact.get("address", "UNKNOWN") (instead of checking if a key exists and then getting it from the list)


## Lunch



## 15:45-16:15 Realtime Distributed Computing At Scale (in pure Python!): Storm And Streamparse

https://ep2017.europython.eu/conference/talks/realtime-distributed-computing-at-scale-in-pure-python-storm-and-streamparse

Alexander Lourenco

- Parse.ly
- Storm is a distributed real-time computation system, which simplifies workers and queues.
- Streamparse is Pythonic Storm
- Nimbus and Storm UI
- Install Storm env from Apache Storm site
- pip install streamparse
- sparse quickstart
- sparse run



## 16:20-16:50 Infrastructure design patterns with Python, Buildbot, and Linux Containers

https://ep2017.europython.eu/conference/talks/infrastructure-design-patterns-with-python-buildbot-and-linux-containers

David Liu

- Dask (distributed task system)
- buildbot

Abuse all the tools :)

Better could have gone to:

## 16:20-16:50 How to make money with your Python Open-Source Project

https://ep2017.europython.eu/conference/talks/how-to-make-money-with-your-python-open-source-project

Max Tepkeev

(skipped, but would've been better)





## Day four, Thursday


## 10:30-11:15 Type Annotations in Python 3: Whats, whys & wows!

https://ep2017.europython.eu/conference/talks/type-annotations-in-python-3-whats-whys-wows

Andreas Dewes

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



## 11:20-12:05 Inside Airbnb: Visualizing data that includes geographic locations

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


## 12:10-12:55 Introduction to Nonparametric Bayesian Models

https://ep2017.europython.eu/conference/talks/introduction-to-non-parametric-models

Omar Gutiérrez

Some people just can't present. Seemed like an interesting subject, but could not concentrate on his really quiet rambling talk, instead playing with the Jupyter notebooks from the previous talks


