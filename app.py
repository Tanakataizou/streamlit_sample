import streamlit as st
st.write("# title")

st.caption("注釈") 

import pandas as pd
df=pd.DataFrame(
    {
        "first column":[1,2,3,4],
        "second column":[10,20,30,40],
    }
)
st.write(df)

st.image("https://i3.gamebiz.jp/media/0af4eaca-9e9e-433f-b815-4a097e3836f1.jpg")

name=st.text_input("名前")

age=st.number_input("年齢",step=1)

st.write(f"名前:{name}({age})")

if st.button("push"):
    st.write("ボタンを押しました")

select=st.selectbox("好きなスポーツ",options=["サッカー","野球","バスケットボール","バドミントン"])
st.write(f"あなたの好きなスポーツは{select}です")

radio=st.radio("選択",["猫","犬"])
st.write(f"あなたが選択したものは:{radio}")

uploaded_file=st.file_uploader("Upload",type=["csv"])
if uploaded_file:
    dataflame=pd.read_csv(uploaded_file)
    st.write(dataflame)

check=st.checkbox("ok")
st.write(f"チェック:{check}")


cols=st.colums(2)
with cols[0]:
    st.write("列1")
with cols[1]:
    st.write("列2")