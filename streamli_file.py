import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title("My first streamlit app")
st.header("This is about bike")

st.sidebar.title ("Here's going to be some information")

def load_dataset(data_link):
    dataset = pd.read_csv(data_link, index_col = "datetime", parse_dates=True))
    return dataset


bike_link = 'https://gitlab.com/codedeploycloud/data_science/-/raw/main/datasets/insurance_1.csv'
bike_data = load_dataset(bike_link)

st.dataframe(bike_data)
bike_data["hour"]=bike_data.index.hour
bike.rename(columns={'count': "total_count"}, inplace= True)

fig, ax = plt.subplots()
ax.plot(bike_data['hour'])
st.pyplot(fig)
