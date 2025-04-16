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