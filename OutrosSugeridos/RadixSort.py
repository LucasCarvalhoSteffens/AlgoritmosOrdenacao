class RadixSort:
    @staticmethod
    def counting_sort(arr, exp):
        n = len(arr)
        output = [None] * n
        count = [0] * 10

        # Contagem da frequência dos dígitos
        for i in range(n):
            num = arr[i].value if hasattr(arr[i], 'value') else arr[i]
            index = (num // exp) % 10
            count[index] += 1

        # Atualiza count[i] para armazenar a posição correta dos elementos na saída
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Constrói a saída ordenada
        for i in range(n - 1, -1, -1):
            num = arr[i].value if hasattr(arr[i], 'value') else arr[i]
            index = (num // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1

        # Copia os valores ordenados de volta para o array original
        for i in range(n):
            arr[i] = output[i]

    @staticmethod
    def sort(arr):
        if not arr:
            return arr  # Retorna se a lista estiver vazia

        # Obtém o maior valor da lista, garantindo que seja um número puro
        if isinstance(arr[0], int):
            max_val = max(arr)
        else:
            max_val = max(arr, key=lambda x: x.value).value

        # Aplica Counting Sort para cada casa decimal
        exp = 1
        while max_val // exp > 0:
            RadixSort.counting_sort(arr, exp)
            exp *= 10

        return arr  # Retorna a lista ordenada
