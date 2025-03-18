class CountingSort:
    @staticmethod
    def sort(arr):
        """ Counting Sort com contagem de movimentações """
        if not arr:
            return 0, 0  # Retorna zero comparações e zero movimentações se a lista estiver vazia

        metrics = {'comparacoes': 0, 'trocas': 0}

        # Garante que os elementos sejam extraídos corretamente, sejam objetos ou inteiros
        if isinstance(arr[0], int):
            min_val = min(arr)
            max_val = max(arr)
        else:
            min_val = min(arr, key=lambda x: x.value).value
            max_val = max(arr, key=lambda x: x.value).value

        range_of_elements = max_val - min_val + 1  # Tamanho do array de contagem

        # Inicializa o array de contagem e o array de saída
        count_arr = [0] * range_of_elements
        output_arr = [None] * len(arr)

        # Contagem de cada elemento no array original
        for num in arr:
            index = (num.value if hasattr(num, 'value') else num) - min_val
            count_arr[index] += 1

        # Atualiza count_arr para armazenar as posições corretas dos elementos ordenados
        for i in range(1, len(count_arr)):
            count_arr[i] += count_arr[i - 1]

        # Constrói o array ordenado e conta movimentações
        for num in reversed(arr):
            index = (num.value if hasattr(num, 'value') else num) - min_val
            output_arr[count_arr[index] - 1] = num
            count_arr[index] -= 1
            metrics['trocas'] += 1  # Contabiliza movimentações

        # Copia os valores ordenados de volta para o array original
        for i in range(len(arr)):
            arr[i] = output_arr[i]

        return metrics['comparacoes'], metrics['trocas']
