# Introdução

O presente projeto tem como objetivo desenvolver um pipeline completo com análise e modelagem preditiva de um conjunto de dados relacionados às variáveis do vinho tinto português. O dataset utiliza o Wine Quality, contendo N amostras de vinhos com 11 características físico-químicas (como teor alcoólico, acidez volátil, pH, sulfatos, entre outras) e uma nota de qualidade atribuída por especialistas (de 1 a 10).

# Problema
O problema foi formulado como uma tarefa de classificação binária supervisionada, onde precisa desenvolver um modelo de classificação binária capaz de prever se um vinho é de alta qualidade (nota ≥ 7) ou de baixa/média qualidade (nota < 7). Essa simplificação permite focar no desafio mais relevante para a indústria: identificar quais vinhos atendem ao padrão de alta qualidade, assim, o modelo visa auxiliar vinícolas na triagem de lotes, redução de custos de análise sensorial e tomada de decisões em tempo real durante a produção.
SW
O dataset apresenta um desequilíbrio significativo entre as classes, com aproximadamente 86% dos vinhos classificados como baixa/média qualidade e apenas 13,5% como alta qualidade, como pode ser observado no gráfico 1, o que exige a aplicação de estratégias específicas de balanceamento. 
