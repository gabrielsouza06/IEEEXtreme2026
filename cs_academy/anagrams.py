import sys
from collections import Counter

# Fast I/O em lote
input_data = sys.stdin.read().split()
iterator = iter(input_data)

def get_word():
    """Retorna o próximo token da entrada como string."""
    try:
        return next(iterator)
    except StopIteration:
        return None

def get_number():
    """Retorna o próximo token convertido para int ou float."""
    data = get_word()
    if data is None:
        return None
    try:
        return int(data)
    except ValueError:
        return float(data)

def solve():
    n = get_number()
    if n is None or n == 0:
        print(0)
        return

    # Usar Counter diretamente gerando as chaves ordenadas
    grupos = Counter(''.join(sorted(next(iterator))) for _ in range(n))

    # max com default previne erros se grupos estiver vazio
    resultado = max(grupos.values(), default=0)
    sys.stdout.write(f"{resultado}\n")

if __name__ == '__main__':
    sys.setrecursionlimit(200000)
    solve()
