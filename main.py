# Importa bibliotecas necessárias
import time
import sys

# Aumenta o limite de recursão do Python
sys.setrecursionlimit(2000)

# Função recursiva para calcular o fatorial
def fatorial(n):
    """
    Calcula o fatorial de n usando recursão
    """

    # Caso base: fatorial de 0 ou 1 é 1
    if n == 0 or n == 1:
        return 1

    # Caso recursivo
    return n * fatorial(n - 1)


# Valores que serão testados
valores_teste = [10, 100, 500, 1000]

print("Tempo de execução do fatorial recursivo\n")

# Loop para testar diferentes valores de n
for n in valores_teste:

    # Marca o tempo antes da execução
    inicio = time.time()

    # Calcula o fatorial
    resultado = fatorial(n)

    # Marca o tempo depois da execução
    fim = time.time()

    # Calcula o tempo total
    tempo_execucao = fim - inicio

    # Mostra o resultado
    print(f"n = {n}")
    print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
    print("-" * 30)