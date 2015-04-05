#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
#from imdb import IMDb
from random import randint
from google.appengine.ext import ndb


import jinja2
import random


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


#x=randint(0,3)
#chances=3;
#movie = ia.search_movie(list[x])
#movie = movie[0]
#movie = ia.get_movie(movie.movieID)
#ques = movie.get('plot outline')

w=""
strike=""
ntf=""
wa=0
cg=[]
flag=True
word=""
endgame=False

def Main():
    global word
    global endgame
    global w
    global strike
    global ntf
    global wa
    global cg
    global plot
    endgame=False
    cg=[]
    ntf="Which Movies plot is this?"
    wa=0
    words=["Boxtrolls","Avengers","Batman"]
    plots=["A young orphaned boy raised by underground cave-dwelling trash collectors tries to save his friends",
           "Earth's mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity.",
           "The Dark Knight of Gotham City begins his war on crime with his first major enemy being the clownishly homicidal Joker."]
    x=randint(0,2)
    word=words[x].upper()
    plot=plots[x].upper()
    w=plot
    strike="Lives"

class MainHandler(webapp2.RequestHandler):
    def get(self):
        global flag
        if flag:
            Main()
            flag=False
        abc="Movie Plotx"
        template_values={'abc':abc,'w':w,'strike':strike,'ntf':ntf,'word':word}

        template = JINJA_ENVIRONMENT.get_template('web/index.html')
        self.response.write(template.render(template_values))

def getguess(x):
    if x.isalpha()==False:
         global ntf
         ntf="Guess the movie"
         return False
    else:
        return True

def init(b,d):
    global w
    w=""
    for a in b:
        wo=False
        for c in d:
            if c==a:
                wo=True
        if wo:
            w+=a+" "
        else:
            w+="_ "

def showstat(d):
    i=0
    global strike
    strike=""
    b=['<3','<3','<3']
    for a in b:
        if i<d:
            i=i+1
            strike+="/"
        else:
            strike+=a


def checkwin(b,d):
    if(b.lower()==d.lower()):
        return True
    else:
        return False


class CharGuess(webapp2.RequestHandler):
    def post(self):
        global cg
        global word
        global ntf
        global wa
        global endgame
        guess=self.request.get('content').upper()
        if not endgame:
            if getguess(guess):
                if checkwin(word,guess):
                    ntf="Well done!"
                    endgame=True
                else:
                    wa=wa+1
                    ntf="Incorrect"
                    showstat(wa)
                    if wa==3:
                        ntf="Sorry! The answer was "+word
                        endgame = True        
        else:
            ntf="Click reset"





        self.redirect('/')


class Reset(webapp2.RequestHandler):
    def post(self):
        global flag
        flag=True
        self.redirect('/')

app=webapp2.WSGIApplication([
    ('/',MainHandler),
    ('/guess',CharGuess),
    ('/reset',Reset)
], debug=True)
