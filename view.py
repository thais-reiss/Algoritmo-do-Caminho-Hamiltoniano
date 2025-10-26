from main import encontrar_caminho_hamiltoniano 
import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, List

def desenhar_grafo_com_caminho_hamiltoniano(grafo: Dict[int, List[int]], caminho: List[int]):
    G = nx.Graph()
    for u in grafo:
        for v in grafo[u]:
            if not G.has_edge(u, v):
                G.add_edge(u, v)

    pos = nx.spring_layout(G, seed=42)

    nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=700)
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=1.5)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    edge_labels = {edge: f"{edge[0]}–{edge[1]}" for edge in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')

    if caminho:
        edges_caminho = [(caminho[i], caminho[i+1]) for i in range(len(caminho)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges_caminho, edge_color='green', width=3)
        print("Caminho hamiltoniano encontrado:", " -> ".join(map(str, caminho)))
        titulo = "Grafo com caminho hamiltoniano (vértices azuis, caminho verde)"
    else:
        print("Nenhum caminho hamiltoniano encontrado.")
        titulo = "Grafo sem caminho hamiltoniano"

    plt.title(titulo, fontsize=11)
    plt.axis('off')
    plt.savefig("grafo_hamiltoniano.png", format="png", dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    grafo_exemplo = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2, 4],
        4: [3, 5],
        5: [4]
    }

    print("--- Testando Grafo de Exemplo ---")
    caminho = encontrar_caminho_hamiltoniano(grafo_exemplo) 
    desenhar_grafo_com_caminho_hamiltoniano(grafo_exemplo, caminho)
