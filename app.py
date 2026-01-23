import streamlit as st
import pandas as pd

st.title("Netflix Watch History EDA")

@st.cache_data
def load_data():
    return pd.read_csv("Netflix_Watch_History_Dataset.csv")

df = load_data()

st.success("Data loaded successfully!")
st.write("Total rows:", df.shape[0])
st.dataframe(df.head())
