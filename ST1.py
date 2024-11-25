# 391057 - Tejas Shastri
# Streamlit assignment 1

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CSV Data Visualizer")
st.sidebar.header("Upload your CSV file")

uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")
    st.dataframe(df)

    columns = df.columns.tolist()
    selected_column = st.sidebar.selectbox("Select Column for Visualization", options=columns)

    chart_type = st.sidebar.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Histogram"])

    st.subheader(f"{chart_type} for {selected_column}")
    if chart_type == "Line Chart":
        st.line_chart(df[selected_column])
    elif chart_type == "Bar Chart":
        st.bar_chart(df[selected_column])
    elif chart_type == "Histogram":
        plt.figure(figsize=(10, 6))
        plt.hist(df[selected_column].dropna(), bins=20, color='blue', edgecolor='black')
        plt.title(f"Histogram of {selected_column}")
        plt.xlabel(selected_column)
        plt.ylabel("Frequency")
        st.pyplot(plt)

else:
    st.write("Upload a CSV file to get started.")