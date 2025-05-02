pip install seaborn
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import io


#Title and subheaders
st.title("Exploratory Data Analysis")
st.subheader("For doing basic data analysis without delving into confusing python codes!")

#Upload Dataset
upload = st.file_uploader("Hello! Upload your data in csv format to get started")
if upload is not None:
    df=pd.read_csv(upload)

#Show Dataset
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("First 5 rows"):
            st.write(df.head())
        if st.button("Last 5 rows"):
            st.write(df.tail())

#Check shape of each column
if upload is not None:
    if st.checkbox("Show the no of rows and columns of the dataset"):
        st.text("No of rows and columns:")
        st.write(f"There are {df.shape[0]} rows and {df.shape[1]} columns.")

#Check info of each column
if upload is not None:
    if st.checkbox("Show information of each column"):
        st.text("Info:")
        buffer = io.StringIO()     #storing the string value of df.info as it cannot be displayed directly using write
        df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

#Check for null values
if upload is not None:
    test=df.isnull().values.any()
    if test==True:
        if st.checkbox("Null Values in the dataset!"):
            st.text(df.isnull().sum())
            if st.button("Show heatmap of the null values"):
                fig, ax =plt.subplots()
                sns.heatmap(df.isnull(), ax=ax)
                st.pyplot(fig)

#Check for duplicated values
if upload is not None:
    test=df.duplicated().any()
    if test==True:
        st.warning(f"The dataset has {df.duplicated().sum()} duplicated values!")
        dup=st.selectbox("Do you want to remove the duplicate values?", \
                         ("Select One", "Yes", "No"))
        if dup=="Yes":
            df.drop_duplicates(inplace=True)
            st.success("Duplicates are removed")
        if dup=="No":
            st.text("Okay, the duplicates were not removed")     

#Get overall stats
if upload is not None:
    if st.checkbox("Summary of the Dataset"):
        st.write(df.describe(include="all"))

#Created by
if st.checkbox("Created by"):
    st.success("Debraj Bhattacharya")
        
        
            
