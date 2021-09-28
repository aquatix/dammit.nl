Title: RQ Python queuing system
Started: 2021-09-28 19:40:57
Date: 2021-09-28 19:40:57
Slug: rq-queuing
Location: Home
Authors: Michiel Scholten
Status: published
Category: responses
Tags: dev, energy, linux, tech, work
Link: https://python-rq.org/

You might be acquainted with the [Celery Distributed Task Queue](https://docs.celeryproject.org/en/stable/), which is a proven way to process vast amounts of messages. Messages containing tasks for your software stack to eventually finish doing, for example.

However, Celery is slightly cumbersome to set up (no rocket surgery, but the RabbitMQ message broker that generally is advisable to use in concert can be hairy). Enter the [Redis](https://redis.io/) memory DB and [RQ](https://python-rq.org/).

> RQ (Redis Queue) is a simple Python library for queueing jobs and processing them in the background with workers. It is backed by Redis and it is designed to have a low barrier to entry. It can be integrated in your web stack easily.

Ensuring Redis to have decent [persistence](https://redis.io/topics/persistence) is key of course, as you likely do not want to lose messages if they contain jobs that really need to be done. Enabling RDB + AOF will take care of that, so be sure to set those in the Redis configuration file.

Myself, I've been enjoying (!) myself implementing background tasks at work. It makes scaling of course so much easier and better, and RQ might say it's simple, but it's pretty complete with things like the FailedJobRegistry, where information about jobs that somehow did not complete (e.g., crashed for example) is kept, including stack traces. Pretty nifty, and helpful to have in our dashboard.

Anyways, recommended for when you're looking into making your (Python) software a bit more asynchronous, and/or you want to spread the load over multiple nodes.
