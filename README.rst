Django action logger
====================

Installation
------------

* Install this package into virtual environment of your project.
* Add the following lines into settings.py::

    INSTALLED_APPS += ('mlogger',)
    MIDDLEWARE_CLASSES += ('mlogger.middleware.CurrentUserMiddleware',)

Usage
-----

* Add into your models.py::

    from mlogger.models import logging_postsave, logging_postdelete

* Then connect signals to logging handlers::

    models.signals.post_save.connect(logging_postsave, sender=YourModelName)
    models.signals.post_delete.connect(logging_postdelete, sender=YourModelName)

* Get changes::

    from mlogger.models import Log
    Log.objects.all()

Conclusion
----------

It's pretty easy!
