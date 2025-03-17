class ShellSort:
    @staticmethod
    def sort(arr):
        n = len(arr)
        gap = n // 2  # Inicializa o intervalo
        
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            
            gap //= 2  # Reduz o intervalo
        
        return arr
