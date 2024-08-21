# Aprendizado por reforço

* Agente:

É o sistema de IA que está aprendendo a interagir com o ambiente e tomar ações.
Toma decisões com base em politicas para maximizar a recompensa.

* Ambiente:

É o mundo com o qual o agente interage.
Real (por exemplo, um robo em um ambiente físico).
Simulado (por exemplo , um jogo de computador).

* Recompensa:

É uma medida numérica que o ambiente  fornece ao agente após cada ação tomada.

* Politica:

É a estratégia ao plano que o agente segue para tomar decisões.
Ela mapeia estados (ou observações) do ambiente para a ação que i agente deve tomar.

## Cenário de utilização

* Agente: 
 Um pequeno robô controlado por um programa de IA.

* Ambiente: 

 Um tabuleiro quadrado com várias células, algumas contendo obstáculos e uma contendo o tesouro.

* Recompensa:
* O agente recebe uma recompensa positiva quando encontra o tesouro e uma recompensa negativa ao colidir com obstáculos ou sair do tabuleiro.

* Objetivo: 

O objetivo do agente é aprender a política (estratégia) que maximiza sua recompensa cumulativa ao longo do tempo, ou seja, encontrar o tesouro com o mínimo possível de colisões.

* Inicialização:

O agente começa sem conhecimento sobre o ambiente. 

Ele explora o ambiente fazendo ações aleatórias.

* Recompensas: 

O agente recebe recompensas após cada ação. 

Ele aprende que colidir com obstáculos ou sair do tabuleiro resulta em recompensas negativas, enquanto encontrar o tesouro resulta em uma recompensa positiva.
* Aprendizado da política:

O agente usa um algoritmo de aprendizado por reforço para ajustar sua política com base nas recompensas recebidas. 

Ele tenta maximizar as recompensas esperadas, aprendendo a evitar obstáculos e procurar o tesouro.

* Explorationversus exploitation: 

O agente enfrenta o dilema de explorar novas ações (como tentar uma célula desconhecida) versus explorar ações conhecidas (como escolher uma célula que já sabe ser segura). 

Ele deve encontrar o equilíbrio certo para maximizar a recompensa cumulativa.

* Aprimoramento gradual: 

Com o tempo, o agente aprimora sua política à medida que aprende a tomar decisões mais inteligentes com base em suas experiências passadas.


1. O aprendizado por reforço envolve um agente que interage com um ambiente e recebe recompensas.
A caracteristica fundamental so aprendizado por reforço, em que um agente toma ações em um ambiente , recebe recompensas com base em suas ações e aprende a otimizar seu comportamento para maximizar essas recompensas.
