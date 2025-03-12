from FileReader import FileReader
from Basicos.Bubble import BubbleSort
from Avancados.Merge import MergeSort
#from Basicos.Selection import SelectionSort
#from Basicos.Insertion import InsertionSortp[p]

if __name__ == "__main__":
    file_reader = FileReader("numeros_aleatorios.txt")
    desordenado = file_reader.read_numbers()
    
    if desordenado:
        print("Lista antes da ordenação:", desordenado)
        
        print("Escolha o algoritmo de ordenação:")
        print("1 - Bubble Sort")
        print("2 - Bubble Sort Melhorado")
        print("3 - Selection Sort")
        print("4 - Insertion Sort")
        print("5 - Merge Sort")
        print("6 - Quick Sort")
        print("7 - Tim Sort")
        escolha = input("Digite o número correspondente: ")
        
        if escolha == "1":
            BubbleSort.sort(desordenado)
        elif escolha == "2":
            BubbleSortMod.sort(desordenado)
        elif escolha == "3":
            SelectionSort.sort(desordenado)
        elif escolha == "4":
            InsertionSort.sort(desordenado)
        elif escolha == "5":
           desordenado = MergeSort.sort(desordenado)
        else:
            print("Opção inválida! Usando Bubble Sort por padrão.")
            BubbleSort.sort(desordenado)
        
        print("Lista ordenada:", desordenado)