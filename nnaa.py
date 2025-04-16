import streamlit as st


#st.set_page_config(layout="wide")

radio = st.radio("選択", ["んなあ", "おしり"])
if radio == "んなあ":
    st.write("それはんなあです") 
else:
    st.write("あかん")