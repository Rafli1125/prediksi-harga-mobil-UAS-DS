import streamlit as st
import pandas as pd
import pickle

with open('model_mobil.pkl', 'rb') as file:
    model = pickle.load(file)

st.title('Prediksi Harga Mobil')
st.write('Aplikasi ini digunakan untuk memprediksi harga mobil berdasarkan spesifikasi yang dimasukkan.')

engine_size = st.number_input('Engine Size', min_value=0.0, value=2.0)
horsepower = st.number_input('Horsepower', min_value=0.0, value=150.0)
wheelbase = st.number_input('Wheelbase', min_value=0.0, value=105.0)
width = st.number_input('Width', min_value=0.0, value=69.0)
length = st.number_input('Length', min_value=0.0, value=180.0)
curb_weight = st.number_input('Curb Weight', min_value=0.0, value=3.0)
fuel_capacity = st.number_input('Fuel Capacity', min_value=0.0, value=15.0)
fuel_efficiency = st.number_input('Fuel Efficiency', min_value=0.0, value=28.0)

if st.button('Prediksi Harga'):
    data_baru = pd.DataFrame({
        'Engine_size': [engine_size],
        'Horsepower': [horsepower],
        'Wheelbase': [wheelbase],
        'Width': [width],
        'Length': [length],
        'Curb_weight': [curb_weight],
        'Fuel_capacity': [fuel_capacity],
        'Fuel_efficiency': [fuel_efficiency]
    })

    hasil_prediksi = model.predict(data_baru)

    st.success(f'Prediksi Harga Mobil: {hasil_prediksi[0]:.2f} ribu dollar')