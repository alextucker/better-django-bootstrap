Better Django Bootstrap
=======================

Starting a new Django project can be a pain. Gotta get static files working, gotta 
get stuff ready for test deploys. 

Setup
-----

1. Set a new `SECRET_KEY` in `project/settings.py` (TODO: Create a new manage.py command to automate this)
2. Edit the Database settings in `.env` to best suit your needs

Running
-------

This project comes bundled with a simple `Procfile` and `.env` so it plays nice with tools like
[Foreman](https://github.com/ddollar/foreman) or [honcho](https://github.com/nickstenning/honcho) 
out of the box. This also makes deploying to a service like [Heroku](www.heroku.com) super 
simple.

1. To start your local webserver you can:

```
foreman start
```

or

```
honcho start
```
