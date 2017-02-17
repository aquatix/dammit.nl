Title: Disabling CSRF checking in Django (Rest Framework) to enable replay
Date: 2014-11-11 13:38:26
Slug: 20141111-disabling-csrf-checking-in-django-rest-framework-to-enable-replay
Location: Work
Authors: Michiel Scholten
Tags: olddammit

You have this interesting project, written in [Django](https://www.djangoproject.com/). Maybe even in the excellent [Django Rest Framework](http://www.django-rest-framework.org/). You want to run some tests on it to know how it will cope with load under stress. Or you just want to repeat a bunch of steps from the outside a lot of times.

Clicks are recorded, responses checked, scripts uploaded to some service that will emulate hundreds or thousands of visitors. A test run is done and you get all kinds of '401: CSRF Failed: CSRF token missing or incorrect.' messages and you can't finish your scenario's. Of course the first thing you do is open the project's settings.py and comment the lines

    MIDDLEWARE_CLASSES (
        #'django.middleware.csrf.CsrfViewMiddleware',

and

    TEMPLATE_CONTEXT_PROCESSORS (
        #'django.core.context_processors.csrf',

and

    CSRF_COOKIE_SECURE = True

after which you think you are done. You rerun the initial test and throw your coffee mug against the wall, as the checks are still being done.

No worries though, you can disable this on a per-request base with a decorator:

    from django.views.decorators.csrf import csrf_exempt
    @csrf_exempt
        def my_failing_view:
            return Httpresponse('Argl')

As it is kind of a hassle to add this to every single one of your views, only to be able to do these tests, just create this little piece of middleware:

    class DisableCSRF(object):
        def process_request(self, request):
                setattr(request, '_dont_enforce_csrf_checks', True)

Put this in a file `disable.py`, which you place in your `myapp`. Add a line to your settings.py:

    MIDDLEWARE_CLASSES = (
        myapp.disable.DisableCSRF,
    )

and you're done :)

[Some pointers](http://stackoverflow.com/questions/1650941/django-csrf-framework-cannot-be-disabled-and-is-breaking-my-site) and [ticket for Django Rest Framework](https://github.com/tomchristie/django-rest-framework/issues/957)