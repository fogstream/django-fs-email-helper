# coding=utf-8

from setuptools import setup


setup(
    name='django-email-helper',
    version = __import__('email_helper').__version__,
    author = 'Yuri Lya',
    author_email = 'yuri.lya@fogstream.ru',
    description = 'The Django-related reusable app provides the ability to send multipart emails and store them in a database.',
    long_description = open('README.rst').read(),
    url = 'https://bitbucket.org/fogstream/django-email-helper',
    packages = ['email_helper'],
    zip_safe = False,
    include_package_data = True,
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
        "Topic :: Communications :: Email",
    ]
)
