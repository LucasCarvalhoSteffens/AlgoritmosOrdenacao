from FileReader import FileReader
class MergeSort:
    @staticmethod
    def merge(left, right):
        sorted_list = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])
        
        return sorted_list

    @staticmethod
    def sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_half = MergeSort.sort(arr[:mid])
        right_half = MergeSort.sort(arr[mid:])
        return MergeSort.merge(left_half, right_half)
