import pickle
import numpy as np
import streamlit as st

loaded_model = pickle.load(open('V:/Jupyter/StreamLit Web Application/trained_model.sav','rb'))

def diabetes_prediction(input_data):
    # The input in List type, so we convert that into numpy array
    input_array = np.asarray(input_data)

    # Reshape the array
    input_reshaped = input_array.reshape(1,-1)
    prediction = loaded_model.predict(input_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return 'The Person is not diabetic'
    else:
        return 'The Person is diabetic'

def main():
    # Title of the Web APP
    st.title('Diabetes Prediction Web Application')

    # Get user input
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')

    # Save the predition
    diagnosis = ''

    # Creating Button
    if st.button('Test ur data'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])

    st.success(diagnosis)

if __name__ == '__main__':
    main()