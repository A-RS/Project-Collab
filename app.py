# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request

# from flask_pymongo import PyMongo
# -- Initialization section --
app = Flask(__name__)


# name of database
# app.config['MONGO_DBNAME'] = 'database-name'

# URI of database
# app.config['MONGO_URI'] = 'mongo-uri'

# mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index', methods =["GET","POST"])
def index():
    return render_template('index.html')

@app.route('/quiz', methods =["GET","POST"])
def quiz ():
    return render_template('quiz.html')


@app.route('/results', methods =["GET","POST"])
def results ():
    if request.form['/results']=="POST":
        density= request.form["density"]
        porocity= request.form["porosity"]
        hair_type=request.form["type"]
        hair_condition= request.form["condition"]
        if density == request.form["dry"] and hair_type == request.form["4a"]:
            return render_template("results.html")
            print("hair")

        






