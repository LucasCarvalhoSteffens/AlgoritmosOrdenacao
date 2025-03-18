class MergeSort:
    @staticmethod
    def merge(left, right):
        sorted_list = []
        i = j = 0

        # Comparação dos elementos de left e right
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        # Adiciona elementos restantes
        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])

        return sorted_list

    @staticmethod
    def sort(arr):
        if len(arr) <= 1:
            return arr  # Retorna se a lista já estiver ordenada

        mid = len(arr) // 2
        left_half = MergeSort.sort(arr[:mid])
        right_half = MergeSort.sort(arr[mid:])

        sorted_arr = MergeSort.merge(left_half, right_half)

        # Copia os elementos ordenados de volta para a lista original (in-place)
        for i in range(len(arr)):
            arr[i] = sorted_arr[i]

        return arr  # Retorna a lista ordenada
