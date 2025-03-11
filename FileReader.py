class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_numbers(self):
        try:
            with open(self.filename, 'r') as file:
                numbers = [int(line.strip()) for line in file.readlines()]
            return numbers
        except FileNotFoundError:
            print("Arquivo não encontrado!")
            return []
        except ValueError:
            print("Erro ao converter os valores para inteiros!")
            return []

# Exemplo de uso
file_reader = FileReader("numeros_aleatorios.txt")
desordenado = file_reader.read_numbers()

