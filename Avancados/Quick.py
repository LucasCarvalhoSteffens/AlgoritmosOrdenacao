class QuickSort:
    @staticmethod
    def sort(arr):
        comparacoes = 0
        trocas = 0

        def quick_sort(arr, low, high):
            nonlocal comparacoes, trocas
            if low < high:
                pi, comp, troca = partition(arr, low, high)
                comparacoes += comp
                trocas += troca
                quick_sort(arr, low, pi - 1)
                quick_sort(arr, pi + 1, high)

        def partition(arr, low, high):
            nonlocal comparacoes, trocas
            pivot = arr[high]
            i = low - 1
            local_comparacoes = 0
            local_trocas = 0

            for j in range(low, high):
                local_comparacoes += 1
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    local_trocas += 1

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            local_trocas += 1

            return i + 1, local_comparacoes, local_trocas

        quick_sort(arr, 0, len(arr) - 1)
        return comparacoes, trocas
