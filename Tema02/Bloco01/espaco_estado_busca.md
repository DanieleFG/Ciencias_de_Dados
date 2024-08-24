# Espaço de busca

**Vamos Refletir**

Quando vc joga um jogo de quebra cabeça , como o cubo mágico , está realizando uma busca para encontrar uma solução. Como os conceitos de espaço e estados de busca se aplicam a situaçẽs cotidianas como esta?

* Representação abstrata  de todas as possiveis soluiões para um problema.
* Em um espaço d ebusca , cada ponto representa um estado possivel do sistema ou uma configuraçãi.
* Por exemplo , no contexto de um quebra cabeça , como um cubo mágico, o espaço de busca incluiria todas as combinações possiveis das peças.
* São os pontos especificos no espaço de busca.
* Representa uma configuração ou uma etapa no processo de resolução do probelma. 
* No exemplo do quebra cabeça ou do cubo mágico, um estado de busca seria uma determinada configuração das cores da face do cubo. 
* Os estados de busca são conectados  por operadores o
u ações que podem ser aplicados para mover-se de um estado para o outro. 

O conceito de Busca em Espaço de Estados refere-se a uma técnica de resolução de problemas em inteligência artificial (IA) e ciência da computação, onde o problema é modelado como um espaço de estados. Cada estado representa uma configuração possível do problema, e a busca consiste em encontrar uma sequência de estados (ou caminho) que leva de um estado inicial a um estado objetivo (ou solução).
Conceitos-Chave:

---------
    Espaço de Estados: É o conjunto de todos os estados possíveis que podem ser alcançados a partir do estado inicial do problema. Cada estado é uma representação completa do sistema em um determinado ponto.

    Estado Inicial: O ponto de partida da busca. É a configuração inicial do problema que deve ser transformada em uma solução.

    Estado Objetivo: O(s) estado(s) que representam a solução do problema.

    Operadores: São ações que podem ser aplicadas a um estado para gerar novos estados. Cada operador transforma o estado atual em um novo estado.

    Caminho: Uma sequência de estados que leva do estado inicial ao estado objetivo.

    Função de Custo: (Opcional) Em alguns problemas, há uma função que atribui um custo a cada caminho, e o objetivo é encontrar o caminho com o menor custo.

Tipos de Busca:

    Busca Cega (ou Não-Informada): Não utiliza nenhuma informação adicional além do espaço de estados e dos operadores. Exemplos incluem busca em largura (BFS) e busca em profundidade (DFS).

    Busca Informada (ou Heurística): Utiliza uma função heurística que estima o custo de alcançar o estado objetivo a partir de um determinado estado. Exemplos incluem o algoritmo A* e a busca gulosa.

Exemplo de Aplicação:

Quebra-cabeça de 8 Peças:

    Espaço de Estados: Todas as configurações possíveis do quebra-cabeça.
    Estado Inicial: A configuração inicial do quebra-cabeça.
    Estado Objetivo: A configuração ordenada do quebra-cabeça.
    Operadores: Movimentos possíveis de uma peça para um espaço vazio adjacente.
    Caminho: A sequência de movimentos que resolve o quebra-cabeça.

A Busca em Espaço de Estados é uma abordagem fundamental em muitos algoritmos de IA para resolver problemas de otimização, planejamento, jogos, entre outros, onde o objetivo é explorar sistematicamente os possíveis estados para encontrar a solução mais eficiente.

## Busca não Informada
Busca não informada (ou busca cega) refere-se a uma categoria de algoritmos de busca que exploram o espaço de estados sem utilizar informações adicionais ou heurísticas sobre a distância ou o custo para chegar ao estado objetivo. Esses algoritmos simplesmente seguem regras de exploração predefinidas e não têm conhecimento específico sobre a "proximidade" da solução. Eles exploram o espaço de estados de maneira sistemática, sem se guiar por estimativas de quão perto estão da solução.
Principais Características:

    Exploração Sistemática: A busca não informada explora o espaço de estados de forma sistemática, garantindo que todos os estados possíveis sejam considerados (eventualmente), mas sem priorizar estados que possam parecer mais promissores.
    Ausência de Heurísticas: Esses algoritmos não usam nenhuma função heurística para guiar a busca. Em vez disso, eles baseiam-se em critérios como profundidade ou ordem de descoberta dos estados.

Exemplos de Algoritmos de Busca Não Informada:

    Busca em Largura (Breadth-First Search, BFS):
        Como Funciona: Explora o espaço de estados nível por nível. Começa no estado inicial e explora todos os estados a uma profundidade de 1, depois todos os estados a uma profundidade de 2, e assim por diante.
        Aplicação: Ideal para encontrar o caminho mais curto em um grafo não ponderado. Por exemplo, em um labirinto, BFS pode ser usada para encontrar o caminho mais curto da entrada até a saída.

    Busca em Profundidade (Depth-First Search, DFS):
        Como Funciona: Explora o espaço de estados ao ir o mais fundo possível ao longo de um ramo antes de retroceder. Se atinge um estado sem filhos (ou um caminho sem saída), volta para o último estado com filhos não explorados.
        Aplicação: Útil para problemas onde a solução está localizada em um caminho profundo. Por exemplo, para percorrer todas as combinações possíveis de movimentos em um quebra-cabeça de Sudoku.

    Busca Cega Iterativa (Iterative Deepening Search, IDS):
        Como Funciona: Combina as abordagens da busca em profundidade e busca em largura. Realiza uma série de buscas em profundidade limitadas, aumentando progressivamente o limite de profundidade até encontrar a solução.
        Aplicação: Ideal quando a profundidade da solução não é conhecida e é preciso economizar memória, como em problemas de planejamento em jogos.

    Busca de Custo Uniforme (Uniform-Cost Search, UCS):
        Como Funciona: Explora o espaço de estados de forma que o próximo nó a ser explorado seja sempre o de menor custo acumulado desde o início. Pode ser visto como uma generalização da BFS que considera o custo dos caminhos.
        Aplicação: Usada em problemas onde os caminhos têm custos diferentes. Por exemplo, para encontrar o caminho mais barato em um mapa de rotas de transporte onde as distâncias ou tempos variam.

Exemplo Prático de Busca Não Informada:

Imagine que você está em uma cidade tentando encontrar um endereço específico sem um mapa (sem nenhuma informação sobre a localização exata do endereço). Se você usasse a busca em largura (BFS), você exploraria sistematicamente todas as ruas adjacentes ao seu ponto de partida antes de seguir para ruas mais distantes. Se usasse a busca em profundidade (DFS), você seguiria uma rua até o fim antes de voltar e tentar uma nova.

Esses métodos garantem que eventualmente você encontrará o endereço, mas sem qualquer conhecimento prévio sobre onde ele está, o processo pode ser demorado e não otimizado.


## Busca Informada

Busca informada é uma categoria de algoritmos de busca que utiliza informações adicionais, chamadas de heurísticas, para guiar a exploração do espaço de estados de forma mais eficiente em direção ao estado objetivo. Ao contrário da busca não informada, que explora o espaço de maneira sistemática sem conhecimento prévio, a busca informada usa estimativas de custo ou proximidade para priorizar certos caminhos que parecem mais promissores, o que pode reduzir significativamente o tempo e o espaço necessários para encontrar a solução.
Principais Características:

    Uso de Heurísticas: A busca informada utiliza uma função heurística, que é uma estimativa do custo para alcançar o objetivo a partir de um determinado estado. Essa função não precisa ser exata, mas deve ser eficiente e "boa o suficiente" para guiar a busca.
    Exploração Direcionada: Em vez de explorar todos os estados uniformemente, a busca informada prioriza aqueles que, de acordo com a heurística, estão mais próximos ou são mais promissores em relação ao objetivo.

Exemplos de Algoritmos de Busca Informada:

    Algoritmo A*
        Como Funciona: Combina a busca de custo uniforme com uma heurística. Para cada estado, o A* calcula o valor f(n)=g(n)+h(n)f(n)=g(n)+h(n), onde:
            g(n)g(n) é o custo acumulado desde o estado inicial até o estado nn.
            h(n)h(n) é a estimativa (heurística) do custo restante para chegar ao estado objetivo a partir do estado nn.
        Aplicação: A* é amplamente utilizado em problemas de caminho mínimo, como encontrar a rota mais curta em um mapa de estradas. Por exemplo, em sistemas de navegação GPS, onde o objetivo é encontrar a rota mais rápida entre dois pontos.

    Algoritmo de Busca Gulosa (Greedy Best-First Search)
        Como Funciona: Seleciona o próximo estado para explorar com base apenas na heurística h(n)h(n), ou seja, escolhe o estado que parece estar mais próximo do objetivo, sem considerar o custo já acumulado.
        Aplicação: É usado em problemas onde é mais importante chegar rapidamente a uma solução aceitável do que encontrar a solução ótima. Por exemplo, em jogos de tabuleiro como o xadrez, onde pode ser usado para fazer uma jogada rápida que pareça promissora, mesmo que não seja a melhor jogada possível.

    Busca Heurística
        Como Funciona: Qualquer algoritmo que utiliza uma função heurística para guiar a busca pode ser considerado uma busca heurística. Isso inclui variantes do A* ou da busca gulosa.
        Aplicação: Pode ser aplicada em problemas de planejamento, onde o objetivo é atingir um estado final desejado a partir de um estado inicial, como planejar uma sequência de ações para alcançar uma meta em robótica ou automação.

Exemplo Prático de Busca Informada:

Imagine que você está novamente em uma cidade tentando encontrar um endereço, mas desta vez você tem um mapa com estimativas de distância até o endereço desejado. Se você usasse o algoritmo A*, você escolheria explorar as ruas que minimizam a soma da distância percorrida até agora e a distância estimada restante até o destino. Se você usasse a busca gulosa, escolheria explorar a rua que parece estar mais próxima do endereço final, sem considerar o caminho já percorrido.
Diferença entre Busca Informada e Não Informada:

    Busca Informada: Utiliza heurísticas para guiar a busca, geralmente resultando em uma exploração mais eficiente e rápida.
    Busca Não Informada: Explora o espaço de estados de forma sistemática e completa, mas pode ser ineficiente, especialmente em espaços grandes.

A busca informada é fundamental em muitas aplicações práticas, como planejamento em IA, jogos de estratégia, e sistemas de recomendação, onde a eficiência e a qualidade da solução são cruciais.