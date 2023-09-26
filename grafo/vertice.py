class Vertice:
    def __init__(self, indice, rotulo):
        self.indice = indice
        self.rotulo = rotulo

    def __str__(self):
        return f"V{self.indice}: {self.rotulo}"
