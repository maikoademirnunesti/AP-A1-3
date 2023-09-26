from grafo.grafo import Grafo

def dfs_ciclo_euleriano(grafo, vertice, visitados):
    visitados[vertice] = True
    for vizinho in grafo.vizinhos(vertice):
        if not visitados[vizinho]:
            if dfs_ciclo_euleriano(grafo, vizinho, visitados):
                return True
    return False

def possui_ciclo_euleriano(grafo):
    if grafo.qtdArestas() == 0:
        return False

    visitados = [False] * grafo.qtdVertices()

    for vertice in range(grafo.qtdVertices()):
        if grafo.grau(vertice) % 2 != 0:
            return False

    return dfs_ciclo_euleriano(grafo, 0, visitados)

if __name__ == "__main__":
    try:
        arquivo_grafo = "grafo.txt"
        grafo = Grafo(arquivo_grafo)

        if possui_ciclo_euleriano(grafo):
            print("O grafo possui um ciclo euleriano.")
        else:
            print("O grafo não possui um ciclo euleriano.")

    except FileNotFoundError as e:
        print("Arquivo não encontrado:", e)
