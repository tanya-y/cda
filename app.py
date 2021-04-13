import streamlit as st

import pandas as pd
df=pd.read_csv('incedenceOfMalaria.csv')


st.title('Communicable Disease Analysis')
st.dataframe(df)
st.markdown('git remote add origin https://github.com/tanya-y/cda.git')

sidebar=st.sidebar
sidebar.header('Choose your action')



