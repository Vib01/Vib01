# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 22:08:12 2024

@author: VIBHU SHARMA
"""

import numpy as np
import pickle
import streamlit as st
loaded_model=pickle.load(open("C:/Users/VIBHU SHARMA/OneDrive/Desktop/docs/heart_trained_model.sav",'rb'))
#creating a function for prediction
def heart_prediction(input_data):
    
    input_data_as_numpy=np.array(input_data)
    #reshaping numby according to predict one data
    input_data_reshaped=input_data_as_numpy.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    if(prediction[0]==0):
      return "No heart disease detected"
    else:
      return "heart disease detected"


def main():
    
    #giving a title
    st.title('heart detection')
    #getting input from the user
    
    age=st.text_input('whats your age ?: ')
    sex=st.text_input('whats your sex(M/F) ?: ')
    cp=st.text_input('whats your chest pain type ?: ')
    trestbps=st.text_input('whats your resting blood pressure ?: ')
    chol=st.text_input('whats your cholestrol ?: ')
    fbs=st.text_input('whats your fasting blood sugar ?: ')
    restecg=st.text_input('whats your resting e-cardiographic ?: ')
    thalach=st.text_input('whats your max heart rate ?: ')
    exang=st.text_input('excercise induced angina ?: ')
    oldpeak=st.text_input('ST depression induced by exercise relative to rest ?: ')
    slope=st.text_input('slope of the peak excercise ST segment ?: ')
    ca=st.text_input('number of major vessels?: ')
    thal=st.text_input('1=normal,2=fixed defect,3=reversible defect?: ')
    
    #code for prediction
    diagnosis = ''
    #creating  a button for prediction
    if st.button('Heart test result'):
        diagnosis = heart_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
    st.success(diagnosis)


if __name__=='__main__':
    main()