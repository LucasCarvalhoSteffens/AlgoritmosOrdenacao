class BubbleSort:
    @staticmethod
    def sort(arr):
        n = len(arr)
        comparacoes = 0  # Contador de comparações
        trocas = 0       # Contador de trocas
        
        for i in range(n):
            for j in range(0, n-i-1):
                comparacoes += 1  # Contagem de comparação
                
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    trocas += 1  # Contagem de troca
        
        return comparacoes, trocas
