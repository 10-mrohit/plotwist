# plotwist
A small text based game. Made using python and Google App Engine.
Uses basic templating library Jinja2. 

Initially i planned to fetch data dynamically using IMDbPY but GAE doesnt support this library yet.
Here is a code snippet of the same:

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


If in future they do support this library. The above code can be used directly. 
