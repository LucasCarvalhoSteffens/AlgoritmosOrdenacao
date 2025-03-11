from FileReader import FileReader
from Basicos.Bubble import BubbleSort
#from Basicos.Selection import SelectionSort
#from Basicos.Insertion import InsertionSort

if __name__ == "__main__":
    file_reader = FileReader("numeros_aleatorios.txt")
    desordenado = file_reader.read_numbers()
    
    if desordenado:
        print("Lista antes da ordenação:", desordenado)
        
        print("Escolha o algoritmo de ordenação:")
        print("1 - Bubble Sort")
        print("2 - Selection Sort")
        print("3 - Insertion Sort")
        escolha = input("Digite o número correspondente: ")
        
        if escolha == "1":
            BubbleSort.sort(desordenado)
        elif escolha == "2":
            SelectionSort.sort(desordenado)
        elif escolha == "3":
            InsertionSort.sort(desordenado)
        else:
            print("Opção inválida! Usando Bubble Sort por padrão.")
            BubbleSort.sort(desordenado)
        
        print("Lista ordenada:", desordenado)