from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("Loan_Model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    income = float(request.form["income"])
    credit_score = float(request.form["credit_score"])
    loan_amount = float(request.form["loan_amount"])
    years_employed = float(request.form["years_employed"])
    points = float(request.form["points"])

    data = np.array([[income, credit_score, loan_amount, years_employed, points]])
    prediction = model.predict(data)[0]

    if prediction == 1:
        result = "Loan Approved"
        color = "#008000"
    else:
        result = "Loan Rejected"
        color = "#cc0000"

    return render_template("result.html", prediction=result, color=color)

if __name__ == "__main__":
    app.run(debug=True)