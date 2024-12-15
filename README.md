# Minimax-Algorithm

Turma da Manha (A)

- Guilherme de Sousa Cirumbolo - 00330049       
- Pedro Marhofer Alles - 00326188       

## Dependências(MUDAR)
Utilizamos apenas bibliotecas padrão do Python e não precisa da instalação de dependências externas.

Bibliotecas usadas: 

## Avaliação 
 
- O minimax sempre ganha ou empata jogando contra o randomplayer?    
Resposta: Sim, o Minimax deve sempre ganhar ou empatar contra jogadas aleatórias. O Minimax explora todas as possibilidades do jogo e escolhe o melhor movimento possível.

- O minimax sempre empata consigo mesmo?    
Resposta: Sim, se houver uma estratégia perfeita para ambos os lados, o Minimax deve sempre empatar contra si mesmo, ja que ambos conhecem as melhores jogadas possíveis.

- O minimax não perde para você quando você usa a sua melhor estratégia?    
Resposta: Sim, o Minimax não deve perder se for implementado corretamente, pois ele calcula todas as possibilidades e sempre escolhe o movimento que evita a derrota.      

## Othello
- Explique  a  heurística  customizada  e,  caso  tenha  sido  utilizada  alguma  fonte  (como 
artigo ou site), indique a fonte também, explicando como as fontes foram utilizadas (a 
heurística foi utilizada conforme apresentada na fonte, foi uma combinação de ideias 
de fontes diferentes, foi totalmente projetada pelo grupo, sem utilização de fontes,...);  
- descrição do critério de parada do agente (profundidade máxima fixa? 
aprofundamento iterativo parado por tempo?etc); 
- Resultado da avaliação (ver item “b” da seção 2.3); 
- Explique a implementação escolhida para o torneio. 
- Extras: Relate qualquer item opcional (como implementação do MCTS) ou melhoria 
não mencionada (técnicas adicionais para melhorar o minimax não vistas em aula) que 
você tenha realizado e, caso tenha utilizado fontes extras para auxiliar, mencione as 
fontes e como foram utilizadas.