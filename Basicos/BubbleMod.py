class BubbleSortMod:
    @staticmethod
    def sort(arr):
        n = len(arr)
        for i in range(n):
            trocou = False  # Flag para verificar se houve troca
            for j in range(n - 1 - i):  # Evita comparar elementos já ordenados
                if arr[j] > arr[j + 1]:  # Compara elementos adjacentes
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Troca os elementos
                    trocou = True  # Marca que houve troca
            if not trocou:
                break  # Se não houve troca, a lista já está ordenada
