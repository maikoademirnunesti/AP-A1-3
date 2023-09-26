from grafo.grafo import Grafo
from ciclo_euleriano import possuiCicloEuleriano, encontrarCicloEuleriano

def main():
    grafo = Grafo()
    grafo.ler("grafo.txt")

    if possuiCicloEuleriano(grafo):
        print("O grafo possui um ciclo euleriano.")
        ciclo = encontrarCicloEuleriano(grafo)
        print("Sequência do ciclo euleriano:", ciclo)
    else:
        print("O grafo não possui um ciclo euleriano.")

if __name__ == "__main__":
    main()
