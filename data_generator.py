import random
import struct

def gerar_dados(tamanho, min_valor=0, max_valor=None, modo='txt', nome_arquivo='dados'):
    if max_valor is None:
        max_valor = tamanho * 10  # Define o máximo como uma casa decimal a mais que o tamanho
    
    numeros = random.sample(range(min_valor, max_valor), tamanho)  # Garante números únicos dentro do intervalo
    
    if modo == 'txt':
        with open(f'{nome_arquivo}.txt', 'w') as f:
            f.write('\n'.join(map(str, numeros)))
    elif modo == 'bin':
        with open(f'{nome_arquivo}.bin', 'wb') as f:
            for numero in numeros:
                f.write(struct.pack('Q', numero))  # Escreve cada número como um inteiro de 8 bytes
    else:
        raise ValueError("Modo inválido! Use 'txt' para texto ou 'bin' para binário.")
    
    print(f'Arquivo {nome_arquivo}.{modo} gerado com {tamanho} números únicos no intervalo [{min_valor}, {max_valor}).')

if __name__ == "__main__":
    while True:
        tamanho = int(input("Digite o tamanho do conjunto de dados: "))
        min_valor = int(input("Digite o valor mínimo: "))
        max_valor = int(input("Digite o valor máximo: "))
        modo = input("Escolha o modo de saída (txt/bin): ").strip().lower()
        nome_arquivo = input("Digite o nome do arquivo (sem extensão): ").strip()
        
        gerar_dados(tamanho, min_valor, max_valor, modo, nome_arquivo)
        
        repetir = input("Deseja gerar outro conjunto de dados? (s/n): ").strip().lower()
        if repetir != 's':
            print("Saindo do programa.")
            break
