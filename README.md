# Minimax-Algorithm

Turma da Manha (A)

- Guilherme de Sousa Cirumbolo - 00330049       
- Pedro Marhofer Alles - 00326188       

## Dependências(MUDAR)
Utilizamos apenas bibliotecas padrão do Python e não precisa da instalação de dependências externas.

Bibliotecas usadas: 

## Avaliação TicTacToe
 
- O minimax sempre ganha ou empata jogando contra o randomplayer?    
Resposta: Sim, o Minimax deve sempre ganhar ou empatar contra jogadas aleatórias. O Minimax explora todas as possibilidades do jogo e escolhe o melhor movimento possível.

- O minimax sempre empata consigo mesmo?    
Resposta: Sim, se houver uma estratégia perfeita para ambos os lados, o Minimax deve sempre empatar contra si mesmo, ja que ambos conhecem as melhores jogadas possíveis.

- O minimax não perde para você quando você usa a sua melhor estratégia?    
Resposta: Sim, o Minimax não deve perder se for implementado corretamente, pois ele calcula todas as possibilidades e sempre escolhe o movimento que evita a derrota.      

## Avaliação Othello
 
Partidas:       
Contagem de peças X Valor posicional: Posicional        
Valor posicional X Contagem de peças: Posicional              
Contagem de peças X Heurística customizada: Customizada     
Heurística customizada X Contagem de peças: Customizada     
Valor posicional X Heurística customizada: Customizada      
Heurística customizada X Valor posicional: Customizada      
 
Também  observe  e  relate  qual  implementação  foi  a  mais  bem-sucedida  de  todas: Melhor heuristica foi a customizada     

Explique  a  heurística  customizada: Equilibrar controle de bordas, estabilidade e mobilidade.Abordagem balanceada que combina aspectos das outras heurísticas.Sendo boa em todas as fases do jogo.        

Descrição do critério de parada do agente: O agente utiliza o algoritmo Minimax com Poda Alfa-Beta, limitado a uma profundidade máxima fixa de 3 níveis, sendo um compromisso entre desempenho computacional e qualidade das decisões.      

Explique a implementação escolhida para o torneio: Foi escolhida a heuristica customizada visto que eh a mais vencedora.
