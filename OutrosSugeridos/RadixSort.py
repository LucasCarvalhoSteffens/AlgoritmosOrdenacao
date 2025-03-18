class RadixSort:
    @staticmethod
    def counting_sort(arr, exp, metrics):
        """Ordena a lista de acordo com o dígito específico (exp) usando Counting Sort."""
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        # Contagem da frequência dos dígitos
        for i in range(n):
            num = arr[i] if isinstance(arr[i], int) else arr[i].value
            index = (num // exp) % 10
            count[index] += 1
            metrics["comparacoes"] += 1  # Conta cada acesso a um elemento

        # Atualiza count[i] para armazenar a posição correta dos elementos na saída
        for i in range(1, 10):
            count[i] += count[i - 1]
            metrics["comparacoes"] += 1  # Conta as comparações do loop

        # Constrói a saída ordenada
        for i in range(n - 1, -1, -1):
            num = arr[i] if isinstance(arr[i], int) else arr[i].value
            index = (num // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            metrics["movimentacoes"] += 1  # Conta cada movimentação para a saída

        # Copia os valores ordenados de volta para o array original
        for i in range(n):
            arr[i] = output[i]
            metrics["movimentacoes"] += 1  # Conta cada movimentação de volta para arr

    @staticmethod
    def sort(arr):
        """Executa o Radix Sort para ordenar a lista de inteiros."""
        if not arr:
            return 0, 0  # Retorna 0 comparações e 0 movimentações se a lista estiver vazia

        # Obtém o maior valor da lista, garantindo que seja um número puro
        max_val = max(arr) if isinstance(arr[0], int) else max(arr, key=lambda x: x.value).value

        exp = 1
        metrics = {"comparacoes": 0, "movimentacoes": 0}  # Inicializa contadores

        # Aplica Counting Sort para cada casa decimal
        while max_val // exp > 0:
            RadixSort.counting_sort(arr, exp, metrics)
            exp *= 10

        return metrics["comparacoes"], metrics["movimentacoes"]  # Retorna apenas métricas