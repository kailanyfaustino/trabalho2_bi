## Introdução 📖

Neste projeto usaremos a previsão de séries temporais para prever as vendas nas lojas com base em dados da Corporación Favorita, uma grande rede varejista de alimentos sediada no Equador.

Especificamente, o objetivo é construir um modelo que prevê com mais precisão as vendas unitárias de milhares de itens vendidos em diferentes lojas Favorita, praticando as habilidades aprendidas ao decorrer da matéria de BI com um conjunto de dados de treinamento acessível de datas, informações de loja e item, promoções e vendas unitárias.

## Fontes de dados 📊

Todos os dados para este projeto foram obtidos do [**Store Sales - Time Series Forecasting**](https://www.kaggle.com/competitions/store-sales-time-series-forecasting/data). O conjunto de dados inclui vários arquivos com informações detalhadas:

- **train.csv**: Dados de treinamento com recursos como store_nbr, family, onpromotion e sales.
- **test.csv**: Dados de teste para prever vendas futuras.
- **stores.csv**: Armazene metadados, incluindo cidade, estado, tipo e cluster.
- **oil.csv**: Preços diários do petróleo, um fator externo essencial.
- **holidays_events.csv**: Conjunto de dados de feriados e eventos, incluindo informações sobre feriados transferidos e de ponte.
e etc.
- **transactions.csv**: 



## Metodologia 🚀

Nossa abordagem para resolver esse problema inclui as seguintes etapas principais:
- **Pré-processamento e limpeza de dados**
- **Engenharia de recursos**
- **Análise Exploratória de Dados (EDA)**
- **Desenvolvimento de modelos (Qual?)**
- **Avaliação do modelo usando a raiz do erro quadrático médio (RMSE) em vez do RMSLE como métrica**

### Pré-processamento de dados 🛠️

Limpamos os dados e manipulamos valores ausentes. Além disso, mesclamos conjuntos de dados externos, como preços de petróleo e eventos de feriados.


### Treinamento e Avaliação 

- **Otimização:** Usamos o otimizador Adam com uma taxa de aprendizado de 0,001.
- **Função de perda:** Erro quadrático médio (RMSE).
- **Épocas:**.
- **Avaliação do modelo:** A métrica de avaliação final foi a Raiz do Erro Logarítmico Quadrático Médio (RMSLE).

## Resultados 📈

## Discussão: Interpretação dos resultados, limitações encontradas, e possíveis melhorias.

## Conclusão 🎯

