# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 12:31:16 2025

@author: USER
"""


import pickle
import pandas as pd
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open('Gedeon_laptop_price_prediction.pkl','rb'))

def laptop_price_prediction(Brand, Processor_Speed, RAM_Size, Storage_Capacity, Screen_Size, Weight):
    # Create a dataframe for the model
    new_laptop = pd.DataFrame([{
        'Brand': Brand,
        'Processor_Speed': Processor_Speed,
        'RAM_Size': RAM_Size,
        'Storage_Capacity': Storage_Capacity,
        'Screen_Size': Screen_Size,
        'Weight': Weight,
    }])
    
    # Predict the price
    predicted_price = loaded_model.predict(new_laptop)
    return predicted_price[0]

def main():
    st.title('GEDEON LAPTOP PRICE PREDICTION SYSTEM')

    # Input fields
    Brand = st.text_input('Enter the Brand (numeric or code)')
    Processor_Speed = st.text_input('Enter Processor Speed (GHz)')
    RAM_Size = st.text_input('Enter RAM Size (GB)')
    Storage_Capacity = st.text_input('Enter Storage Capacity (GB)')
    Screen_Size = st.text_input('Enter Screen Size (inches)')
    Weight = st.text_input('Enter Weight (kg)')

    if st.button('Predict Price'):
        try:
            Brand = int(Brand)
            Processor_Speed = float(Processor_Speed)
            RAM_Size = int(RAM_Size)
            Storage_Capacity = int(Storage_Capacity)
            Screen_Size = float(Screen_Size)
            Weight = float(Weight)
            
            # Prediction
            price = laptop_price_prediction(Brand, Processor_Speed, RAM_Size, Storage_Capacity, Screen_Size, Weight)
            st.success(f'The predicted price for the laptop is: ${price:.2f}')
        except ValueError:
            st.error("Please enter valid numeric values for all inputs.")

if __name__ == '__main__':
    main()

