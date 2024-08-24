import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("C:\Users\kedir\Downloads\data\data\benin-malanville.csv")

# Display the data
st.write(df.head())