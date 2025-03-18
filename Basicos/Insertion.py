class InsertionSort:
    @staticmethod
    def sort(arr):
        comparacoes = 0
        trocas = 0
        n = len(arr)

        for i in range(1, n):
            key = arr[i]
            j = i - 1

            while j >= 0:
                comparacoes += 1  # Cada comparação feita no while
                if key < arr[j]:
                    arr[j + 1] = arr[j]
                    trocas += 1  # Movimentação de elemento = troca
                else:
                    break  # Sai do loop se não precisar trocar
                j -= 1

            arr[j + 1] = key
            trocas += 1  # Inserção final da chave

        return comparacoes, trocas  # Retorna os valores corretos!
