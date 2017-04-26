Title: On frameworks
Started: 2014-02-11
Date: 2017-04-26 15:52:00
Slug: on-frameworks
Location: Home
Authors: Michiel Scholten
Category: posts
Tags: dev
Status: draft

A while ago a friend of mine wrote that all frameworks suck. He was referring to [this article on PHP frameworks](http://) in which the main author of PHP was saying things along the same lines. My friend took things even further and said that all frameworks were useless, as none work the way you want to and you just end up fighting them. Only exception might be frameworks you write with your team.

I agree on a lot of frameworks having specific ways of doing things, so if you want to build features that are out of their main way of thinking, they might hamper you more than support you on your endeavour. However, for the big lines, you can see this coming and choose the base you want to build your application on. Choose wisely and you don't end up circumventing they ways it wants to do things.

PHP's frameworks tend to grow unwieldy fast because of the inherent clumsiness of the language itself. In other languages however, frameworks can be a lot more cooperative. I'm a fond user of Python and one of its main web stacks, Django. The latter has a great community that puts a *lot* of thought into how it's designing things to work. It's clean, properly tiered and supports you in a lot of things. Of course it has quirks, but not much fighting is being done by its plugins.

Here the same idea holds for choosing your environment; when you don't need the whole might of model-based automatically generated layers of functionality, don't choose it. Flask and similar will likely be a better match for your needs.

The idea of the only frameworks worth using are the ones you build yourself reeks a bit like the Not Invented Here syndrome. I love building little frameworks and have done so in the past and [am still doing so](https://github.com/aquatix/kontent-api). However, disregarding thousands upon thousands man hours of work and thought that went into a decent excisting framework for your language of choise might not be the wisest decision. In the end, I rather build new apps instead of endlessly thinkering with my architecture.

