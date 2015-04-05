# plotwist
A small text based game. Made using python and Google App Engine.
Uses basic templating library Jinja2. 

Initially i planned to fetch data dynamically using IMDbPY but GAE doesnt support this library yet.
Here is the code for the same.

from imdb import IMDb
from random import randint
ia = IMDb()
x=randint(0,3)
chances=3;
list=["Kingsman","Birdman","Batman","Insurgent"]
movie = ia.search_movie(list[x])
movie = movie[0]
movie = ia.get_movie(movie.movieID)
description = movie.get('plot outline')
print description
if(chances>0):
    for i in range(0,3):
        guess=raw_input();
        if(guess.lower()==list[x].lower()):
            print "CORRECT!"
            break
        else:
            print "INCORRECT!"
            chances=chances-1
else:
    print "No more lives left!"

If in future they do support this library. The above code can be used directly. 
