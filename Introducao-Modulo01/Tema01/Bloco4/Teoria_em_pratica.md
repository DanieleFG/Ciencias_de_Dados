# Teória em Pratica
### Projeto de Ia usando mineração de dados
## CRISP -DM 
1. Compreenção do negocio

O ciêntista de dados ou minerador de dados comçea identificando os objetivos e o escopo do projeto. Eles colaboram com as partes interessadas do negocio para identificar determinadas informações.

    * Problemas que precisam ser resolvidos
    * Restrições ou limitações do projeto
    * O impacto nos negocios de soluções potênciais

Eles então usam essas informações para definir metas de mineração de dados e idenificar os recursos necessarios para descoberta de conhecimento.

2. Compreenção de dados
Depois de entender o problema de negócios, os ciéntistas de dados começam a analizar preliminar dos dados . Eles coletam conjuntos de dados de varias fontes, obtem direitos de acesso e preparam um relatório de descrição de dados . O elatório inclui os tipos de dados , quantidade de requisitos de hardware e sofrware para processamento de dados . Depois que a empresa aprova o seu plano, ela começa a explorar e verificar os dados. Eles manipulam os dados usando técnicas estátisticas básicas , avaliam a quantidade dos dados e escolhem um conjunto de dados final para o poximo estagio.

3. Preparação dos dados
Os mineradors de dados gastam mais tempo nessa fase porque o softwae de mineração de daos requer dados de alta qualidade. Os processo de negocio coletam e armazenam dados por outros motivos  que não a mineração, e os mineradores de dados devem refinalos  antes de usalos para a modelagem . A preparação de dados envolve os processos a seguir .

**Limpar dados**

Por exemplo manipule dados ausentes, erros de dados , valores padrões e correções de dados .

**Integre os dados**

Combine dois conjuntos de dados diferentes para obter o conjunto de dados de destino final.

**Formatar Dados**

Converta tipos de dados ou configure dados para a tecnologia de mineração especifica que está sendo usada.

4. Modelagem de dados

Os minerados de dados insere os dados preparados no software de mineração de dadose estudam os resultados . Para fazer isso eles podem escolher entre varias tecnicas e ferramentas de mineração de dados. Eles também devem escrever testes para avaliar a qualidade dos resultados da mineração de dados. Para minerar os dados , os cientistas de dados podem:
* Treinar os modelos de machine learning (Ml) em conjunto de dados menores com resultados conhecidos.
* Usar modelos para analizar ainda mais conjuntos de dados desconhecidos.
* Ajustar e reconfigurar o softaware de mineração de dados até que os resultados sejam satisfatorios.

5. Avaliação

Depois de criar os modelos os mineradores de dados começam a medi-los em relação aos objetivos de negocio originais. Eles compartilham os resultados com os analistas de negócios e coletam feedbacks . O modelo pode responder bem a pergunta original ou mostrar padrões novos e anteriormente desconhecidos. Os mineradores de dados podem alterar o modelo , ajustar a meta de negócio ou revisitar os dados, dependendo do feedback da emmpresa. Avaliação continua , feedback e modificação fazem parte do processo de descoberta do conhecimento.

6. Implantação

Durante a implantação outras partes interessadas usam o modelo de trabalho para gerar inteligência de negócio. O ciêntista de dados planeja o processo de implantação, que inclui ensinar outras pessoas  sobre as funções do modelo, monitorar continuamente e manter a aplicação de mineração de dados . Os analistas de negócios usam a aplicação para criar relatórios para gerenciamento, compartilhar resultados com clientes e melhorar os processos de negócios. 

![IA](https://www.iteris.com.br/wp-content/uploads/2023/12/Artigo_-_Data-Mining-PT-copia.png)
https://aws.amazon.com/pt/what-is/data-mining/


Norte para resolução 

A regressão logística estima a probabilidade de ocorrência de um evento, como voto ou não voto, com base em um determinado conjunto de dados de variáveis independentes.
Esse tipo de modelo estatístico (também conhecido como modelo logit) frequentemente é usado para classificação e análise preditiva. Como o resultado é uma probabilidade, a variável dependente é limitada entre 0 e 1. Na regressão logística, uma transformação logit é aplicada à chance, isto é, a probabilidade de sucesso dividida pela probabilidade de fracasso. Isso também é comumente conhecido como chance logarítmica, ou logaritmo natural da chance, e essa função logística é representada pelas seguintes fórmulas: 

Logit(pi) = 1/(1+ exp(-pi))
ln(pi/(1-pi)) = Beta_0 + Beta_1*X_1 + … + B_k*K_k

![Regressãologistica](https://www.researchgate.net/profile/Adalberto-Dornelles-Filho/publication/313478477/figure/fig2/AS:459808735272963@1486638353290/Figura-2-Regressao-logistica-da-aplicacao-da-vocalizacao-de-l-em-funcao-da-data-de.png)


**Floresta Aleatoria (random florest)** 


Floresta aleatória é um algoritmo de machine learning comumente usado, com marca registrada por Leo Breiman e Adele Cutler, que combina a saída de várias árvores de decisão para alcançar um único resultado. Sua facilidade de uso e flexibilidade incentivaram a sua adoção, pois lida tanto com problemas de classificação quanto de regressão.
Árvores de decisão

Uma vez que o modelo de floresta aleatória é composto por várias árvores de decisão, seria útil começar por descrever o algoritmo de árvore de decisão resumidamente. As árvores de decisão começam com uma pergunta básica, como "devo navegar?" A partir daí, é possível fazer uma série de perguntas para determinar uma resposta, como "você pode perguntar uma série de perguntas para determinar uma resposta, como "as ondas são de longo período?" ou "o vento está soprando em alto mar?". Essas perguntas formam os nós de decisão na árvore, agindo como um meio de dividir os dados. Cada pergunta ajuda um indivíduo a chegar a uma decisão final, que seria indicada pelo nó folha. Observações que se enquadram nos critérios seguirão a ramificação "Sim" e aquelas que não se enquadram seguirão um caminho alternativo.  As árvores de decisão buscam a melhor divisão para criar subconjuntos de dados e elas são geralmente treinadas por meio do algoritmo de árvore de classificação e regressão (CART). Métricas, como impureza de Gini, ganho de informação ou erro quadrático médio (MSE), podem ser utilizadas para avaliar a qualidade da divisão.  

Esta árvore de decisão é um exemplo de um problema de classificação, em que os rótulo de classe são "navegar" e "não navegar".

![florest](https://miro.medium.com/v2/resize:fit:592/1*i0o8mjFfCn-uD79-F1Cqkw.png)

**Máquina vetores de suporte (SVM)**

Máquina de Vetores de Suporte (SVM, do inglês Support Vector Machine) é um algoritmo de aprendizado supervisionado usado principalmente para classificação e regressão. O objetivo principal do SVM é encontrar um hiperplano em um espaço de várias dimensões que melhor separa as classes de dados.
Como Funciona:

    Margem Máxima: O SVM tenta encontrar um hiperplano que maximize a margem entre as diferentes classes. A margem é a distância entre o hiperplano e os pontos de dados mais próximos de qualquer classe, que são chamados de vetores de suporte.
    Hiperplano: Em um problema de duas dimensões, o hiperplano é uma linha. Em um problema tridimensional, é um plano. Em espaços de dimensões superiores, é uma hipersuperfície.

Exemplos de Aplicação:

    Classificação de Imagens: O SVM pode ser usado para classificar imagens, por exemplo, diferenciando entre fotos de cães e gatos com base em características visuais extraídas das imagens.

    Análise de Sentimento: Na análise de sentimentos de textos, o SVM pode ser utilizado para classificar se uma revisão de produto é positiva ou negativa.

    Reconhecimento de Escrita Manual: SVMs são comumente usados para reconhecimento de dígitos escritos à mão, como na classificação de dígitos do banco de dados MNIST.

Exemplo de Aplicação Prática:

Suponha que você tenha um conjunto de dados com duas características que diferenciam duas classes de objetos, digamos, altura e peso para classificar pessoas como "atletas" ou "não-atletas". O SVM pode ser usado para encontrar a linha (ou hiperplano) que melhor separa essas duas classes no gráfico de altura versus peso. Depois que o modelo SVM é treinado, ele pode classificar novos dados (com base na altura e no peso) como "atleta" ou "não-atleta" de acordo com o lado do hiperplano em que os novos dados caem.

O SVM é eficaz em espaços de alta dimensionalidade e é especialmente útil em problemas onde o número de dimensões é maior que o número de amostras.
![SVM](https://media.licdn.com/dms/image/D4D12AQGvT5qGucZIZA/article-cover_image-shrink_600_2000/0/1707241213966?e=2147483647&v=beta&t=z6Nudfi0iLOzXnjzvTN-HrsXQIa0boiTSZp6myKuNIo)

**K- nearest meighbors (K-NN)**
O k-NN (k-Nearest Neighbors) é um algoritmo de aprendizado supervisionado usado principalmente para problemas de classificação e regressão. Ele é baseado na ideia de que objetos semelhantes estão próximos uns dos outros. O algoritmo classifica um novo dado com base em quão próximos estão os seus vizinhos mais próximos no espaço dos dados.
Como Funciona:

    Escolha de k: O valor de k é um parâmetro do algoritmo e determina o número de vizinhos mais próximos a considerar.
    Cálculo de Distância: Para classificar um novo ponto, o k-NN calcula a distância entre este ponto e todos os outros pontos no conjunto de dados de treinamento. As distâncias mais comuns usadas são a Euclidiana, Manhattan e Minkowski.
    Classificação: O novo ponto é classificado com base na maioria dos votos entre os k vizinhos mais próximos. Se for um problema de regressão, a média ou a mediana dos valores dos vizinhos mais próximos é usada para prever o valor do ponto.

Exemplo de Aplicação:

    Reconhecimento de Padrões: k-NN pode ser usado para o reconhecimento de dígitos manuscritos. Dado um novo dígito escrito à mão, o algoritmo compara com dígitos conhecidos (em um banco de dados como o MNIST) e classifica o novo dígito com base no dígito mais comum entre os k mais próximos.

    Diagnóstico Médico: k-NN pode ser aplicado para prever o diagnóstico de doenças. Por exemplo, se você tiver um novo paciente com certas características (como pressão arterial, idade, nível de colesterol), o k-NN pode comparar essas características com as de pacientes anteriores e prever o diagnóstico com base nos diagnósticos mais comuns entre os k pacientes mais próximos.

    Recomendação de Produtos: O k-NN pode ser utilizado em sistemas de recomendação, onde produtos similares são recomendados a um usuário com base nas preferências de usuários com perfis semelhantes.

Exemplo Prático:

Imagine que você tem um conjunto de dados de clientes de uma loja, contendo informações como idade e renda anual. Você quer classificar um novo cliente como "alto poder de compra" ou "baixo poder de compra". Com o k-NN, você calcularia a distância desse novo cliente para todos os outros clientes no conjunto de dados. O novo cliente seria classificado com base na maioria dos k vizinhos mais próximos. Por exemplo, se k=3 e dois dos três vizinhos mais próximos foram classificados como "alto poder de compra", o novo cliente seria classificado da mesma forma.


**Naive bayes**
Naive Bayes é uma família de algoritmos de classificação baseados no Teorema de Bayes, com a suposição ingênua (daí o nome "Naive") de que as características são independentes entre si. Embora essa suposição de independência raramente seja verdadeira na prática, o algoritmo ainda funciona bem em muitas aplicações, especialmente em problemas de classificação de texto.
Como Funciona:

O Naive Bayes utiliza o Teorema de Bayes para calcular a probabilidade de uma classe, dado um conjunto de características. A fórmula do Teorema de Bayes é:
P(C∣X)=P(X∣C)⋅P(C)P(X)
P(C∣X)=P(X)P(X∣C)⋅P(C)​

Onde:

    P(C∣X)P(C∣X) é a probabilidade posterior da classe CC dado o vetor de características XX.
    P(X∣C)P(X∣C) é a probabilidade de observar as características XX dado que a classe é CC.
    P(C)P(C) é a probabilidade a priori da classe CC.
    P(X)P(X) é a probabilidade das características XX ocorrerem.

Na prática, o algoritmo classifica uma nova instância ao calcular a probabilidade de cada classe possível e escolher a classe com a maior probabilidade.
Exemplos de Aplicação:

    Filtragem de Spam: O Naive Bayes é amplamente utilizado em sistemas de filtragem de spam para classificar e-mails como "spam" ou "não spam". Ele analisa palavras e frases em um e-mail e calcula a probabilidade de o e-mail ser spam com base em palavras frequentemente associadas a spam.

    Análise de Sentimento: Naive Bayes pode ser usado para classificar o sentimento em análises de texto, como comentários de clientes, revisões de produtos, tweets, etc. O algoritmo pode classificar textos como "positivo", "negativo" ou "neutro" com base em palavras e expressões usadas no texto.

    Classificação de Notícias: Pode ser utilizado para classificar artigos de notícias em diferentes categorias, como "política", "esportes", "tecnologia", etc. O modelo aprende a partir de características de texto em cada categoria e, em seguida, pode prever a categoria de novos artigos.

Exemplo Prático:

Imagine que você tenha um banco de dados de e-mails, onde alguns são marcados como spam e outros como não spam. Cada e-mail contém várias palavras que são usadas como características. O Naive Bayes pode calcular a probabilidade de um novo e-mail ser spam com base nas palavras que ele contém. Por exemplo, se palavras como "promoção", "grátis" e "clique" aparecem frequentemente em e-mails marcados como spam, o Naive Bayes atribuiria uma alta probabilidade de que um novo e-mail contendo essas palavras seja spam.

Embora o Naive Bayes seja baseado em uma suposição simplificada, ele é muito eficaz, especialmente quando aplicado a problemas de alta dimensionalidade, como classificação de textos.
![naive](https://i.ytimg.com/vi/O2L2Uv9pdDA/maxresdefault.jpg)



