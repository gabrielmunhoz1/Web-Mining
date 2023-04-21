# AC3 - Web Mining
## Bibliotecas
- Basicamente sobre as bibliotecas estou utilizando a do streamlit para a aplicação e 2 gráficos, o pandas e  o ploty para os 4 gráficos necessários

## Arquivo
- O arquivo de script da ac3 está no path: ac3/arduinoUsinaInfo/scripts/ac3.py

## Aplicação
- A variavel "data" le a base de dados tratada
- As variáveis "top_precos" e "top_titulos" delimitam quantos valores vão ser mostrados nos gráficos abaixo
- A variável gráfico pega uma lista de todos os gráficos, sendo que na variável "escolha_do_grafico" utilizo a variavel grafico para exibir as opções
- Logo abaixo faço 6 condicionais (if) para a escolha de exibição de cada gráfico

## Gráficos
# Streamlit
- O primeiro gráfico feito pelo streamlit mostra em um gráfico de barras o preço médio por cada produto
- O segundo gráfico segue a mesma linha do primeiro, porém mostra o preço mínimo e máximo por produto

# Plotly
- O terceiro gráfico boxplot é feito pelo plotly e mostra a distribuição dos preços medios dos produtos com maiores preços
- O quarto é um gráfico de superfície, que basicamente mostra os 20 produtos com maiores preços 
- O quinto é um gráfico de linha que mostra os 20 produtos com maiores preços
- O sexto é um gráfico de area e pega os 20 produtos com maiores preços