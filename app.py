import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="Prediksi Harga Mobil",
    page_icon="🚗",
    layout="wide"
)

with open("model_mobil.pkl", "rb") as file:
    model = pickle.load(file)

st.markdown("""
<style>

h1 a, h2 a, h3 a {
    display: none !important;
}

.stApp {
    background: linear-gradient(135deg, #0f172a, #111827);
    color: white;
}

.main-box {
    padding: 35px;
    border-radius: 20px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 8px 32px rgba(0,0,0,0.35);
    animation: fadeIn 1s ease-in-out;
}

.card {
    padding: 25px;
    border-radius: 18px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 20px;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.25);
}

.result-box {
    padding: 30px;
    border-radius: 18px;
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    text-align: center;
    color: white;
    font-size: 32px;
    font-weight: bold;
    margin-top: 20px;
    animation: fadeInUp 0.8s ease-in-out;
}

.small-text {
    color: #cbd5e1;
    font-size: 15px;
    line-height: 1.8;
}

.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 14px;
    padding-top: 30px;
}

.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 14px;
    border: none;
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    color: white;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.02);
    background: linear-gradient(135deg, #1d4ed8, #6d28d9);
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(15px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(25px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

</style>
""", unsafe_allow_html=True)

with st.sidebar:

    st.title("🚗 Prediksi Harga Mobil")

    st.markdown("---")

    st.subheader("Final Project")
    st.write("Mata Kuliah : Sains Data")
    st.write("Metode : Linear Regression")

    st.markdown("---")

    st.subheader("Disusun Oleh")
    st.write("Nama : Rafli Haikal")
    st.write("NPM : 237006099")

    st.markdown("---")

    st.subheader("Universitas")
    st.write("Program Studi Informatika")
    st.write("Fakultas Teknik")
    st.write("Universitas Siliwangi")

st.markdown("""
<div class="main-box">

<h1>🚗 Prediksi Harga Mobil</h1>

<h3>Final Project Sains Data</h3>

<p class="small-text">
Aplikasi ini dibuat untuk memenuhi tugas UAS Mata Kuliah Sains Data.
Sistem menggunakan metode Linear Regression untuk memprediksi harga mobil
berdasarkan spesifikasi yang dimasukkan pengguna.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

col1, col2 = st.columns(2)

with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Spesifikasi Mesin")

    engine_size = st.number_input(
        "Engine Size",
        min_value=0.0,
        value=2.0,
        step=0.1
    )

    horsepower = st.number_input(
        "Horsepower",
        min_value=0.0,
        value=150.0,
        step=1.0
    )

    wheelbase = st.number_input(
        "Wheelbase",
        min_value=0.0,
        value=105.0,
        step=0.1
    )

    width = st.number_input(
        "Width",
        min_value=0.0,
        value=69.0,
        step=0.1
    )

    st.markdown('</div>', unsafe_allow_html=True)

with col2:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Spesifikasi Body")

    length = st.number_input(
        "Length",
        min_value=0.0,
        value=180.0,
        step=0.1
    )

    curb_weight = st.number_input(
        "Curb Weight",
        min_value=0.0,
        value=3.0,
        step=0.1
    )

    fuel_capacity = st.number_input(
        "Fuel Capacity",
        min_value=0.0,
        value=15.0,
        step=0.1
    )

    fuel_efficiency = st.number_input(
        "Fuel Efficiency",
        min_value=0.0,
        value=28.0,
        step=0.1
    )

    st.markdown('</div>', unsafe_allow_html=True)

st.write("")

if st.button("🔍 Prediksi Harga Mobil"):

    data_baru = pd.DataFrame({
        "Engine_size": [engine_size],
        "Horsepower": [horsepower],
        "Wheelbase": [wheelbase],
        "Width": [width],
        "Length": [length],
        "Curb_weight": [curb_weight],
        "Fuel_capacity": [fuel_capacity],
        "Fuel_efficiency": [fuel_efficiency]
    })

    hasil_prediksi = model.predict(data_baru)

    st.markdown(f"""
    <div class="result-box">
        Prediksi Harga Mobil<br><br>
        ${hasil_prediksi[0]:.2f} Ribu Dollar
    </div>
    """, unsafe_allow_html=True)

st.write("")

st.markdown("""
<div class="card">

<h4>Catatan</h4>

<p class="small-text">
Hasil prediksi ini merupakan estimasi berdasarkan model Linear Regression
dan data penjualan mobil yang digunakan pada project.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
Final Project Sains Data | Rafli Haikal - 237006099
</div>
""", unsafe_allow_html=True)
