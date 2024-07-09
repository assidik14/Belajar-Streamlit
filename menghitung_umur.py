import streamlit as st
import datetime as dt

st.title ("Aplikasi menghitung umur")

tanggal_lahir = st.date_input("Masukan tanggal lahir kamu", max_value=dt.date.today(), min_value=dt.date(1990, 1, 1))
hitung = st.button("Hitung umur")

if hitung:
    today = dt.date.today()
    st.success(f"Hari ini tanggal {today} adalah hari {today:%A}")
    st.success(f"Tanggal lahir kamu adalah {tanggal_lahir}, kamu lahir pada hari {tanggal_lahir:%A}")
    
    umur_hari = today - tanggal_lahir
    umur_tahun = umur_hari.days // 365
    umur_bulan = (umur_hari.days % 365) // 30
    st.success(f"Umur kamu hari ini adalah {umur_tahun} tahun, {umur_bulan} bulan")
