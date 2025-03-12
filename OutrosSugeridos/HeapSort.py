from FileReader import FileReader
class HeapSort:
    @staticmethod
    def heapify(arr, n, i):
        largest = i  # Inicializa o maior como raiz
        left = 2 * i + 1  # Filho esquerdo
        right = 2 * i + 2  # Filho direito

        # Verifica se o filho esquerdo é maior que a raiz
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Verifica se o filho direito é maior que o maior até agora
        if right < n and arr[right] > arr[largest]:
            largest = right

        # Se o maior não for a raiz, troca e continua heapificando
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            HeapSort.heapify(arr, n, largest)

    @staticmethod
    def sort(arr):
        n = len(arr)

        # Constrói o heap máximo
        for i in range(n // 2 - 1, -1, -1):
            HeapSort.heapify(arr, n, i)

        # Extrai elementos um por um
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Troca
            HeapSort.heapify(arr, i, 0)
        
        return arr
