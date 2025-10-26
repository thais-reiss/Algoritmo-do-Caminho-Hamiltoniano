def encontrar_caminho_hamiltoniano(grafo):

    total_vertices = len(grafo)
    
    if total_vertices == 0:
        return [] 

    caminho_atual = []
    
    visitados = set()
    
    for no_inicial in grafo:
        
        if backtrack(grafo, total_vertices, no_inicial, caminho_atual, visitados):
            return caminho_atual

    return None

def backtrack(grafo, total_vertices, vertice_atual, caminho_atual, visitados):

    caminho_atual.append(vertice_atual)
    visitados.add(vertice_atual)
    
    if len(caminho_atual) == total_vertices:
        return True  

    for vizinho in grafo[vertice_atual]:
        if vizinho not in visitados:

            if backtrack(grafo, total_vertices, vizinho, caminho_atual, visitados):
                return True 
                
    caminho_atual.pop()       
    visitados.remove(vertice_atual) 
    
    return False

