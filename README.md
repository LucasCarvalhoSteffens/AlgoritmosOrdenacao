# Relatório Técnico: Comparativo de Algoritmos de Ordenação

## 1. Código-Fonte Documentado e Organizado

O código do projeto está bem estruturado, seguindo a divisão de módulos para diferentes algoritmos de ordenação. As principais partes do código incluem:

- **Main.py**: Responsável pela execução dos algoritmos e medição de tempo.
- **data_generator.py**: Gera conjuntos de dados aleatórios para testes.
- **metricas.py**: Mede e registra as estatísticas de execução.
- **Logs (OpenTelemetry + Jaeger)**: Captura informações detalhadas sobre a execução dos algoritmos.
- **Pastas "Basicos", "Avancados" e "OutrosSugeridos"**: Contêm as implementações de diferentes algoritmos de ordenação.

Cada algoritmo está bem modularizado e segue o padrão de separação de responsabilidades.

## 2. Explicação do Uso do Padrão Strategy

O padrão Strategy foi aplicado ao definir diferentes algoritmos de ordenação como classes separadas. Isso permite que a seleção do algoritmo ocorra dinamicamente no momento da execução sem alterar a lógica principal do sistema.

### Implementação do Strategy:
- Cada algoritmo de ordenação está em uma classe própria (exemplo: `BubbleSort`, `QuickSort`, `MergeSort`).
- A função `medir_tempo()` recebe um algoritmo como argumento e o executa.
- O usuário pode selecionar dinamicamente qual algoritmo deseja testar.

Essa abordagem melhora a manutenção do código e permite facilmente adicionar novos algoritmos sem impactar a estrutura geral.

## 3. Descrição do Processo de Geração dos Dados

O arquivo `data_generator.py` é responsável por gerar conjuntos de dados aleatórios para os testes. Os dados são gerados da seguinte forma:
- Definição do tamanho do conjunto de dados.
- Uso da função `random.sample()` para gerar números únicos dentro de um intervalo definido.
- Os dados podem ser salvos em formatos `.txt` ou binário (`.bin`).
- Opção de gerar listas ordenadas, reversamente ordenadas ou aleatórias.

Isso garante flexibilidade na avaliação do desempenho dos algoritmos em diferentes cenários.

## 4. Métricas e Gráficos Comparativos de Desempenho

O script `metricas.py` mede e registra as seguintes informações para cada algoritmo:
- Tempo de execução.
- Número de comparações.
- Número de movimentações/trocas.

### Exemplos de resultados registrados:
| Algoritmo      | Tempo (s) | Comparacões | Trocas |
|---------------|----------|-------------|-------|
| Bubble Sort  | 0.003010  | 19900       | 10156 |
| Selection Sort | 0.001550 | 19900       | 196   |
| Quick Sort    | 0.000338  | 1646        | 938   |
| Merge Sort    | 0.000626  | 1286        | 1544  |
| Radix Sort    | 0.000593  | 836         | 1600  |
| Heap Sort     | 0.001173  | 2450        | 1358  |

## 5. Descrição da Ferramenta Utilizada para Logs e Análise dos Resultados

Para capturar e visualizar os logs das execuções dos algoritmos, utilizamos o **OpenTelemetry** integrado ao **Jaeger**. A configuração está presente no `Main.py`:

- **OpenTelemetry**: Instrumenta o código para capturar eventos de execução.
- **Jaeger**: Coleta e exibe logs detalhados de cada execução.
- **Métricas coletadas**: Tempo de execução, número de comparações e trocas.

Os logs podem ser visualizados diretamente no Jaeger UI, permitindo identificar gargalos e otimizar os algoritmos.

## 6. Conclusão: Melhor Algoritmo e Justificativa

Com base nos testes realizados, os algoritmos **Quick Sort** e **Merge Sort** apresentaram os melhores desempenhos na maioria dos cenários:

- **Quick Sort** é muito eficiente para grandes volumes de dados devido à sua complexidade média de O(n log n).
- **Merge Sort** se mostrou uma alternativa confiável por sua estabilidade e eficiência em grandes listas.
- **Algoritmos como Bubble Sort e Selection Sort foram significativamente mais lentos**, devido à complexidade O(n^2).

Portanto, **Quick Sort é a escolha recomendada para ordenação eficiente em aplicações reais**.

