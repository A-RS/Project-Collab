# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
# from flask_pymongo import PyMongo
# -- Initialization section --
app = Flask(__name__)

@app.route('/')
@app.route('/index', methods =["GET","POST"])
def index():
    return render_template('index.html')

@app.route('/quiz', methods =["GET","POST"])
def quiz ():
    return render_template('quiz.html')


@app.route('/results', methods =["GET","POST"])
def results ():
    if request.method == "POST":
        print(dict(request.form))
        density= request.form["density"]
        porocity= request.form["porosity"]
        hair_type=request.form["type"]
        hair_condition= request.form["condition"]
        hair_p ={"denisty":density,"porocity":porocity, "hair_type":hair_type, "hair_condition":hair_condition}
        if  hair_condition== "dry" and porocity == "low" and hair_type.startswith("4") and density == "high":
            return render_template("DL4H.html",time=datetime.now()) 
    # dry, porocity(low),type 4, density(high) HTML: DL4H.html
        elif hair_condition== "dry" and porocity == "medium" and hair_type.startswith("4") and density == "high":
            return render_template (" DM4H.html",time=datetime.now())
    # dry, porocity(medium),type 4, density(high) HTML: DM4H.html
        elif hair_condition== "dry" and porocity == "high" and hair_type.startswith("4") and density == "high": 
            return render_template (" DH4H.html")
    # dry, porocity(high),type 4, density(high) HTML: DH4H.html
        elif hair_condition== "dry" and porocity == "low" and hair_type.startswith("4") and density == "medium": 
            return render_template ("DL4M.html")
    # dry, low(porocity),type 4, density(medium) HTML: DL4M.html
        elif hair_condition== "dry" and porocity == "medium" and hair_type.startswith("4") and density == "medium": 
            return render_template ("DM4M.html")
    # dry, medium(porocity),type 4, density(medium) HTML: DM4M.html
        elif hair_condition== "dry" and porocity == "high" and hair_type.startswith("4") and density == "medium": 
            return render_template ("DH4M.html") 
    # dry, high(porocity),type 4, density(medium) HTML: DH4M.html
        elif hair_condition == "dry" and porocity == "low" and hair_type.startswith("4") and density == "low": 
            return render_template (" DL4L.html")
    # dry, low(porocity),type 4, density(low) HTML: DL4L.html
        elif hair_condition== "dry" and porocity == "medium" and hair_type.startswith("4") and density == "low": 
            return render_template ("DM4L.html")
    # dry, low(porocity),type 4, density(medium) HTML: DM4L.html
        elif hair_condition== "dry" and porocity == "high" and hair_type.startswith("4") and density == "low": 
            return render_template ("DH4L.html")
    # dry, high(porocity),type 4, density(low) HTML: DH4L.html
# //////////////////////////-type4 damaged-//////////////////////////////////////////////////////////////////////////////////////////////////
        if  hair_condition== "damaged" and porocity == "low" and hair_type.startswith("4") and density == "high":
            return render_template("DaL4H.html",time=datetime.now() ) 
        # damaged, porocity(low),type 4, density(high) HTML: DaL4H.html
        elif hair_condition== "damaged" and porocity == "medium" and hair_type.startswith("4") and density == "high":
            return render_template (" DaM4H.html")
        # damaged, porocity(medium),type 4, density(high) HTML: DaM4H.html
        elif hair_condition== "damaged" and porocity == "high" and hair_type.startswith("4") and density == "high": 
            return render_template (" DaH4H.html")
        # damaged, porocity(high),type 4, density(high) HTML: DaH4H.html
        elif hair_condition== "damaged" and porocity == "low" and hair_type.startswith("4") and density == "medium": 
            return render_template ("DaL4M.html")
        # damaged, low(porocity),type 4, density(medium) HTML: DaL4M.html
        elif hair_condition== "damaged" and porocity == "medium" and hair_type.startswith("4") and density == "medium": 
            return render_template ("DaM4M.html")
        # damaged, medium(porocity),type 4, density(medium) HTML: DaM4M.html
        elif hair_condition== "damaged" and porocity == "high" and hair_type.startswith("4") and density == "medium": 
            return render_template ("DH4M.html") 
        # damaged, high(porocity),type 4, density(medium) HTML: DaH4M.html
        elif hair_condition == "damaged" and porocity == "low" and hair_type.startswith("4") and density == "low": 
            return render_template (" DaL4L.html")
        # damaged, low(porocity),type 4, density(low) HTML: DaL4L.html
        elif hair_condition== "dry" and porocity == "medium" and hair_type.startswith("4") and density == "low": 
            return render_template ("DaM4L.html")
        # damaged, low(porocity),type 4, density(medium) HTML: DaM4L.html
        elif hair_condition== "damaged" and porocity == "high" and hair_type.startswith("4") and density == "low": 
            return render_template ("DaH4L.html")
        # damaged, high(porocity),type 4, density(low) HTML: DaH4L.html
# ///////////////////////////////////////////////////////////////////////Type 4 brittle/////////////////////////////////////////////////////////////////////////
        if  hair_condition== "brittle" and porocity == "low" and hair_type.startswith("4") and density == "high":
            return render_template("BL4H.html",time=datetime.now()) 
        # brittle, porocity(low),type 4, density(high) HTML: BL4H.html
        elif hair_condition== "brittle" and porocity == "medium" and hair_type.startswith("4") and density == "high":
            return render_template ("BM4H.html",time=datetime.now())
        # brittle, porocity(medium),type 4, density(high) HTML: BM4H.html
        elif hair_condition== "brittle" and porocity == "high" and hair_type.startswith("4") and density == "high": 
            return render_template ("BH4H.html")
        # brittle, porocity(high),type 4, density(high) HTML: BH4H.html
        elif hair_condition== "brittle" and porocity == "low" and hair_type.startswith("4") and density == "medium": 
            return render_template ("BL4M.html")
        # brittle, low(porocity),type 4, density(medium) HTML: BL4M.html
        elif hair_condition== "brittle" and porocity == "medium" and hair_type.startswith("4") and density == "medium": 
            return render_template ("BM4M.html")
        # brittle, medium(porocity),type 4, density(medium) HTML: BM4M.html
        elif hair_condition== "brittle" and porocity == "high" and hair_type.startswith("4") and density == "medium": 
            return render_template ("BH4M.html") 
        # brittle, high(porocity),type 4, density(medium) HTML: BH4M.html
        elif hair_condition == "brittle" and porocity == "low" and hair_type.startswith("4") and density == "low": 
            return render_template (" BL4L.html")
        # brittle, low(porocity),type 4, density(low) HTML: BL4L.html
        elif hair_condition== "brittle" and porocity == "medium" and hair_type.startswith("4") and density == "low": 
            return render_template ("BM4L.html")
        # brittle, low(porocity),type 4, density(medium) HTML: BM4L.html
        elif hair_condition== "brittle" and porocity == "high" and hair_type.startswith("4") and density == "low": 
            return render_template ("BH4L.html")
        # brittle, high(porocity),type 4, density(low) HTML: BH4L.html
      


