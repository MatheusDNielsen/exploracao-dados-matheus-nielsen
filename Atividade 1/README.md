# Introdução

O presente relatório apresenta uma análise exploratória do conjunto de dados sobre acidentes ferroviários ocorridos no Brasil entre 2004 e 2020, obtido no portal oficial Dados.gov.br.
A escolha do dataset foi motivada tanto pelo interesse pessoal do pesquisador por sistemas ferroviários quanto pela relevância pública do tema, considerando o impacto social, econômico e humano dos acidentes em linhas férreas.

# Metodologia

Foi realizada uma análise estatística exploratória utilizando Python com as bibliotecas:
- Pandas
- Numpy
- Matplotlib
- Seaborn

Com as seguintes etapas executadas:
- Cálculo de estatísticas descritivas
- Tratamento de valores ausentes
- Análise de frequência de acidentes por concessionária
- Análise de frequência de natureza dos acidentes
- Comparação entre natureza do acidente e número de feridos
- Comparação entre natureza do acidente e número de óbitos
- Visualização por meio de gráficos de barras, histogramas e boxplots

# Resultados

A análise revelou que as categorias de acidentes com maior número de feridos foram:
- Atropelamento
- Abalroamento

Essas categorias apresentaram as maiores médias e totais de pessoas feridas ao longo do período analisado.

# Discussão

Os resultados sugerem que uma parcela significativa dos ferimentos está associada a eventos envolvendo interação direta entre trens e pessoas ou veículos em cruzamentos.

A predominância de atropelamentos e abalroamentos pode indicar:
- Falhas na sinalização de passagens em nível
- Deficiência na comunicação visual e sonora de aproximação de trens
- Ausência de barreiras físicas adequadas
- Problemas de fiscalização ou conscientização pública

Embora a análise seja exploratória e não permita estabelecer causalidade direta, os dados apontam para possíveis fragilidades no sistema de segurança das travessias ferroviárias no Brasil.

# Limitações
Presença de valores ausentes em algumas categorias
Possíveis inconsistências de registro ao longo dos anos
Ausência de variáveis complementares (ex.: localização detalhada, infraestrutura da travessia, fluxo de veículos)

# Conclusão
A análise do dataset de acidentes ferroviários (2004–2020) indica que atropelamentos e abalroamentos são as principais naturezas associadas ao maior número de feridos.

Os resultados sugerem a necessidade de maior atenção às travessias ferroviárias, especialmente no que se refere à comunicação, sinalização e mecanismos de prevenção.

Estudos futuros podem aprofundar a investigação incluindo variáveis regionais, infraestrutura local e evolução temporal das ocorrências.
