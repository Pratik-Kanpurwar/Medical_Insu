from flask import Flask, jsonify, render_template, request
import config
from Project_app.utils import MedicalInsurance

app = Flask(__name__)

####################################################################
############################--BASE API--############################
####################################################################

@app.route('/')
def hello_flask():
    print('Welcome to Project Prediction')
    return 'Thank You'

####################################################################

@app.route('/predict_charges')
def get_insurance_charges():
    
    data = request.form
    
    print(data)
    
    age = eval(data['age'])
    print(age)
    sex = data['sex']
    print(sex)
    bmi = eval(data['bmi'])
    print(bmi)
    children = eval(data['children'])
    print(children)
    smoker = data['smoker']
    print(smoker)
    region = data['region']
    print(region)

    med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges = med_ins.get_predicted_charges()
    
    # return jsonify({'MSG':'SUCCESS!'})
    return jsonify({'RESULT':f'Predicted Medical Insurance Charges are: {charges}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=config.PORT_NUMBER,debug=False)