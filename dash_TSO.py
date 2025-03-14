import streamlit as st 
import pandas as pd 
import plotly_express as px 
import numpy as np
#import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

#color = st.color_picker("Pick A Color", "#00f900")
#st.write("The current color is", color)

df = pd.read_csv("Respostas_TSO.csv", sep=",")


df=df.sort_values("Nome")

df["Colab"] = df["Nome"]
df["Compet"] = df["Competencia"]

st.write("""
# TSO - Análise de Competências
""" )
aval = ["Autoavaliação","Gestor"]

Nome = st.sidebar.selectbox("Colaboradores",df["Colab"].unique())

df_filtered = df[df["Colab"] == Nome]

df["Compet"] = df_filtered["Competencia"]

aval = ["Autoavaliação","Gestor"]

st.write("""
## Competências
""" ), Nome

fig_comp = px.bar(df_filtered, y=aval, x="Competencia", barmode='group')
fig_comp

#df_filtered

st.write("""
## Análise das Perguntas
""" ), Nome

unica_Competencia = st.selectbox("Escolha a Competência",df["Compet"].unique(),index=1)

df_filtered2 = df_filtered[df["Compet"] == unica_Competencia]

fig_Perg = px.bar(df_filtered2, y="Pergunta", x=aval, orientation="h", barmode='group')

fig_Perg

#df_filtered2

st.write("""
## Desempenho por Competência
""" )

Compet_Desemp = st.selectbox("Defina a Competência",df["Competencia"].unique(),index=1)

aval = ["Autoavaliação","Gestor"]

df_filtered3 = df[df["Competencia"] == Compet_Desemp]

#df_filtered3

fig_Desenv = px.bar(df_filtered3, y=aval, x="Nome", barmode='group')
fig_Desenv

st.write("""
## Desempenho da TSO por Setor x Competência
""" ), Compet_Desemp

fig_Setor = px.bar(df_filtered3, y=aval, x="Setor", barmode='group')
fig_Setor
