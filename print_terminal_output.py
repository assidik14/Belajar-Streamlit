import streamlit as st
import os

hello_world = "Hello World"
print (hello_world)
st.text(hello_world)
st.success(hello_world)

st.divider()

hostnamectl = os.system("hostnamectl")
print (hostnamectl)