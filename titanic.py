import pickle
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

pickle_in = open('titanic.pkl', 'rb')
regressor = pickle.load(pickle_in)

def predict_price(Pclass, age, n_sibl, parch, fare, gender, embarked):
    prediction = regressor.predict([[Pclass, age, n_sibl, parch, fare, gender, embarked]])
    print(prediction)
    return prediction

def main():
    st.title("This is page will say could you survive on Titanic")

    age = st.number_input("Your age:", min_value=18, max_value=100)
    gender = st.selectbox("Your gender(1 - Male ; 0 - Female):", [1, 0])
    n_sibl = st.number_input("How many siblings di you have:", min_value=0, max_value=100)
    fare = st.number_input("What was your fare:", min_value=0, max_value=100)
    Pclass = st.selectbox("Your class(1 - 1st class; 2- 2nd class; 3 - 3rd class):", [1, 2, 3])
    embarked = st.selectbox("Your station(1 - Q; 2- S; 3 - S):", [1, 2, 3])
    parch = st.selectbox("Your parch: ", [1, 0])


    result = ''
    if st.button('Predict'):
        result = int(predict_price(Pclass, age, n_sibl, parch, fare, gender, embarked))
        
    st.success('Prediction (1 - You will sirvive, 0 - You will now survive) {}'.format(result))
    
if __name__ == '__main__':
    main()