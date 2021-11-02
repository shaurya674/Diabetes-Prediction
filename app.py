import numpy as np
import pickle
import pandas as pd
import streamlit as st

with open('model.pkl', 'rb') as file:
    classifier = pickle.load(file)
# @app.route('/')
def welcome():
    return "Welcome All"


# @app.route('/predict',methods=["Get"])
def predict_note_authentication(pregnencies, glucose, bps, Skint, imsulin, BMI, DiabetesPedigreeFunction, age):
    X = np.array([[pregnencies, glucose, bps, Skint, imsulin, BMI, DiabetesPedigreeFunction, age]])
    prediction = classifier.predict(X.astype(np.float))
    print(prediction)
    return prediction

#preg,glucose,bloodpress,skinthick,insulin,bmi,pedigree,age]
def main():
    st.title("Diabetes Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Diabetes ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    age = st.text_input("Age")
    sex = st.text_input("Sex")
    bps = st.text_input("Blood Pressure")
    BMI = st.text_input("BMI")
    imsulin = st.text_input("Insulin")
    pregnencies = st.text_input("Pregnencies")
    glucose = st.text_input("Glucose")
    Skint = st.text_input("Skin Thickness")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")

    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(pregnencies, glucose, bps, Skint, imsulin, BMI, DiabetesPedigreeFunction, age)
        if result==1:
            result = "You are Diabetic"
        else:
            result = "You are not Diabetic"
    st.success(result)
   

if __name__ == '__main__':
    main()
