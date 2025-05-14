import streamlit as st
import requests

st.title("Login 2FA Demo")

base = "http://localhost:8000/auth"
user = st.text_input("Username")
pwd = st.text_input("Password", type="password")
if st.button("Login Step 1"):
    res = requests.post(f"{base}/login", json={"username": user, "password": pwd})
    st.write(res.json())
    code = st.text_input("OTP Code")
    if st.button("Verify OTP"):
        r2 = requests.post(f"{base}/verify-otp", json={"username": user, "code": code})
        st.write(r2.json())