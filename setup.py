# coding=utf-8

from setuptools import setup


setup(
    name='django-email-helper',
    version = '0.1',
    author = 'Yuri Lya',
    author_email = 'yuri.lya@fogstream.ru',
    maintainer = 'Fogstream'
    maintainer_email = 'org@fogstream.ru'
    description = 'The Django-related reusable app provides the ability to send multipart emails and store them in a database.',
    url = 'https://bitbucket.org/fogstream/django-email-helper',
    packages = ['email_helper'],
)
