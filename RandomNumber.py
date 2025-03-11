import random

def gerar_numeros(qtd, nome_arquivo):
    inicio, fim = 1, qtd  # Define o intervalo automaticamente baseado na quantidade solicitada
    
    if qtd > (fim - inicio + 1):
        raise ValueError("Quantidade excede o limite de números únicos possíveis no intervalo especificado.")
    
    numeros = random.sample(range(inicio, fim + 1), qtd)  # Gera uma sequência única de números aleatórios dentro do intervalo
    
    with open(nome_arquivo, "w") as arquivo:
        for numero in numeros:
            arquivo.write(f"{numero}\n")

if __name__ == "__main__":
    quantidade = int(input("Quantos números deseja gerar? "))
    nome_arquivo = "numeros_aleatorios.txt"
    gerar_numeros(quantidade, nome_arquivo)
    print(f"{quantidade} números únicos foram gerados e salvos em '{nome_arquivo}'.")
