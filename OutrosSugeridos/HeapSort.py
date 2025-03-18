class HeapSort:
    @staticmethod
    def heapify(arr, n, i, metrics):
        """ Função para reorganizar o heap """
        largest = i  # Inicializa o maior como a raiz
        left = 2 * i + 1  # Filho esquerdo
        right = 2 * i + 2  # Filho direito

        # Compara o nó raiz com o filho esquerdo
        if left < n:
            metrics['comparacoes'] += 1
            if arr[left] > arr[largest]:
                largest = left

        # Compara o maior nó encontrado com o filho direito
        if right < n:
            metrics['comparacoes'] += 1
            if arr[right] > arr[largest]:
                largest = right

        # Se o maior não for a raiz, troca e continua o heapify
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            metrics['trocas'] += 1
            HeapSort.heapify(arr, n, largest, metrics)

    @staticmethod
    def sort(arr):
        """ Função principal do Heap Sort """
        n = len(arr)
        metrics = {'comparacoes': 0, 'trocas': 0}

        # Constrói o heap (reorganiza o array)
        for i in range(n // 2 - 1, -1, -1):
            HeapSort.heapify(arr, n, i, metrics)

        # Extrai elementos um por um do heap
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Troca o elemento atual com a raiz
            metrics['trocas'] += 1
            HeapSort.heapify(arr, i, 0, metrics)

        return metrics['comparacoes'], metrics['trocas']
