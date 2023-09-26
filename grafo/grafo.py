from grafo.vertice import Vertice

# Para criar um vértice
vertice1 = Vertice(1, "A")


class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.arestas = [ [] for _ in range(num_vertices) ]

    def adicionarAresta(self, vertice1, vertice2):
        self.arestas[vertice1].append(vertice2)
        self.arestas[vertice2].append(vertice1)

    def qtdVertices(self):
        return self.num_vertices

    def qtdArestas(self):
        return sum(len(vertice) for vertice in self.arestas) // 2

    def grau(self, v):
        return len(self.arestas[v])

    def rotulo(self, v):
        return v

    def vizinhos(self, v):
        return self.arestas[v]

    def haAresta(self, u, v):
        return v in self.arestas[u]

    def ler(self, arquivo):
        try:
            with open(arquivo, "r") as file:
                num_vertices = int(file.readline())
                grafo = Grafo(num_vertices)

                for linha in file:
                    vertice1, vertice2 = map(int, linha.strip().split())
                    grafo.adicionarAresta(vertice1, vertice2)

            return grafo

        except FileNotFoundError as e:
            print("Arquivo não encontrado:", e)

if __name__ == "__main__":
    arquivo_grafo = "grafo.txt"
    grafo = Grafo(arquivo_grafo)

    print("Número de vértices no arquivo:", grafo.qtdVertices())
    print("Número de arestas no arquivo:", grafo.qtdArestas())

    for vertice in range(grafo.qtdVertices()):
        print(f"Grau do vértice {vertice}: {grafo.grau(vertice)}")
        print(f"Rótulo do vértice {vertice}: {grafo.rotulo(vertice)}")
        print(f"Vizinhos do vértice {vertice}: {grafo.vizinhos(vertice)}")
