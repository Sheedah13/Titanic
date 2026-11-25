from flask import Flask, render_template, request
import pickle
import pandas as pd

app=Flask(__name__)
model= pickle.load(open("titanic_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = {
    "Pclass": [int(request.form["pclass"])],
    "Sex": [request.form["sex"]],
    "Age": [float(request.form["age"])],
    "Sibsp": [int(request.form["sibsp"])],
    "Parch": [int(request.form["parch"])],
    "Fare": [float(request.form["fare"])],
    "Embarked": [request.form["embarked"]]
    }

    df = pd.DataFrame(data)
    prediction = model.predict(df)[0]
    result = "Survived" if prediction == 1 else "Did Not Survive" 
    return render_temlate("result.html",
    pclass=data["Pclass"][0],
    sex=data["Sex"][0],
    age=data["Age"][0],
    result=result)

if __name__=="__main__":
    app.run(debug=True)
    