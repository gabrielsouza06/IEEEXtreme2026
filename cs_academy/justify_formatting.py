"""
===============================================================================
Problem: Justify Formatting
Platform: CS Academy (Interview Archive)
Link: https://csacademy.com/contest/interview-archive/task/justify_formatting/
Time Limit: 2000 ms
Memory Limit: 128 MB

STATEMENT:
You should implement a program that takes as input an array of N words (strings)
representing a text and an integer K. Format the text on multiple lines such that
each line has length K and is justified.

RULES:
1. Pack as many words as possible on each line.
2. Extra spaces should be evenly distributed between words on the same line.
3. If extra spaces cannot be distributed evenly, add more spaces to the left gaps.
4. If a line contains only 1 word, left-align it and pad extra spaces to the right.
5. The last line should NOT be justified (left-aligned with single spaces between
   words, padded with spaces at the end to reach length K).

STANDARD INPUT:
- First line: Two integers N and K.
- Next N lines: One word per line.

STANDARD OUTPUT:
- Print the formatted lines one by one.
===============================================================================
"""

import sys

# Fast I/O em lote
input_data = sys.stdin.read().split()
iterator = iter(input_data)

def get_word():
    try:
        return next(iterator)
    except StopIteration:
        return None

def get_number():
    data = get_word()
    if data is None:
        return None
    try:
        return int(data)
    except ValueError:
        return float(data)

def justify(words, k):
    n = len(words)
    linhas = []
    i = 0
    while i < n:
        # 1. Quantas palavras cabem na linha começando em i
        comprimento = len(words[i])
        j = i + 1
        while j < n and comprimento + 1 + len(words[j]) <= k:
            comprimento += 1 + len(words[j])
            j += 1

        num_palavras = j - i

        if j == n:
            # Última linha: alinhada à esquerda + espaços à direita até completar K
            linha = " ".join(words[i:j]).ljust(k)
        elif num_palavras == 1:
            # Só uma palavra: alinhada à esquerda + espaços à direita
            linha = words[i].ljust(k)
        else:
            # Justificar
            num_gaps = num_palavras - 1
            total_letras = sum(len(words[i + t]) for t in range(num_palavras))
            total_espacos = k - total_letras
            base = total_espacos // num_gaps
            resto = total_espacos % num_gaps

            partes = []
            for t in range(num_gaps):
                partes.append(words[i + t])
                espacos = base + (1 if t < resto else 0)
                partes.append(" " * espacos)
            partes.append(words[j - 1])
            linha = "".join(partes)

        linhas.append(linha)
        i = j

    return linhas

def solve():
    n = get_number()
    k = get_number()
    if n is None or k is None:
        return

    palavras = []
    for _ in range(n):
        w = get_word()
        if w is None:
            break
        palavras.append(w)

    linhas = justify(palavras, k)
    for linha in linhas:
        print(linha)

if __name__ == '__main__':
    solve()