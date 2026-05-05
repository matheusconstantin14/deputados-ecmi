import streamlit as st
import pandas as pd

df = pd.read_csv('deputados_2022.csv')
st.dataframe(df)


partido = st.text_input("Escolha o Partido: ")
print("Seu partido escolhido é: " + partido)
