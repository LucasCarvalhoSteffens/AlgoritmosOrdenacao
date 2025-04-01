from concurrent.futures import ThreadPoolExecutor
import math

class QuickSortMulti:
    @staticmethod
    def partition(arr, low, high, comparacoes_total, trocas_total):
        """Helper function to partition the array"""
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

        comparacoes_total[0] += local_comparacoes
        trocas_total[0] += local_trocas
        return i + 1

    # In QuickSortMulti.py
    @staticmethod
    def quick_sort_chunk(arr, low, high, comparacoes_total, trocas_total):
        if low >= high or low < 0 or high >= len(arr):  # Add bounds checking
            return
        if high - low < 1000:  # Threshold for small arrays to prevent deep recursion
            QuickSortMulti.partition(arr, low, high, comparacoes_total, trocas_total)
        else:
            pi = QuickSortMulti.partition(arr, low, high, comparacoes_total, trocas_total)
            QuickSortMulti.quick_sort_chunk(arr, low, pi - 1, comparacoes_total, trocas_total)
            QuickSortMulti.quick_sort_chunk(arr, pi + 1, high, comparacoes_total, trocas_total)

    @staticmethod
    def sort(arr):
        comparacoes_total = [0]  # Mutable list for thread-safe counter
        trocas_total = [0]
        n = len(arr)

        if n <= 1:
            return comparacoes_total[0], trocas_total[0]

        # Determine number of threads and chunk size
        num_threads = min(4, n)  # Use up to 4 threads
        chunk_size = math.ceil(n / num_threads)

        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = []
            for i in range(num_threads):
                start = i * chunk_size
                end = min((i + 1) * chunk_size - 1, n - 1)
                if start < n:
                    futures.append(
                        executor.submit(
                            QuickSortMulti.quick_sort_chunk,
                            arr,
                            start,
                            end,
                            comparacoes_total,
                            trocas_total
                        )
                    )
            
            # Wait for all initial chunks to be sorted
            for future in futures:
                future.result()

        # Final pass to ensure complete sorting
        QuickSortMulti.quick_sort_chunk(arr, 0, n - 1, comparacoes_total, trocas_total)

        return comparacoes_total[0], trocas_total[0]
