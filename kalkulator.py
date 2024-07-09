import streamlit as st

st.title("Aplikasi kalkulator")
st.text("Aplikasi kalkulator sederhana menggunakan Streamlit Python")
st.divider()

def penjumlahan(x, y):
      hasil = x + y
      st.success(f"Hasil dari penjumlahan {x} + {y} = {hasil}")

def pengurangan(x, y):
      hasil = x - y
      st.success(f"Hasil dari pengurangan {x} - {y} = {hasil}")

def perkalian(x, y):
      hasil = x * y
      st.success(f"Hasil dari perkalian {x} x {y} = {hasil}")

def pembagian(x, y):
      hasil = x / y
      st.success(f"Hasil dari pembagian {x} : {y} = {hasil}")

angka1 = st.number_input("Masukan angka pertama", 0)
angka2 = st.number_input("Masukan angka kedua", 0)
st.divider()

col1, col2, col3 , col4 = st.columns(4)

with col1:
    tambah = st.button("Tambah")

with col2:
    kurang = st.button("Kurang")

with col3:
    bagi = st.button("Bagi")

with col4:
    kali = st.button("Kali")


if tambah:
      penjumlahan(angka1, angka2)

if kurang:
      pengurangan(angka1, angka2)

if kali:
      perkalian(angka1, angka2)

if bagi:
      pembagian(angka1, angka2)