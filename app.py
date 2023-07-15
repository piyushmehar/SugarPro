from   flask import Flask, render_template,request
import numpy as np
import pickle 


app = Flask(__name__)
model = pickle.load(open('F:\MyDS\projects\SugarPro\model.pkl' ,'rb'))

@app.route('/')
def hello():
    return render_template("home.html")

@app.route('/home.html')
def home():
    return render_template("home.html")

@app.route('/blog.html')
def blog():
    return render_template("blog.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/predict.html')
def index():
    return render_template("predict.html")

@app.route('/predict.html', methods=['POST'])
def predict():
    Pregnancies  = request.form.get('Pregnancies')
    Glucose = request.form.get('Glucose')
    BloodPressure = request.form.get('BloodPressure')
    SkinThickness = request.form.get('SkinThickness')
    Insulin = request.form.get('Insulin')
    bmi = request.form.get('bmi')
    DiabetesPedigreeFunction = request.form.get('DiabetesPedigreeFunction')
    Age = request.form.get('Age')

    print(Pregnancies, Glucose,BloodPressure ,SkinThickness , Insulin , bmi , DiabetesPedigreeFunction ,Age)
    
    bmi = float(bmi)
    if(bmi <= 18):
        NewBMI = 1
        x = 'Underweight'
    elif(bmi >18 and bmi<=24):
        NewBMI = 5
        x = 'Normal'
    elif(bmi >24 and bmi <= 29):
        NewBMI = 4
        x = 'Overweight'
    elif(bmi >29 and bmi<=34):
        NewBMI = 1
        x = 'Obesity 1'
    elif(bmi >34 and bmi<= 39):
        NewBMI = 2
        x = 'Obesity 2'
    elif(bmi >39):
        NewBMI = 3
        x = 'Obesity 3'
    # render_template('predict.html', bmilevel='BMI Level: {}'.format(x))

    Insulin = float(Insulin)
    if((Insulin) >=16 and Insulin<=166):
        NewInsulinScore = 1
        y = 'Normal'
    else:
        NewInsulinScore = 0
        y = 'Abnormal'
    # render_template('predict.html', insulinlevel='Insulin Level: {}'.format(y))
    
    Glucose = float(Glucose)
    if(Glucose <= 70):
        NewGlucose = 1
        z = 'Low'
    elif(Glucose >70 and Glucose<=99):
        NewGlucose = 2
        z = 'Normal'
    elif(Glucose > 99 and Glucose <= 126):
        NewGlucose = 3
        z = 'Prediabetic'
    elif(Glucose >126):
        NewGlucose = 0
        z = 'Diabetic'
    # render_template('predict.html', glucoselevel='Glucose Level: {}'.format(z))


    features = [Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,bmi,DiabetesPedigreeFunction,Age,NewBMI,NewInsulinScore,NewGlucose]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    
    if(output==0):
        return render_template('predict.html', prediction_text0='Cool! Person is not having Diabetes'.format(output))
    elif(output==1):
        return render_template('predict.html', prediction_text1='Oops! Person is suffering from Diabetes'.format(output))
    
    # render_template('predict.html', bmilevel='BMI Level: {}'.format(x))
    # render_template('predict.html', glucoselevel='Glucose Level: {}'.format(z))
    # render_template('predict.html', insulinlevel='Insulin Level: {}'.format(y))



if __name__=="__main__":
    app.run()