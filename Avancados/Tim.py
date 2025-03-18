class TimSort:
    @staticmethod
    def insertion_sort(arr, left, right):
        comparacoes = 0
        trocas = 0

        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                comparacoes += 1
                arr[j + 1] = arr[j]
                trocas += 1
                j -= 1
            arr[j + 1] = key
            trocas += 1

        return comparacoes, trocas

    @staticmethod
    def merge(arr, left, mid, right):
        comparacoes = 0
        trocas = 0

        left_part = arr[left:mid + 1]
        right_part = arr[mid + 1:right + 1]

        i = j = 0
        k = left

        while i < len(left_part) and j < len(right_part):
            comparacoes += 1
            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            trocas += 1
            k += 1

        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1
            trocas += 1

        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1
            trocas += 1

        return comparacoes, trocas

    @staticmethod
    def sort(arr):
        RUN = 32
        n = len(arr)
        total_comparacoes = 0
        total_trocas = 0

        # Aplicar Insertion Sort nos subarrays de tamanho RUN
        for i in range(0, n, RUN):
            comp, troca = TimSort.insertion_sort(arr, i, min(i + RUN - 1, n - 1))
            total_comparacoes += comp
            total_trocas += troca

        size = RUN
        while size < n:
            for left in range(0, n, 2 * size):
                mid = left + size - 1
                right = min(left + 2 * size - 1, n - 1)

                if mid < right:
                    comp, troca = TimSort.merge(arr, left, mid, right)
                    total_comparacoes += comp
                    total_trocas += troca

            size *= 2

        return total_comparacoes, total_trocas
