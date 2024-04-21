# app.py
from flask import Flask, render_template, request, redirect, url_for
import joblib

app = Flask(__name__)

# Load the updated model
model = joblib.load('updated5_model.joblib')

@app.route('/')
def input_values():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    perimeter_worst = float(request.form['perimeter_worst'])
    concave_points_worst = float(request.form['concave points_worst'])
    radius_worst = float(request.form['radius_worst'])
    area_worst = float(request.form['area_worst'])
    concave_points_mean = float(request.form['concave points_mean'])
    area_mean = float(request.form['area_mean'])
    concavity_mean = float(request.form['concavity_mean'])
    area_se = float(request.form['area_se'])
    radius_mean = float(request.form['radius_mean'])

    # Add other input features here...

    # Make prediction using the loaded model
    #prediction = model.predict([[radius_mean, area_mean,concave points_se,symmetry_se,fractal_dimension_se,texture_worst,perimeter_worst,compactness_worst,concavity_worst,concave points_worst]])[0]  # Add other input features here...
    prediction = model.predict([[perimeter_worst,concave_points_worst,radius_worst,area_worst,concave_points_mean,area_mean,concavity_mean,area_se,radius_mean]])[0]

    # Redirect to the results page with the prediction
    return redirect(url_for('results', prediction=prediction))


#@app.route('/results/<prediction>')
#def results(prediction):
 #   cancer_result = 'benign' if prediction == 0 else 'malignant'
  #  message = 'The diagnosis indicates a benign tumor, which means the tumor is non-cancerous. While this is reassuring, it\'s still essential to monitor your health and follow up with regular check-ups. It\'s always wise to stay vigilant and seek medical advice if you notice any changes or concerns regarding your breast health. Remember, your health is paramount, and seeking medical advice as soon as possible is crucial for effective management and care.' if prediction == 0 else 'The diagnosis indicates a malignant tumor, it means that the tumor is cancerous and requires immediate medical attention. Early detection and treatment of breast cancer significantly improve the chances of successful outcomes. Remember, your health is paramount, and seeking medical advice as soon as possible is crucial for effective management and care.'
   # print("Message:",message)
    #return render_template('results.html', cancer_result=cancer_result, message=message)

@app.route('/results/<int:prediction>')
def results(prediction):
    #cancer_result = 'benign' if prediction == 0 else ''
    #message = 'The diagnosis indicates a benign tumor, which means the tumor is non-cancerous. While this is reassuring, it\'s still essential to monitor your health and follow up with regular check-ups. It\'s always wise to stay vigilant and seek medical advice if you notice any changes or concerns regarding your breast health. Remember, your health is paramount, and seeking medical advice as soon as possible is crucial for effective management and care.' if cancer_result == 'benign' else 'The diagnosis indicates a malignant tumor, it means that the tumor is cancerous and requires immediate medical attention. Early detection and treatment of breast cancer significantly improve the chances of successful outcomes. Remember, your health is paramount, and seeking medical advice as soon as possible is crucial for effective management and care.'
    cancer_result = 'malignant' if prediction == 1 else 'benign'
    message = 'The diagnosis indicates a benign tumor, which means the tumor is non-cancerous. While this is reassuring, it\'s still essential to monitor your health and follow up with regular check-ups. It\'s always wise to stay vigilant and seek medical advice if you notice any changes or concerns regarding your breast health. Remember, your health is paramount, and seeking medical advice as soon as possible is crucial for effective management and care.' if cancer_result == 'benign' else 'The diagnosis indicates a malignant tumor, it means that the tumor is cancerous and requires immediate medical attention. Early detection and treatment of breast cancer significantly improve the chances of successful outcomes. Remember, your health is paramount, and seeking medical advice as soon as possible is crucial for effective management and care.'


    print("Message:", message)
    return render_template('results.html', cancer_result=cancer_result, message=message)


if __name__ == '__main__':
    app.run(debug=True)
