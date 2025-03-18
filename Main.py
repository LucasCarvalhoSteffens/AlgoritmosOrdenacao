import subprocess
import time
from FileReader import FileReader
from Basicos.bubble import BubbleSort
from Basicos.BubbleMod import BubbleSortMod
from Basicos.Selection import SelectionSort
from Basicos.Insertion import InsertionSort
from Avancados.Merge import MergeSort
from Avancados.Quick import QuickSort
from Avancados.Tim import TimSort
from OutrosSugeridos.HeapSort import HeapSort
from OutrosSugeridos.CountingSort import CountingSort
from OutrosSugeridos.RadixSort import RadixSort
from OutrosSugeridos.ShellSort import ShellSort

def medir_tempo(algoritmo, lista):
    """Mede o tempo de execução de um algoritmo de ordenação."""
    lista_copia = lista.copy()  # Evita modificar a lista original
    inicio = time.time()
    algoritmo.sort(lista_copia)
    fim = time.time()
    return fim - inicio

if __name__ == "__main__":
    file_reader = FileReader("numeros_aleatorios.txt")
    desordenado = file_reader.read_numbers()

    if desordenado:
        print("\nLista antes da ordenação:", desordenado)

        print("\nEscolha o algoritmo de ordenação:")
        print("1 - Bubble Sort")
        print("2 - Bubble Sort Melhorado")
        print("3 - Selection Sort")
        print("4 - Insertion Sort")
        print("5 - Merge Sort")
        print("6 - Quick Sort")
        print("7 - Tim Sort")
        print("8 - Heap Sort")
        print("9 - Counting Sort")
        print("10 - Radix Sort")
        print("11 - Shell Sort")
        print("12 - Verificar métricas de tempo de execução")
        print("0 - Sair")

        escolha = input("Digite o número correspondente: ").strip()

        if escolha == "0":
            print("Saindo do programa...")
        elif escolha == "12":
            print("\nExecutando métricas de tempo de execução...\n")
            subprocess.run(["python", "metricas.py"])  # Chama o script metricas.py e espera a execução
        elif escolha == "1":
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
        elif escolha == "9":
            desordenado = CountingSort.sort(desordenado)
        elif escolha == "10":
            desordenado = RadixSort.sort(desordenado)
        elif escolha == "11":
            desordenado = ShellSort.sort(desordenado)
        else:
            print("Opção inválida! Usando Bubble Sort por padrão.")
            BubbleSort.sort(desordenado)

        if escolha not in {"12", "0"}:
            print("\nLista ordenada:", desordenado)
