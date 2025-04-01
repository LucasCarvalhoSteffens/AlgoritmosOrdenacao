from concurrent.futures import ThreadPoolExecutor
import math

class InsertionSortMulti:
    @staticmethod
    def insertion_sort_chunk(arr, start, end, comparacoes_total, trocas_total):
        """Helper function to sort a chunk of the array"""
        comparacoes = 0
        trocas = 0
        
        for i in range(start + 1, end + 1):
            key = arr[i]
            j = i - 1
            
            while j >= start:
                comparacoes += 1
                if key < arr[j]:
                    arr[j + 1] = arr[j]
                    trocas += 1
                else:
                    break
                j -= 1
            
            arr[j + 1] = key
            trocas += 1
        
        comparacoes_total[0] += comparacoes
        trocas_total[0] += trocas

    @staticmethod
    def sort(arr):
        comparacoes_total = [0]  # Using list as mutable object for thread safety
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
                end = min((i + 1) * chunk_size, n) - 1
                if start < n:
                    futures.append(
                        executor.submit(
                            InsertionSortMulti.insertion_sort_chunk,
                            arr,
                            start,
                            end,
                            comparacoes_total,
                            trocas_total
                        )
                    )
            
            # Wait for all threads to complete
            for future in futures:
                future.result()

        # Final pass to ensure complete sorting (simplified merge)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0:
                comparacoes_total[0] += 1
                if key < arr[j]:
                    arr[j + 1] = arr[j]
                    trocas_total[0] += 1
                else:
                    break
                j -= 1
            arr[j + 1] = key
            trocas_total[0] += 1

        return comparacoes_total[0], trocas_total[0]
