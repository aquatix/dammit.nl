Title: Infrastructure automation: hype
Started: 2022-03-01 14:24:47
Date: 2022-03-01 14:24:47
Slug: infrastructure-automation-hype
Location: Home
Authors: Michiel Scholten
Status: published
Category: projects
Tags: dev, energy, hosting, linux, python, tech, work

This weekend we did a big migration of our stack at work to a new data centre and I am stoked about how our applications and their virtual machines are set up now. Quite a bunch is already automated and having a decent base image is such a nice thing to have.

One of the parts where I want to improve a bit more, is in the area of our CI/CD. Currently, some parts are still manual, which is of course not optimal. I want to start using [Fabric](https://www.fabfile.org/) which is just super useful to do remote commands. A step further would be using something like [pyinfra](https://pyinfra.com/) which is an alternative to [ansible](https://www.ansible.com/) and is taking care of the state of the nodes too, by describing what you need them to function. For example [this article: How to Deploy Python App on a Remote Server with Pyinfra](https://python.plainenglish.io/deploy-your-python-app-on-remote-server-with-pyinfra-42753ada37ca) has some examples of how to do just that, and being some kind of combination of Fabric and Ansible to try to combine the best of both worlds.

But maybe I should just play around with [this Fabric2 Example](https://github.com/chrisgo/fabric2-example) first. Enough food for play^H^H^H^Hthoughts :)
