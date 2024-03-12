import streamlit as st
import pandas as pd
import requests
import json

# Configurações iniciais da página Streamlit
st.set_page_config(layout="wide")

# Barra lateral para interação com o usuário
with st.sidebar:
    st.title("Análise de Lucro")
    upload_file = st.file_uploader("Coloque o seu arquivo aqui")

# Verifica se um arquivo foi carregado
if upload_file is not None:
    df = pd.read_csv(upload_file)  # Carrega o arquivo CSV usando o pandas

   # Barra lateral para opções de filtragem
    with st.sidebar:
        # Lista de regiões distintas no DataFrame
        distinct_regions = df["Region"].unique().tolist()
        region_selected = st.selectbox("**Região Específica**", distinct_regions)
        
        # Seleção de vendedores com radio buttons
        seller_selected = st.radio("**Listas De Vendedores**", ["H", "C", "M", "L"], index=None)

        # Filtra o DataFrame com base nas seleções do usuário
        if region_selected:
            df = df[df['Region'] == region_selected]

        if seller_selected:
            df = df[df['Order Priority'] == seller_selected]

     # Seção principal de exibição de resultados 
    st.title(" **Tabela de Recorde de Vendas** ")

     # Título e exibição da tabela de dados completa
    st.bar_chart(df, x="Item Type", y="Total Profit")
    st.title(" **Lista de Produtos de Vendas** ")
    st.dataframe(df, use_container_width=True)

