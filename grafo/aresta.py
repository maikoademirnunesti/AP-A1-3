class Aresta:
    def __init__(self, vertice1, vertice2, peso):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.peso = peso

    def __str__(self):
        return f"Aresta({self.vertice1}, {self.vertice2}, {self.peso})"
