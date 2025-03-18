class ShellSort:
    @staticmethod
    def sort(arr):
        """Executa o Shell Sort, retornando o número de comparações e trocas."""
        n = len(arr)
        gap = n // 2  # Inicializa o intervalo
        
        comparacoes = 0  # Contador de comparações
        trocas = 0  # Contador de trocas

        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i

                while j >= gap and arr[j - gap] > temp:
                    comparacoes += 1  # Contabiliza a comparação
                    arr[j] = arr[j - gap]
                    j -= gap
                    trocas += 1  # Contabiliza a troca

                arr[j] = temp

                if j != i:
                    trocas += 1  # Contabiliza a troca final caso ocorra

            gap //= 2  # Reduz o intervalo
        
        return comparacoes, trocas  # Retorna as métricas corretamente
