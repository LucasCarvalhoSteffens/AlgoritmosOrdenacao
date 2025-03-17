class QuickSort:
    @staticmethod
    def sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]  # Escolhe o pivô como o elemento do meio
        left = [x for x in arr if x < pivot]  # Elementos menores que o pivô
        middle = [x for x in arr if x == pivot]  # Elementos iguais ao pivô
        right = [x for x in arr if x > pivot]  # Elementos maiores que o pivô
        return QuickSort.sort(left) + middle + QuickSort.sort(right)
