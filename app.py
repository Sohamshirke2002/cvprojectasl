from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the data once when the app starts
data = pd.read_csv("data/work - Sheet1.csv")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/result", methods=['POST'])
def result():
    grade = request.form['grade']
    work = request.form['work']

    # Filter the data based on the form inputs
    data_filtered = data[(data['M/C'] == work) & (data['OPERATOR GRADE'] == grade)]
    data_output = data_filtered[['NAME', 'Line', 'STATUS', 'ATTENDANCE']]

    # Convert the DataFrame to a list of dictionaries for easier template rendering
    data_dict = data_output.to_dict(orient='records')

    # Render the results template
    return render_template('result.html', data=data_dict)

if __name__ == "__main__":
    app.run(debug=True)
