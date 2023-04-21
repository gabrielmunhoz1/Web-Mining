import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Lendo o arquivo CSV
data = pd.read_csv('../bases_de_upload/dados_tratados.csv', delimiter=';')

top_precos = 20
top_titulos = 20

# título do aplicativo
st.title('Visualizações Gráficas - Produtos Arduino|Preços')

grafico = ['streamlit1', 'streamlit2', 'boxplot', 'surface chart', 'line chart', 'area chart']

escolha_do_grafico = st.sidebar.selectbox("Escolha o grafico", grafico)

if escolha_do_grafico=='streamlit1':
    # bar chart(medio) visualização usando o Streamlit
    st.header('1 - Preço Médio por Produto')
    mean_price = data.groupby('titulo')['preco'].mean().reset_index()
    mean_price = mean_price.sort_values('preco', ascending=False).head(top_precos)
    st.bar_chart(mean_price, x='titulo', y='preco')
    st.write('Este Grafico mostra os {} produtos com os maiores preços médios.'.format(top_precos))

if escolha_do_grafico=='streamlit2':
    # bar chart(maiores) visualização usando o Streamlit
    st.header('2 - Preço Mínimo e Máximo por Produto')
    min_max_price = data.groupby('titulo')['preco'].agg(['min', 'max']).reset_index()
    min_max_price = min_max_price.sort_values('max', ascending=False).head(top_precos)
    st.bar_chart(min_max_price, x='titulo', y=['min', 'max'])
    st.write('Este Grafico mostra os {} produtos com os maiores preços máximos.'.format(top_precos))

if escolha_do_grafico=='boxplot':
    #box plot visualização usando o Plotly
    st.header('3 - Box Plot')
    fig = px.box(data.groupby('titulo')['preco'].mean().reset_index(), x='titulo', y='preco')
    fig.update_layout(xaxis=dict(showticklabels=False))
    st.plotly_chart(fig)
    st.write('Este Grafico mostra a distribuição dos preços dos {} produtos com os maiores preços médios.'.format(top_precos))


if escolha_do_grafico=='surface chart':
    # Gráfico de superfície
    st.header('Gráfico de Superfície')
    top_20 = data.nlargest(20, 'preco')
    fig = go.Figure(data=[go.Surface(z=top_20['preco'].values.reshape(-1, 5))])
    fig.update_layout(title='20 produtos com os maiores preços', autosize=False,
                    width=800, height=800, margin=dict(l=65, r=50, b=65, t=90))
    st.plotly_chart(fig)

if escolha_do_grafico=='line chart':
    # criando o gráfico de linha com o Plotly
    st.header('Gráfico 5 - Line Chart - Preço por Produto (Top {})'.format(top_titulos))
    mean_price = data.groupby('titulo')['preco'].mean().reset_index()
    mean_price = mean_price.sort_values(by='preco', ascending=False)[:top_titulos]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=mean_price['titulo'], y=mean_price['preco'], mode='lines+markers'))
    st.plotly_chart(fig)
    st.write('Este Grafico mostra os {} produtos com os maiores preços.'.format(top_titulos))

if escolha_do_grafico=='area chart':
    # Criando o gráfico de área
    st.header('Gráfico 6 - Area chart - Preço por Produto (Top {})'.format(top_titulos))
    # Ordenando o DataFrame pelo preço em ordem decrescente e pegando as 20 primeiras linhas
    data_top20 = data.sort_values('preco', ascending=False).head(20)
    # Criando o gráfico de área
    area_chart = px.area(data_top20, x='preco', color='titulo')
    # Exibindo o gráfico
    st.plotly_chart(area_chart)


