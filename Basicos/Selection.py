class SelectionSort:
    @staticmethod
    def sort(arr):
        """Executa o Selection Sort, retornando o número de comparações e trocas."""
        n = len(arr)
        comparacoes = 0  # Contador de comparações
        trocas = 0  # Contador de trocas

        for i in range(n - 1):
            min_idx = i  # Índice do menor elemento encontrado
            
            for j in range(i + 1, n):
                comparacoes += 1  # Conta a comparação entre elementos
                if arr[j] < arr[min_idx]:
                    min_idx = j  # Atualiza o índice do menor valor
            
            # Faz a troca somente se necessário
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                trocas += 1  # Contabiliza a troca

        return comparacoes, trocas  # Retorna os valores corretos
