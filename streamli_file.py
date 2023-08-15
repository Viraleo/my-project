import streamlit as st
import pandas as pd
import numpy as np


st.write("""
My first app
Hello *world!*
""")

def load_dataset(data_link):
    dataset = pd.read_csv(data_link)
    return dataset


titanic_link = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
titanic_data = load_dataset(titanic_link)

st.dataframe(titanic_data)
