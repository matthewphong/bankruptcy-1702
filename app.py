#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:58:31 2022

@author: matthew
"""

from flask import Flask
app = Flask(__name__)

from flask import request, render_template
from keras.models import load_model

@app.route("/", methods =["GET","POST"])
def index():
    if request.method == "POST":
        #NPTA= request.form.get("NPTA")
        #TLTA= request.form.get("TLTA")
        #WCTA= request.form.get("WCTA")
        #print(NPTA,TLTA,WCTA)
        #model=load_model("bankruptcy")
        #pred= model.predict([[float(NPTA),float(TLTA),float(WCTA)]])
        #s = "The predicted bankruptcy score is: " + str(pred)
        return(render_template("index.html", result="1"))
    else:
        return(render_template("index.html", result="2"))

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=int("1111"))