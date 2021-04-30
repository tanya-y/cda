import streamlit as st

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd
from database import Report
from AnalyseData import Analyse
from visualization import *

engine = create_engine('sqlite:///db.sqlite3')
Session = sessionmaker(bind=engine)
sess = Session()

st.title('Cummunicable Disease Analysis')
st.text("")
st.text("")
sidebar = st.sidebar

tbAnalysis = Analyse('datasets/tuberculosis.csv')
malAnalysis = Analyse('datasets/malaria.csv')

def viewDataset():
    
    st.header("Dataset Details")
    datasetNames = ['Malaria Dataset', 'Tuberculosis Dataset']
    selData = st.selectbox(options = datasetNames, label = "Select the Dataset to View Details")
    st.text("")
    st.text("")
    if selData == datasetNames[0]:
        data =  malAnalysis.getDataset()
        st.dataframe(data)
    elif selData == datasetNames[1]:
        data =  tbAnalysis.getDataset()
        st.dataframe(data)
    
def analyseApps():
    # st.header('Trending App Categories')
    # st.plotly_chart(plotBar(appAnalysis.getTopCategories(), 'Top App Categories on PlayStore', 'No. of Apps', 'Category Name'))

    pass
    
def analyseSentiments():
    st.header('Sentiment Analysis of User Reviews')
    

def viewForm():
    title = st.text_input("Report Title")
    desc = st.text_area('Report Description')
    btn = st.button("Submit")

    if btn:
        report1 = Report(title = title, desc = desc, data = "")
        sess.add(report1)
        sess.commit()
        st.success('Report Saved')

def viewReport():
    reports = sess.query(Report).all()
    titlesList = [ report.title for report in reports ]
    selReport = st.selectbox(options = titlesList, label="Select Report")
    
    reportToView = sess.query(Report).filter_by(title = selReport).first()

    markdown = f"""
        ## {reportToView.title}
        ### {reportToView.desc}
        
    """

    st.markdown(markdown)

sidebar.header('Choose Your Option')
options = [ 'View Database', 'Analyse Malaria', 'View Report' ]
choice = sidebar.selectbox( options = options, label="Choose Action" )


if choice == options[0]:
    viewDataset()
elif choice == options[1]:
    analyseApps()
elif choice == options[2]:
    viewReport()