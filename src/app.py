from flask import Flask, request, render_template
from pickle import load

app = Flask(__name__)
with open("../models/random_forest_classifier_default_42.sav", 'rb') as f:
    model = load(f)

@app.route("/", methods = ["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        
        Pregnancies = float(request.form["val1"])
        Glucose = float(request.form["val2"])
        BloodPressure = float(request.form["val3"])
        BMI = float(request.form["val4"])
        DiabetesPedigreeFunction = float(request.form["val5"])
        Age = float(request.form["val6"])
        
        data = [[Pregnancies, Glucose, BloodPressure, BMI, DiabetesPedigreeFunction, Age]]
        prediction = model.predict(data)
    
    return render_template("index.html", prediction = prediction)


    # URL for the Web App
    # https://diabetes-flask.onrender.com/