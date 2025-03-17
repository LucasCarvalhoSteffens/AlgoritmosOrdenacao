from FileReader import FileReader
from Basicos.bubble import BubbleSort
from Basicos.BubbleMod import BubbleSortMod
from Basicos.Selection import SelectionSort
from Basicos.Insertion import InsertionSort
from Avancados.Merge import MergeSort
from Avancados.Quick import QuickSort
#from Avancados.Tim import TimSort
from OutrosSugeridos.HeapSort import HeapSort
#from OutrosSugeridos.CountingSort import CountingSort
#from OutrosSugeridos.RadixSort import RadixSort
#from OutrosSugeridos.ShellSort import ShellSort

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
        print("8 - Heap Sort")
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
        elif escolha == "6":
           desordenado = QuickSort.sort(desordenado)
        elif escolha == "7":
           desordenado = TimSort.sort(desordenado)
        elif escolha == "8":
           desordenado = HeapSort.sort(desordenado)
        else:
            print("Opção inválida! Usando Bubble Sort por padrão.")
            BubbleSort.sort(desordenado)
        
        print("Lista ordenada:", desordenado)
