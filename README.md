#Algoritmo para encontrar um Caminho Hamiltoniano em um grafo
##O que é este projeto?
Este projeto apresenta uma implementação em Python de um algoritmo capaz de identificar um Caminho Hamiltoniano em um grafo, quando este existe, e de visualizar o grafo gerado. Além disso, o projeto inclui um
relatório técnico detalhado sobre o algoritmo, abordando:

-a análise da complexidade computacional,
-a determinação da complexidade assintótica,
-a aplicação do Teorema Mestre,
-e a análise de diferentes casos de complexidade do algoritmo. 

 ##O que é Caminho Hamiltoniano?
 Um caminho hamiltoniano é um caminho que passa por cada vértice de um grafo exatamente uma vez. Encontrá-lo é um desafio, pois não se conhece um algoritmo eficiente em tempo polinomial para resolvê-lo em casos gerais.
 Existem heurísticas e técnicas para tentar encontrá-lo, dentre elas, o Backtracking, que foi a técnica usada neste projeto. Essa técnica envolve busca com retrocesso, pois ela explora todas as sequências possíveis de
 vértices, sendo que para cada vértice ela tenta construir o caminho recursivamente, voltando atrás se uma escolha não levar à solução. 
