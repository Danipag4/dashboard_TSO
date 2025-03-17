import streamlit as st
import pandas as pd
import plotly_express as px
import numpy as np

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
aval = ["Auto Avaliação","Avaliador"]
st.sidebar.image("Logo TSO.jpg")


Nome = st.sidebar.selectbox("Colaboradores", df["Colab"].unique())

df_filtered = df[df["Colab"] == Nome]
df_Média = df_filtered.groupby("Compet")[["Auto Avaliação","Avaliador"]].mean().reset_index()
#df_Média

aval = ["Auto Avaliação","Avaliador"]

#-------------------------------------------------------------------------------------
Avaliado = str(Nome)
st.write("""
## Competências
""" ), Avaliado

fig_comp = px.bar(df_Média, y=aval, x="Compet", barmode='group', color_discrete_map = {"Auto Avaliação":"Brown", "Avaliador":"Yellow"})
fig_comp.update_layout(xaxis_title="Comtetências", yaxis_title="Médias")

fig_comp

#df_filtered

#-------------------------------------------------------------------------------------------

st.write("""
## Análise das Perguntas
""" ), Nome

df["CompetUniq"] = df_filtered["Competencia"]
unica_Competencia = st.selectbox("Escolha a Competência",df["CompetUniq"].unique(),index=1)

df_filtered2 = df_filtered[df["Compet"] == unica_Competencia]

fig_Perg = px.bar(df_filtered2, y="Pergunta", x=aval, orientation="h", barmode='group', color_discrete_map = {"Auto Avaliação":"Brown", "Avaliador":"Yellow"})
fig_Perg.update_layout(xaxis_title="Médias", yaxis_title="Perguntas")
fig_Perg

#df_filtered2

#-----------------------------------------------------------------------------------------

st.write("""
## Desempenho Geral TSO por Competência
""" )

Compet_Desemp = st.selectbox("Defina a Competência",df["Competencia"].unique(),index=1)

aval = ["Auto Avaliação","Avaliador"]

df_filtered5 = df[df["Compet"] == Compet_Desemp]

df_MédiaGeral = df_filtered5.groupby("Nome")[["Auto Avaliação","Avaliador"]].mean().reset_index()
#df_MédiaGeral

fig_DesenvGeral = px.bar(df_MédiaGeral, y=aval, x="Nome", barmode='group',color_discrete_map = {"Auto Avaliação":"Brown", "Avaliador":"Yellow"})
fig_DesenvGeral.update_layout(xaxis_title="Colaboradores", yaxis_title="Médias")
fig_DesenvGeral

#---------------------------------------------------------------------------------

st.write("""
## Desempenho da TSO por Setor x Competência
""" ), Compet_Desemp

df_filtered3 = df[df["Competencia"] == Compet_Desemp]
#df_filtered3

df_MédiaSetor = df_filtered5.groupby("Setor")[["Auto Avaliação","Avaliador"]].mean().reset_index()
#df_MédiaSetor

fig_Setor = px.bar(df_MédiaSetor, y=aval, x="Setor", barmode='group', color_discrete_map = {"Auto Avaliação":"Brown", "Avaliador":"Yellow"})
fig_Setor.update_layout(xaxis_title="Setores", yaxis_title="Médias")
fig_Setor
