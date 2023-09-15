import numpy as np
import pickle
import streamlit as st
import pandas as pd

loaded_model = pickle.load(open('C:/Users/ADMIN/Desktop/python jupyter/water quality pred/water_model.sav','rb'))

nav = st.sidebar.radio("Navigation",["About","Predict"])
df = pd.read_csv('water_potability.csv')

if nav=="About":
    st.title("Water Quality Prediction App")
    st.text("")
    st.text("")
    st.image('water.webp',width=600)

if nav=="Predict":

    def water_prediction(input_data):

        data_numeric = np.array(input_data).astype(float)
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = loaded_model.predict(input_data_reshaped)
        print(prediction)

        if(prediction[0] == 1):
            return "WATER IS DRINKABLE"
        else:
            return "WATER IS NOT DRINKABLE"

    def main():

        st.title('Water Quality Predictor App')

        ph = st.number_input('Level of ph : ')
        Hardness = st.number_input('Hardness Level : ')
        Solids = st.number_input('Solids Value : ')
        Chloramines = st.number_input('Chloramines Value : ')
        Sulfates = st.number_input('Sulfates Value : ')
        Conductivity = st.number_input('Conductivity Value : ')
        Organic_carbon = st.number_input('Organic_carbon Value  : ')
        Trihalomethanes = st.number_input('Trihalomethanes values : ')
        Turbidity = st.number_input('Turbidity values : ')

        # code for prediction

        analysis = ' '

        if st.button('PREDICT'):
            analysis = water_prediction([ph , Hardness , Solids , Chloramines , Sulfates , Conductivity , Organic_carbon , Trihalomethanes , Turbidity])
        
        st.success(analysis)

    if __name__ == '__main__':
            main()
    