from FileReader import FileReader
from Basicos.bubble import BubbleSort

if __name__ == "__main__":
    file_reader = FileReader("numeros_aleatorios.txt")
    desordenado = file_reader.read_numbers()
    if desordenado:
        print("Lista antes da ordenação:", desordenado)
        BubbleSort.sort(desordenado)
        print("Lista ordenada:", desordenado)
