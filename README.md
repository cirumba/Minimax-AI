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
-  Para  o  Othello,  faça  um  mini-torneio  entre  os  algoritmos  (minimax  com  as  três  heurísticas), 
considerando as partidas abaixo. Para cada partida, relate quem venceu e o número de peças final de 
cada  agente.  Note  que  os  mesmos  oponentes  se  enfrentam  duas  vezes,  em  cada  uma  delas,  cada 
oponente começa jogando uma vez. 
 
Partidas: 
Contagem de peças X Valor posicional: 
Valor posicional X Contagem de peças: 
Contagem de peças X Heurística customizada: 
Heurística customizada X Contagem de peças: 
Valor posicional X Heurística customizada: 
Heurística customizada X Valor posicional: 
 
Também  observe  e  relate  qual  implementação  foi  a  mais  bem-sucedida  de  todas  (a  que  mais  teve 
vitórias e, caso tenha empate nesse critério, a que mais capturou peças). 
- Explique  a  heurística  customizada  e,  caso  tenha  sido  utilizada  alguma  fonte  (como 
artigo ou site), indique a fonte também, explicando como as fontes foram utilizadas (a 
heurística foi utilizada conforme apresentada na fonte, foi uma combinação de ideias 
de fontes diferentes, foi totalmente projetada pelo grupo, sem utilização de fontes,...);  
- descrição do critério de parada do agente (profundidade máxima fixa? 
aprofundamento iterativo parado por tempo?etc); 
- Resultado da avaliação (ver item “b” da seção 2.3); 
- Explique a implementação escolhida para o torneio. 
