class QuickSort:
    @staticmethod
    def partition(arr, low, high):
        pivot = arr[high]  # Escolhe o pivô
        i = low - 1
        comparisons = 0  # Contador de comparações
        moves = 0  # Inicializa o contador de movimentações

        for j in range(low, high):
            comparisons += 1  # Conta comparação
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                moves += 2  # Conta movimentações

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        moves += 2  # Conta movimentações

        return i + 1, comparisons, moves  # Retorna índice do pivô e métricas

    @staticmethod
    def sort(arr, low=0, high=None):
        if high is None:
            high = len(arr) - 1

        if low < high:
            pi, comparisons, moves = QuickSort.partition(arr, low, high)  # Captura métricas
            QuickSort.sort(arr, low, pi - 1)
            QuickSort.sort(arr, pi + 1, high)

        return arr
