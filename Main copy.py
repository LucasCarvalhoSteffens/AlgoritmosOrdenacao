import time
import logging
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import Resource
from FileReader import FileReader
from Basicos.bubble import BubbleSort
from Basicos.BubbleMod import BubbleSortMod
from Basicos.Selection import SelectionSort
from Basicos.Insertion import InsertionSort
from Avancados.Merge import MergeSort
from Avancados.Quick import QuickSort
from Avancados.Tim import TimSort
from OutrosSugeridos.HeapSort import HeapSort
from OutrosSugeridos.CountingSort import CountingSort
from OutrosSugeridos.RadixSort import RadixSort
from OutrosSugeridos.ShellSort import ShellSort

# 🔹 Configuração do Logger Local
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)

# 🔹 Configuração do OpenTelemetry com Jaeger
trace.set_tracer_provider(
    TracerProvider(resource=Resource.create({"service.name": "sorting-algorithms"}))
)
tracer = trace.get_tracer(__name__)

# 🔹 Exportador do Jaeger para capturar os traces
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",  # Host padrão do Jaeger rodando localmente
    agent_port=6831,  # Porta padrão para recepção de spans
)

# 🔹 Configurando o Processador de Traces para enviar os dados ao Jaeger
span_processor = BatchSpanProcessor(jaeger_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# 🔹 Função para medir tempo e capturar métricas de ordenação
def medir_tempo(algoritmo, lista):
    """Mede o tempo de execução de um algoritmo de ordenação e envia logs para o Jaeger."""
    lista_copia = lista.copy()

    with tracer.start_as_current_span(algoritmo.__name__) as span:
        inicio = time.perf_counter()  # ⏱️ Captura o tempo inicial

        resultado = algoritmo.sort(lista_copia)  # Executa o algoritmo de ordenação

        fim = time.perf_counter()  # ⏱️ Captura o tempo final
        tempo_execucao = fim - inicio  # Calcula o tempo total

        # 🔹 Ajusta retorno para evitar erros de desempacotamento
        if isinstance(resultado, tuple) and len(resultado) == 2:
            comparacoes, trocas = resultado
        else:
            comparacoes, trocas = 0, 0

        # 🔹 Garante que tempos extremamente curtos sejam tratados corretamente
        if tempo_execucao < 1e-6:
            tempo_execucao = 1e-6

        # 🔹 Adiciona atributos ao OpenTelemetry para análise
        span.set_attribute("algoritmo", algoritmo.__name__)
        span.set_attribute("tamanho_lista", len(lista))
        span.set_attribute("tempo_execucao", tempo_execucao)
        span.set_attribute("comparacoes", comparacoes)
        span.set_attribute("trocas", trocas)

        # 🔹 Logging local para acompanhamento
        log.info(f"Algoritmo: {algoritmo.__name__}, Tamanho: {len(lista)}, Tempo: {tempo_execucao:.6f}s, Comparações: {comparacoes}, Trocas: {trocas}")

    return tempo_execucao


if __name__ == "__main__":
    file_reader = FileReader("numeros_aleatorios.txt")
    desordenado = file_reader.read_numbers()

    if desordenado:
        print("\nEscolha o algoritmo de ordenação:")
        print("1 - Bubble Sort")
        print("2 - Bubble Sort Melhorado")
        print("3 - Selection Sort")
        print("4 - Insertion Sort")
        print("5 - Merge Sort")
        print("6 - Quick Sort")
        print("7 - Tim Sort")
        print("8 - Heap Sort")
        print("9 - Counting Sort")
        print("10 - Radix Sort")
        print("11 - Shell Sort")
        print("12 - Verificar métricas de tempo de execução")

        escolha = input("Digite o número correspondente: ")

        # 🔹 Dicionário com os algoritmos de ordenação disponíveis
        algoritmos = {
            "1": BubbleSort,
            "2": BubbleSortMod,
            "3": SelectionSort,
            "4": InsertionSort,
            "5": MergeSort,
            "6": QuickSort,
            "7": TimSort,
            "8": HeapSort,
            "9": CountingSort,
            "10": RadixSort,
            "11": ShellSort
        }

        # 🔹 Executa o algoritmo escolhido
        if escolha in algoritmos:
            medir_tempo(algoritmos[escolha], desordenado)

        # 🔹 Geração de métricas para todos os algoritmos
        elif escolha == "12":
            tempoinicio =  time.perf_counter()
            print("\nMétricas de tempo de execução:")
            for nome, algoritmo in algoritmos.items():
                
                tempo = medir_tempo(algoritmo, desordenado)
               
                print(f"{algoritmo.__name__}: {tempo:.6f} segundos")

            fim = time.perf_counter()
            print(f"Tempo total: {fim - tempoinicio:.6f} segundos")
        else:
            print("Opção inválida! Usando Bubble Sort por padrão.")
            medir_tempo(BubbleSort, desordenado)