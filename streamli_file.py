import streamlit as st
import pandas as pd
import numpy as np


st.title("My first streamlit app")
st.header("This is about bike")

st.sidebar.title ("Here's going to be some information")

def load_dataset(data_link):
    dataset = pd.read_csv(data_link)
    return dataset


titanic_link = 'https://gitlab.com/codedeploycloud/data_science/-/raw/main/datasets/insurance_1.csv'
titanic_data = load_dataset(titanic_link)

st.dataframe(titanic_data)
