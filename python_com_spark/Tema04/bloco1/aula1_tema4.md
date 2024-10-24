# Introdução à análise estatística dos dados

Segundo Haslwanter (2016), estatística é a prática ou ciência de coletar e analisar dados numéricos, para extração de proporções, representação e interpretação do todo, por meio de amostras.
Algumas métricas:
* Média, mediana, moda, desvio e variância.
* Distribuição.
* Amplitude.
* Significância.

## Módulos Python
### Módulos utilizados:
* NumPy.
* Pandas.
* SciPy.
* Matplotlib.
* Statsmodels

1. Média

A média (ou média aritmética) é uma medida de tendência central que indica o valor médio de um conjunto de dados. Ela é calculada somando todos os valores de um conjunto e dividindo pelo número total de valores.

Fórmula:
Meˊdia=∑Xn
Meˊdia=n∑X​

Onde:

    ∑X∑X é a soma de todos os valores no conjunto.
    nn é o número total de valores.

Exemplo:
Para os dados: 10, 20, 30, a média seria:
Meˊdia=10+20+303=603=20
Meˊdia=310+20+30​=360​=20

A média nos dá uma ideia geral de onde estão concentrados os valores.
2. Mediana

A mediana é o valor central de um conjunto de dados ordenados. Diferente da média, ela não é afetada por valores extremos (outliers).

    Se o número de valores no conjunto for ímpar, a mediana é o valor que está exatamente no meio.
    Se o número for par, a mediana é a média dos dois valores centrais.

Exemplo:
Para o conjunto de dados ordenados: 10, 20, 30, a mediana é 20 (valor do meio).
Para o conjunto: 10, 20, 30, 40, a mediana é:
Mediana=20+302=25
Mediana=220+30​=25

A mediana nos mostra onde está o centro dos dados, levando em consideração sua ordem.
3. Moda

A moda é o valor que aparece com maior frequência em um conjunto de dados.

    Se todos os valores ocorrem a mesma quantidade de vezes, o conjunto não tem moda.
    Se mais de um valor aparece com a mesma maior frequência, o conjunto tem múltiplas modas.

Exemplo:
Para os dados: 10, 20, 20, 30, a moda é 20 (pois aparece duas vezes, mais que os outros valores).
Se tivermos: 10, 20, 20, 30, 30, então temos duas modas: 20 e 30.

A moda é útil para identificar o valor mais comum em um conjunto de dados.
4. Desvio padrão

O desvio padrão mede a dispersão dos dados em torno da média, ou seja, o quão espalhados os dados estão. Ele mostra a variação dos dados em relação à média do conjunto.

    Um desvio padrão baixo indica que os valores estão próximos da média.
    Um desvio padrão alto indica que os valores estão mais dispersos.

Fórmula:
Desvio Padra˜o=∑(X−μ)2n
Desvio Padra˜o=n∑(X−μ)2​
​

Onde:

    XX são os valores do conjunto.
    μμ é a média.
    nn é o número total de valores.

Exemplo:
Para os dados: 10, 20, 30, a média é 20. O desvio padrão calcula o quanto os valores se distanciam dessa média.

O desvio padrão é importante para saber se os dados variam muito ou pouco em relação à média.
5. Variância

A variância mede a dispersão dos dados de forma similar ao desvio padrão, mas sem aplicar a raiz quadrada no cálculo. Ela representa o "quadrado do desvio padrão". Como resultado, a variância expressa o grau de variação de forma mais amplificada.

Fórmula:
Variaˆncia=∑(X−μ)2n
Variaˆncia=n∑(X−μ)2​

A única diferença em relação ao desvio padrão é a ausência da raiz quadrada. A variância é sempre não negativa.

Exemplo:
Se o desvio padrão for 5, a variância será 52=2552=25.

A variância é útil para comparar a dispersão de diferentes conjuntos de dados, especialmente em relação a dados que têm unidades diferentes, já que ela amplifica as diferenças.
Resumo visual:

    Média: Ponto de equilíbrio dos valores (soma total dividida pelo número de valores).
    Mediana: Valor do meio de um conjunto ordenado (ou média dos dois valores centrais se o conjunto for par).
    Moda: Valor que mais se repete.
    Desvio padrão: Mostra o quão longe os valores estão da média (medida de dispersão).
    Variância: Quão dispersos os valores estão da média, mas expressa em termos amplificados (quadrado do desvio padrão).

Esses conceitos são essenciais para descrever a distribuição de dados e suas características centrais e dispersões em qualquer análise estatística.

1. Distribuição

A distribuição em estatística refere-se à maneira como os dados são organizados ou dispersos ao longo de um conjunto de valores possíveis. Ela descreve a frequência com que diferentes valores ou intervalos de valores ocorrem em um conjunto de dados.

Existem vários tipos de distribuições, algumas comuns incluem:

    Distribuição normal (ou gaussiana): A famosa "curva em forma de sino", onde os dados se concentram em torno da média e têm simetria nos dois lados.
    Distribuição uniforme: Todos os valores dentro de um intervalo têm a mesma probabilidade de ocorrer.
    Distribuição binomial: Relacionada a experimentos com dois possíveis resultados (como sucesso e fracasso).

Exemplo: Se coletarmos as alturas de 100 pessoas e construirmos um gráfico de frequência (histograma), esse gráfico mostrará como as alturas estão distribuídas — ou seja, quantas pessoas possuem alturas em determinados intervalos.
2. Amplitude

A amplitude é uma medida da dispersão ou do intervalo dos valores em um conjunto de dados. Ela indica a diferença entre o maior e o menor valor.

Fórmula:
Amplitude=Valor maˊximo−Valor mıˊnimo
Amplitude=Valor maˊximo−Valor mıˊnimo

Exemplo: Se o conjunto de dados é 10, 15, 20, 25, 30, a amplitude seria:
Amplitude=30−10=20
Amplitude=30−10=20

A amplitude nos dá uma ideia da extensão total dos valores em um conjunto. Porém, ela não mostra a variação interna entre os dados, apenas os extremos.
3. Significância

Na estatística, a significância refere-se à probabilidade de que um resultado observado em um conjunto de dados não tenha ocorrido por acaso, ou seja, que exista uma diferença ou efeito real.

A significância estatística é medida por um valor-p (p-value). Em geral, um resultado é considerado estatisticamente significativo quando o valor-p é menor do que um limiar definido (geralmente 0,05 ou 5%). Isso significa que há menos de 5% de chance de o resultado ter ocorrido por acaso.

Exemplo: Se realizamos um teste para comparar a eficácia de dois medicamentos, e o valor-p obtido é 0,03, isso indica que há uma probabilidade de 3% de que a diferença entre os medicamentos tenha ocorrido por acaso. Como o valor é menor que 0,05, podemos dizer que a diferença é significativa.

Significância é essencial em testes de hipóteses, onde se avalia se os resultados de um experimento ou estudo são confiáveis.
Resumo:

    Distribuição: A forma como os dados estão organizados ou espalhados em relação a seus valores possíveis. Pode ser visualizada através de gráficos como histogramas ou curvas de distribuição.
    Amplitude: A diferença entre o valor máximo e o valor mínimo de um conjunto de dados. Mede a extensão total dos dados.
    Significância: Em estatística, refere-se à probabilidade de um resultado ser verdadeiro e não ocorrer por acaso, avaliado por meio de testes de hipóteses e valor-p.