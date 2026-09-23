import sys

def solve():
    # Lê todas as entradas de uma vez e divide por espaços/quebras de linha
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # Exemplo de leitura:
    # n = int(input_data[0])
    # array = [int(x) for x in input_data[1:n+1]]
    
    print("Ambiente configurado com sucesso!")

if __name__ == "__main__":
    solve()