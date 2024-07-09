import streamlit as st

st.title("Aplikasi menghitung luas Persegi Panjang")

panjang = st.number_input("Masukan Panjang", 0)
lebar = st.number_input("Masukan Lebar", 0)
hitung = st.button("Hitung Luas")

if hitung:
    hitung = panjang * lebar
    st.success(f"Luas Persegi Panjang = {hitung}")