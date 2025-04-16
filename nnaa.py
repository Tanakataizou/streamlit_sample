import streamlit as st

radio = st.radio("選択", ["んなあ", "おしり"])
if radio == "んなあ":
    st.write("それはんなあです") 