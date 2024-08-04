'''Import Module'''
import datetime as dt
import streamlit as st

# Function
# def header():
#     '''Fungsi menampilkan judul aplikasi'''
#     judul = "APLIKASI MENGHITUNG BODY MASS INDEX"
#     print(f"{'SELAMAT DATANG':^50}")
#     print(f"{judul:^50}")
#     print(50*"=")

def user_input():
    '''Fungsi untuk mengambil input user'''
    nama = st.text_input("Masukan nama kamu")
    lahir = st.date_input("Masukan tanggal lahir kamu", max_value=dt.date.today(), min_value=dt.date(1990, 1, 1))
    bb = st.number_input("Masukan berat badan kamu dalam Kilogram (Kg)", 0)
    tb = st.number_input("Masukan tinggi badan kamu dalam Centimeter (Cm)", 0)
    gender = st.selectbox(
    "Gender",
    ("Laki-laki", "Perempuan"),
    placeholder="Pilih gender kamu...",
    )
    st.write("Kamu ", gender)
    return nama,lahir,bb,tb,gender

def hitung_umur(tgl_lahir_user):
    '''Fungsi untuk menghitung umur user'''
    today = dt.date.today()
    umur_hari = today - tgl_lahir_user
    umur_tahun = umur_hari.days // 365
    umur_bulan_sisa = (umur_hari.days % 365) // 30
    print (f"Umur kamu sekarang \t: {umur_tahun} tahun, {umur_bulan_sisa} bulan")
    return umur_tahun, umur_bulan_sisa

def hitung_bmi(berat_badan, tinggi_badan):
    '''Fungsi menghitung BMI'''
    bmi = (berat_badan / (tinggi_badan ** 2)) * 10000
    return bmi

def bmi_score(nama, score):
    '''Fungsi score bmi'''
    if score < 18.5:
        st.error(f"""
Wah, kamu Underweight {nama}!!
Kamu terlalu kurus, kamu harus perbanyak makan
makanan bergizi dan berprotein tinggi
""")
    elif score >= 18.5 and score <= 24.9:
        st.success(f"""
Selamat, kamu Normal {nama}!!
Pertahankan pola hidupmu saat ini dan lengkapi
dengan asupan yang baik dan tetap berolahraga
""")
    elif score >= 25.0 and score <= 29.9:
        st.warning(f"""
Wah kamu Overheight {nama}!!
Jaga pola makan dan perbanyak aktivitas olahragamu
agar pembakaran lemak menjadi lebih optimal
""")
    elif score >= 30.0:
        st.error(f"""
Gawat, kamu Obesity {nama}!!
Kamu terlalu gemuk, masuk dalam kategori obesitas.
Kurangi asupan dan perbanyak olahraga serta aktivitas
di luar ruangan
""")
        
# Main App
st.title ("Aplikasi Body Mass Index Calculator")
nama_user, lahir_user, bb_user, tb_user, gender_user = user_input()
proses = st.button("Proses")

if proses:
    # if nama_user == "":
    #     st.error("Silakan isi nama dulu..")
    # if bb_user == 0:
    #     st.error("Silakan isi berat badan dulu...")
    # if tb_user == 0:
    #     st.error("Silakan isi tinggi badan dulu...")

    umur_tahun_user, umur_bulan_user = hitung_umur(lahir_user)
    bmi_user = hitung_bmi(bb_user, tb_user)
    if gender_user == "Laki-laki":
        st.success(f"Heyy broo {nama_user}, terimakasih sudah mengisi data")
    else:
        st.success(f"Heyy sistt {nama_user}, terimakasih sudah mengisi data")

    st.success(f"""
Hari ini adalah {dt.date.today():%A}, {dt.date.today()}\n
Selamat {nama_user}, usia kamu saat ini adalah {umur_tahun_user} tahun {umur_bulan_user} bulan\n
Score BMI kamu adalah {bmi_user:.1f}
""")
    bmi_score(nama_user, bmi_user)