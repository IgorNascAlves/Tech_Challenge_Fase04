# Índice
- [O Problema](#o-problema)
- [Cronograma](#cronograma)
  - [Tarefas](#tarefas)
- [Estrutura de pastas](#estrutura-de-pastas)
- [Referências](#referências)


# O Problema

Você foi contratado(a) para uma consultoria, e seu trabalho envolve analisar os dados de preço do petróleo brent, que pode ser encontrado no [site do ipea](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view). Essa base de dados histórica envolve duas colunas: data e preço (em dólares).

Um grande cliente do segmento pediu para que a consultoria desenvolvesse um dashboard interativo e que gere insights relevantes para tomada de decisão. Além disso, solicitaram que fosse desenvolvido um modelo de Machine Learning para fazer o forecasting do preço do petróleo.

**Seu objetivo é:**

* Criar um dashboard interativo com ferramentas à sua escolha.

* Seu dashboard deve fazer parte de um storytelling que traga insights relevantes sobre a variação do preço do petróleo, como situações geopolíticas, crises econômicas, demanda global por energia e etc. Isso pode te ajudar com seu modelo. **É obrigatório que você traga pelo menos 4 in-sights neste desafio**.

* Criar um modelo de Machine Learning que faça a previsão do preço do petróleo diariamente (lembre-se de time series). Esse modelo deve estar contemplado em seu storytelling e deve conter o código que você trabalhou, analisando as performances do modelo.

* Criar um plano para fazer o deploy em produção do modelo, com as ferramentas que são necessárias.

* Faça um MVP do seu modelo em produção utilizando o Streamlit.


# Cronograma


| Data | Semana | Atividade |
| --- | --- | --- |
| 13/11 | Semana 7 | Download base, montar cronograma e criar repositório |
| 20/11 | Semana 6 | Análise exploratória |
| 27/11 | Semana 5 | Criar um dashboard |
| 04/12 | Semana 4 | Modelo de Machine Learning |
| 11/12 | Semana 3 | MVP Streamlit |
| 18/12 | Semana 2 | Criar relatório |
| 25/12 | Semana - | Sem atividades |
| 01/01 | Semana - | Sem atividades |
| 08/01 | Semana 1 | Ajustes finais |
| 12/01 | Semana 1 | Entregar o projeto |
| 15/01 | Semana 0 | Data Final |


## Tarefas

- [x] Download base 
- [x] Montar cronograma 
- [x] Criar repositório
- [ ] Análise exploratória
- [ ] Criar um dashboard
- [ ] Modelo de Machine Learning
- [ ] Plano de deploy em produção do modelo
- [ ] MVP Streamlit
- [ ] 4 in-sights sobre o desafio
- [ ] Criar relatório
- [ ] Ajustes finais
- [ ] Entregar o projeto

# Estrutura de pastas

```bash
├── README.md               <- apresentação do projeto
│
├── data                    <- dados usados no projeto
│
├── notebooks               <- Jupyter notebooks
│
├── dashboards              <- arquivos de dashboard
│
├── relatórios              <- arquivos de relatório
│
├── src                     <- código-fonte do projeto
│
└── requirements.txt        <- pacotes utilizados no projeto
```

# Referências

* [Ipeadata](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view)
* [Documentação Power BI](https://docs.microsoft.com/pt-br/power-bi/)
* [Documentação Streamlit](https://docs.streamlit.io/en/stable/)
