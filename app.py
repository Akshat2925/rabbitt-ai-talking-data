import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Talking Rabbitt - AI Data Assistant")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.write("Data Preview")
    st.dataframe(df)

    question = st.text_input("Ask a question about your data")

    if question:
        if "highest revenue" in question.lower():
            region = df.loc[df['Revenue'].idxmax()]
            st.write(f"Highest revenue region: {region['Region']} with {region['Revenue']}")

        if "chart" in question.lower() or "visualize" in question.lower():
            fig, ax = plt.subplots()
            ax.bar(df['Region'], df['Revenue'])
            ax.set_xlabel("Region")
            ax.set_ylabel("Revenue")
            st.pyplot(fig)