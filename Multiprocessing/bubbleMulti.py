from concurrent.futures import ThreadPoolExecutor
import math

class BubbleSortMulti:
    @staticmethod
    def bubble_sort_chunk(arr, start, end, comparacoes_total, trocas_total):
        """Helper function to sort a chunk of the array using bubble sort"""
        comparacoes = 0
        trocas = 0
        
        for i in range(start, end):
            for j in range(start, end - (i - start) - 1):
                comparacoes += 1
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    trocas += 1
        
        comparacoes_total[0] += comparacoes
        trocas_total[0] += trocas

    @staticmethod
    def merge_chunks(arr, start, mid, end, comparacoes_total, trocas_total):
        """Helper function to merge two sorted chunks"""
        comparacoes = 0
        trocas = 0
        left = arr[start:mid + 1]
        right = arr[mid + 1:end + 1]
        i = j = 0
        k = start

        while i < len(left) and j < len(right):
            comparacoes += 1
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                trocas += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            trocas += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            trocas += 1

        comparacoes_total[0] += comparacoes
        trocas_total[0] += trocas

    @staticmethod
    def sort(arr):
        n = len(arr)
        comparacoes_total = [0]  # Mutable list for thread-safe counter
        trocas_total = [0]

        if n <= 1:
            return comparacoes_total[0], trocas_total[0]

        # Determine number of threads and chunk size
        num_threads = min(4, n)  # Use up to 4 threads
        chunk_size = math.ceil(n / num_threads)

        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = []
            for i in range(num_threads):
                start = i * chunk_size
                end = min((i + 1) * chunk_size, n)
                if start < n:
                    futures.append(
                        executor.submit(
                            BubbleSortMulti.bubble_sort_chunk,
                            arr,
                            start,
                            end,
                            comparacoes_total,
                            trocas_total
                        )
                    )
            
            # Wait for all chunks to be sorted
            for future in futures:
                future.result()

        # Merge sorted chunks
        for i in range(num_threads - 1):
            start = 0
            mid = (i + 1) * chunk_size - 1
            end = min((i + 2) * chunk_size - 1, n - 1)
            if mid < end:
                BubbleSortMulti.merge_chunks(arr, start, mid, end, comparacoes_total, trocas_total)

        # Final bubble sort pass to ensure complete sorting
        for i in range(n):
            for j in range(0, n - i - 1):
                comparacoes_total[0] += 1
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    trocas_total[0] += 1

        return comparacoes_total[0], trocas_total[0]