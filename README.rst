Introduction
============

django-email-helper is the Django-related reusable app provides the ability to send multipart emails and store them in a database.


Installation
============

1. Install django-email-helper using ``pip`` or ``easy_install``::

    $ pip install django-email-helper
    or
    $ easy_install django-email-helper

2. Add the ``'email_helper'`` application to the ``INSTALLED_APPS`` setting of your Django project ``settings.py`` file::

    INSTALLED_APPS = (
        ...
        'email_helper',
        ...
    )


Usage
=====

There are only one function for sending email in the ``email_helper`` module:

  * ``send_email``
