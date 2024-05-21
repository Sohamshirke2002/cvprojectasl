from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

data = pd.read_csv("/Users/sohamshirke/Documents/Projects/cvprojectasl/data/work - Sheet1.csv")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/result", methods=['POST'])
def result():
    grade = request.form['grade']
    work = request.form['work']

    dataFiltered = data[(data['M/C']==work) & (data['OPERATOR GRADE']==grade)] 
    dataOutput = dataFiltered[['NAME','Line','STATUS','ATTENDANCE']]
    dataOutput
    formatted_output = dataOutput.to_html(classes=['table', 'table-striped'], index=False)
    return formatted_output

