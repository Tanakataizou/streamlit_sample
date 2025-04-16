import streamlit as st
st.write("# title")

st.caption("注釈") 

import pandas as pd
df=pd.DataFrame(
    {
        "first column":[1,2,3,4],
        "second column":[10,20,30,20],
    }
)
st.write(df)

st.image("https://i3.gamebiz.jp/media/0af4eaca-9e9e-433f-b815-4a097e3836f1.jpg")

name=st.text_input("なまえ")

age=st.number_input("年齢",step=1)

st.write(f"名前:{name}")
st.write(f"年齢:{age}")