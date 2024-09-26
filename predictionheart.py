# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
#loading the saved model
loaded_model=pickle.load(open("C:/Users\VIBHU SHARMA\OneDrive\Desktop\docs\heart_trained_model.sav",'rb'))


input_data=(40,1,0,110,167,0,0,114,1,2,1,0,3,)
input_data_as_numpy=np.array(input_data)
#reshaping numby according to predict one data
input_data_reshaped=input_data_as_numpy.reshape(1,-1)
prediction=loaded_model.predict(input_data_reshaped)
print(prediction)
if(prediction[0]==0):
  print("No heart disease detected")
else:
  print("heart disease detected")