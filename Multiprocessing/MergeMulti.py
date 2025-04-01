from concurrent.futures import ThreadPoolExecutor
import math

class MergeSortMulti:
    @staticmethod
    def merge(arr, L, R, comparacoes_total, trocas_total):
        """Helper function to merge two sorted arrays"""
        comparacoes = 0
        trocas = 0
        i = j = k = 0

        while i < len(L) and j < len(R):
            comparacoes += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            trocas += 1

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

        comparacoes_total[0] += comparacoes
        trocas_total[0] += trocas

    @staticmethod
    def merge_sort_chunk(arr, start, end, comparacoes_total, trocas_total):
        """Helper function to sort a chunk of the array"""
        if end - start > 1:
            mid = (start + end) // 2
            left = arr[start:mid]
            right = arr[mid:end]
            
            MergeSortMulti.merge_sort_chunk(left, 0, len(left), comparacoes_total, trocas_total)
            MergeSortMulti.merge_sort_chunk(right, 0, len(right), comparacoes_total, trocas_total)
            MergeSortMulti.merge(arr[start:end], left, right, comparacoes_total, trocas_total)
        elif end - start == 1:
            if arr[start] > arr[end-1]:
                arr[start], arr[end-1] = arr[end-1], arr[start]
                trocas_total[0] += 1
            comparacoes_total[0] += 1

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
                end = min((i + 1) * chunk_size, n)
                if start < n:
                    futures.append(
                        executor.submit(
                            MergeSortMulti.merge_sort_chunk,
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

        # Final merge passes to combine sorted chunks
        current_size = chunk_size
        while current_size < n:
            for start in range(0, n, current_size * 2):
                mid = min(start + current_size, n)
                end = min(start + current_size * 2, n)
                if mid < end:
                    left = arr[start:mid]
                    right = arr[mid:end]
                    MergeSortMulti.merge(arr[start:end], left, right, comparacoes_total, trocas_total)
            current_size *= 2

        return comparacoes_total[0], trocas_total[0]