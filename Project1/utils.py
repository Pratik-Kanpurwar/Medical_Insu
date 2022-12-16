import pickle
import json
import config
import numpy as np
import warnings
warnings.filterwarnings('ignore')

class MedicalInsurance():
    def __init__(self,age,sex,bmi,children,smoker,region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = 'region_'+region
        
    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)
            
        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)
            
    def get_predicted_charges(self):
        self.load_model()
        
        index = self.json_data['columns'].index(self.region)

        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.age
        test_array[1] = self.json_data['sex'][self.sex]
        test_array[2] = self.bmi
        test_array[3] = self.children
        test_array[4] = self.json_data['smoker'][self.smoker]

        test_array[index] = 1
        
        # print('predicted charges are >> ',self.model.predict([test_array]))
        
        # print("Test Array:",test_array )
        return np.around(self.model.predict([test_array])[0],2)
        
if __name__ == "main":
    
    age = 19.0
    sex = 'male'
    bmi = 27.9
    children = 3
    smoker = 'yes'
    region = 'southeast'

    med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
    med_ins.get_predicted_charges()