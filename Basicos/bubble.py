class BubbleSort:
    @staticmethod
    def sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(n - 1):  # Percorre toda a lista
                if arr[j] > arr[j + 1]:  # Compara elementos adjacentes
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Troca os elementos
