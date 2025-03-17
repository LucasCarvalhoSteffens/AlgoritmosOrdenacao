class TimSort:
    @staticmethod
    def insertion_sort(arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    @staticmethod
    def merge(arr, left, mid, right):
        left_part = arr[left:mid + 1]
        right_part = arr[mid + 1:right + 1]
        i = j = 0
        k = left

        while i < len(left_part) and j < len(right_part):
            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1

    @staticmethod
    def sort(arr):
        RUN = 32
        n = len(arr)

        for i in range(0, n, RUN):
            TimSort.insertion_sort(arr, i, min(i + RUN - 1, n - 1))

        size = RUN
        while size < n:
            for left in range(0, n, 2 * size):
                mid = left + size - 1
                right = min(left + 2 * size - 1, n - 1)
                if mid < right:
                    TimSort.merge(arr, left, mid, right)
            size *= 2

        return arr
