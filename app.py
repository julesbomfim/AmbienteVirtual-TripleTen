import streamlit as st
import pandas as pd
import plotly.express as px

# Cabeçalho (obrigatório)
st.header("Análise de Anúncios de Veículos")

# Ler dados (obrigatório)
car_data = pd.read_csv('data/vehicles.csv')

# Botão do histograma (obrigatório)
hist_button = st.button('Criar histograma')
if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botão do gráfico de dispersão (obrigatório)
scatter_button = st.button('Criar gráfico de dispersão')
if scatter_button:
    st.write('Criando gráfico de dispersão para preço x quilometragem')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)