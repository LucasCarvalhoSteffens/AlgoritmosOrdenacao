import time
from FileReader import FileReader

# Importa os algoritmos de ordenação já implementados
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

# Contadores globais para comparações e movimentações
comparisons = 0
moves = 0

# Classe que encapsula um número e conta cada comparação realizada
class CountedNumber:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        global comparisons
        comparisons += 1
        return self.value < (other.value if isinstance(other, CountedNumber) else other)

    def __le__(self, other):
        global comparisons
        comparisons += 1
        return self.value <= (other.value if isinstance(other, CountedNumber) else other)

    def __gt__(self, other):
        global comparisons
        comparisons += 1
        return self.value > (other.value if isinstance(other, CountedNumber) else other)

    def __ge__(self, other):
        global comparisons
        comparisons += 1
        return self.value >= (other.value if isinstance(other, CountedNumber) else other)

    def __eq__(self, other):
        global comparisons
        comparisons += 1
        return self.value == (other.value if isinstance(other, CountedNumber) else other)

    def __ne__(self, other):
        global comparisons
        comparisons += 1
        return self.value != (other.value if isinstance(other, CountedNumber) else other)

    def __repr__(self):
        return str(self.value)

# Subclasse de list para contar cada atribuição (movimentação de elemento)
class CountedList(list):
    def __setitem__(self, index, value):
        global moves
        moves += 1
        super().__setitem__(index, value)

# Lista dos algoritmos de ordenação a serem comparados
algorithms = [
    ("Bubble Sort", BubbleSort.sort),
    ("Bubble Sort Melhorado", BubbleSortMod.sort),
    ("Selection Sort", SelectionSort.sort),
    ("Insertion Sort", InsertionSort.sort),
    ("Merge Sort", MergeSort.sort),
    ("Quick Sort", QuickSort.sort),
    ("Tim Sort", TimSort.sort),
    ("Heap Sort", HeapSort.sort),
    ("Counting Sort", CountingSort.sort),
    ("Radix Sort", RadixSort.sort),
    ("Shell Sort", ShellSort.sort)
]

def is_sorted(arr):
    """ Verifica se a lista está ordenada corretamente """
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

if __name__ == "__main__":
    # Leitura dos dados do arquivo gerado
    file_reader = FileReader("numeros_aleatorios.txt")
    data = file_reader.read_numbers()

    if not data:
        print("Arquivo de dados vazio ou não encontrado!")
    else:
        runs = 5  # número de execuções para cada algoritmo
        print(f"Executando cada algoritmo {runs} vezes para calcular a média das métricas...\n")

        # Cabeçalho da tabela de resultados
        print(f"{'Algoritmo':30} {'Tempo médio (ms)':>20} {'Comparações':>15} {'Movimentações':>15}")

        # Avalia cada algoritmo de ordenação
        for name, sort_function in algorithms:
            total_time = total_comp = total_moves = 0
            success = True  # Flag para verificar se todos os runs ordenam corretamente

            for _ in range(runs):
                # Cria uma cópia dos dados originais para não afetar as próximas execuções
                arr_copy = data.copy()
                arr_counted = CountedList([CountedNumber(x) for x in arr_copy])

                # Reinicia os contadores globais
                comparisons = 0
                moves = 0

                # Mede o tempo de execução do algoritmo
                start_time = time.perf_counter()
                sort_function(arr_counted)  # Executa a ordenação
                end_time = time.perf_counter()

                # Verifica se a lista está ordenada corretamente
                if not is_sorted(arr_counted):
                    success = False
                    print(f"Erro: {name} não ordenou corretamente!")
                    break  # Sai do loop se houver erro

                # Calcula o tempo em milissegundos para esta execução
                exec_time_ms = (end_time - start_time) * 1000

                # Atualiza os acumuladores com os resultados desta execução
                total_time += exec_time_ms
                total_comp += comparisons
                total_moves += moves

            if success:
                # Calcula as médias das métricas para o algoritmo atual
                avg_time = total_time / runs
                avg_comp = total_comp / runs
                avg_moves = total_moves / runs

                # Exibe os resultados médios formatados
                print(f"{name:30} {avg_time:20.2f} {avg_comp:15.0f} {avg_moves:15.0f}")
