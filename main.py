from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

model = joblib.load("./model.pkl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    married = int(request.form['married'])
    dependents = int(request.form['dependents'])
    education = int(request.form['education'])
    selfEmployed = int(request.form['selfEmployed'])
    applicantIncome = int(request.form['applicantIncome'])
    loanAmount = float(request.form['loanAmount'])
    creditHistory = float(request.form['creditHistory'])

    prediction = model.predict([[married, dependents, education, selfEmployed, applicantIncome, loanAmount, creditHistory]])

    return render_template('result.html', result="Loan Approved" if prediction[0] == 1 else "Loan Rejected")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
