class SelectionSort:
    @staticmethod
    def sort(arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:  # Encontra o menor elemento
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Troca o menor elemento com o primeiro da parte não ordenada
