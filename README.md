# challenge-flask-api

## What

We create our first API with Flask, we use Docker to create the image and we depolye it on [Heroku](https://www.heroku.com/).

## Why

We do this exercise to be able to deploye a API and run on a web service. We choose Heroku because it's free.

## When

During becode training. It takes us around 3 days (24 december 2020, 4 and 5 january 2021)

## How

First, you have to create your API on your computer, for this, we use flask. To install flask you just need to write this on your terminal :
`pip install Flask`
Then you have to import flask with `from flask import Flask`. After that, we mentioned with `@app.route('url_route')` decorator for each page of our website. We have 4 pages: home page, status, login and predict (the only one with POST request is login, others are GET request). We create our website with HTML and CSS files and we renders with our api.py file. We also have form.py which need to install flask WTF (you have to install with `pip install Flask-WTF`) which will create our login form and verify if it's fitting what we expected. It will also hide our password.
After testing and doing our design we create a Dockerfile and create the image then we deploy the API on Heroku.
To deploy On Heroku, first we need to install where our application is (you can find it on documentation on the website). After that, we do these following operations:

    /heroku conatiner:login
     heroku create
     heroku container:push web
     heroku container:push web --app name-of-your-app
     heroku container:release web
     heroku open
     
After these operation, this will open a page on your browser and you can navigate on the website that you've just created.
Important: Do not forget to create a profile with just these codes `web:python api.py`and the port and host on your man in run method.

## Who

[Ebubekir Kocadag](https://github.com/EbubekirKocadag), junior AI developer
  
