# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 16:20:44 2021

@author: Mustafa Hasnain
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')

def dummyApi():
    return ("Hello World")

if __name__=="__main__":
    app.run(debug=True)