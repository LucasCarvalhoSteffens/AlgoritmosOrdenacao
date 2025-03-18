class BubbleSortMod:
    @staticmethod
    def sort(arr):
        n = len(arr)
        comparacoes = 0
        trocas = 0
        for i in range(n):
            trocou = False
            for j in range(0, n - i - 1):
                comparacoes += 1
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    trocas += 1
                    trocou = True
            if not trocou:  # Se não houve troca, a lista já está ordenada
                break
        return comparacoes, trocas  # ✅ Retorna corretamente
