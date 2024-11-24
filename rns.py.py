import streamlit as st
import pandas as pd
from streamlit import button

name = st.text_input("Enter Your Name : ")
fname = st.text_input("Enter Your Father Name : ")
sname = st.text_input("Enter Your Surname")
adr  = st.text_area("Enter Your adr : ")
classdata = st.selectbox("Enter Your Roll Number : ",(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64))

button = st.button("Open camera")
if button :
    st.markdown(f"""
    Name : {name}
    Father Name : {fname}
    Surname Name : {sname}
    address : {adr}
    class : {classdata}""")