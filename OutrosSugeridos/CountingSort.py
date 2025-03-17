class CountingSort:
    @staticmethod
    def sort(arr):
        if not arr:
            return arr
        
        max_val = max(arr)  # Encontra o maior valor no array
        min_val = min(arr)  # Encontra o menor valor no array
        range_of_elements = max_val - min_val + 1
        
        count = [0] * range_of_elements  # Inicializa a contagem
        output = [0] * len(arr)  # Lista de saída ordenada
        
        for num in arr:
            count[num - min_val] += 1  # Conta as ocorrências de cada número
        
        for i in range(1, len(count)):
            count[i] += count[i - 1]  # Acumula as contagens
        
        for num in reversed(arr):  # Ordena os elementos
            output[count[num - min_val] - 1] = num
            count[num - min_val] -= 1
        
        return output
