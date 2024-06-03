import pandas as pd
import sqlalchemy as sqa
import streamlit as st 
import numpy as np
import plotly.express as px
from PIL import Image

#logo = Image.open('matei.png')  # Substitua 'caminho/para/sua/logo.png' pelo caminho correto para sua imagem
st.image('matei.png', caption='')
col1, col2, col3 = st.columns([10, 50, 10])


st.write('***Taxa de Homicídio Intencional***')
dados = pd.read_csv("C:/Users/2302323/Documents/AP2/0_bases_originais/dados_originais_taxa_de_homicídio_intencional.csv", sep=";", encoding='utf-8')

option = st.selectbox(
   "Selecione a opção:",
   ("Base Analítica", "Relatórios"),
   index=None,
   placeholder="",
   )

engine = sqa.create_engine("sqlite:///taxas.db", echo=True)
comn = engine.connect()
dados = pd.read_sql('taxas.db', con=comn)
df = pd.DataFrame(dados)
#st.dataframe(df)

tx = st.select_slider(
    "Selecione a taxa",
    options=df['taxa'])
df2 = df.loc[df.taxa>=tx]


if option == "Base Analítica": 
    st.dataframe(df2)
elif option == "Relatórios":    
    

    dfpais = df2["pais"]
    fig = px.area(df2, x="pais", y="taxa")
    st.plotly_chart(fig)

    df2taxa = df2['taxa']
    grtaxa = px.box(df2, x = 'total')
    st.plotly_chart(grtaxa)

    df2total = df2['total']
    grtotal = px.bar(df2, x="regiao", y="total")
    st.plotly_chart(grtotal)

    df2regiao = df2['regiao']
    grregiao=  px.line(df2, x="sub_regiao")
    st.plotly_chart(grregiao)

    df2sub = df2['sub_regiao']
    grsub = px.histogram(df2, x="taxa", y="sub_regiao")
    st.plotly_chart(grsub)

