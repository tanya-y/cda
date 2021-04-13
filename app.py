import streamlit as st

import pandas as pd
df=pd.read_csv('incedenceOfMalaria.csv')


st.title('Communicable Disease Analysis')
st.dataframe(df)
st.markdown('')

sidebar=st.sidebar
sidebar.header('Choose your action')



