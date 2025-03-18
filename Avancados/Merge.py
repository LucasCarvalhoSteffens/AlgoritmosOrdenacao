class MergeSort:
    @staticmethod
    def sort(arr):
        comparacoes = 0
        trocas = 0

        def merge(arr, L, R):
            nonlocal comparacoes, trocas
            i = j = k = 0

            while i < len(L) and j < len(R):
                comparacoes += 1  # Comparação entre elementos de L e R
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
                trocas += 1  # Cada inserção conta como troca

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
                trocas += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
                trocas += 1

        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                L = arr[:mid]
                R = arr[mid:]

                merge_sort(L)
                merge_sort(R)
                merge(arr, L, R)

        merge_sort(arr)
        return comparacoes, trocas  # Retorna os valores corretos!
