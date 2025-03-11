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

# Exemplo de uso
gerar_dados(10, min_valor=10, max_valor=1000, modo='txt')  # Gera um arquivo de texto com 10 números únicos no intervalo especificado
