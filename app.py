import pandas as pd
import streamlit as st
import openpyxl  

st.set_page_config(page_title="dados transporte", layout="wide", page_icon="📊")
st.title("dados transporte")
st.sidebar.header("Filtros")

df_tabela = pd.read_csv("dados_transporte_bh.csv", sep=";", decimal=",")
df_total = df_tabela["TOTAL USUARIOS"]

df_tabela
df_total






