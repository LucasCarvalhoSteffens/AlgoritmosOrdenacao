class RadixSort:
    @staticmethod
    def counting_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10  # Contagem para os dígitos (0-9)

        for num in arr:
            index = (num // exp) % 10
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            num = arr[i]
            index = (num // exp) % 10
            output[count[index] - 1] = num
            count[index] -= 1

        for i in range(n):
            arr[i] = output[i]

    @staticmethod
    def sort(arr):
        if not arr:
            return arr
        
        max_val = max(arr)
        exp = 1
        while max_val // exp > 0:
            RadixSort.counting_sort(arr, exp)
            exp *= 10
        
        return arr
