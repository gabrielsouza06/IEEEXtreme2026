"""
===============================================================================
Problem: Intersecting Rectangles
Platform: CS Academy (Interview Archive)
Link: https://csacademy.com/contest/interview-archive/task/intersecting_rectangles/
Time Limit: 2000 ms
Memory Limit: 128 MB

STATEMENT:
You should implement a program that takes as input an array of N non-degenerate
rectangles in the cartesian plane. Return the number of pairs of rectangles that
strictly intersect each other (their intersection has a strictly positive area).

DESIRED SOLUTION:
The limits are low enough for O(N^2) to pass.

STANDARD INPUT:
- The first line contains a single integer N, representing the total number of rectangles.
- Each of the next N lines contains four integers x1, y1, x2, y2 representing
  the lower left corner (x1, y1) and the upper right corner (x2, y2) of a rectangle.

STANDARD OUTPUT:
- Print a single integer representing the number of strictly intersecting pairs.
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

def solve():
    n = get_number()
    if n is None or n < 2:
        print(0)
        return

    # Guarda cada retângulo como uma tupla: (x1, y1, x2, y2)
    rectangles = []
    for _ in range(n):
        x1 = get_number()
        y1 = get_number()
        x2 = get_number()
        y2 = get_number()
        if x1 is not None:
            rectangles.append((x1, y1, x2, y2))

    count = 0
    num_rects = len(rectangles)

    # Comparação O(N^2) de todos os pares (i, j) onde i < j
    for i in range(num_rects):
        x1_a, y1_a, x2_a, y2_a = rectangles[i]
        for j in range(i + 1, num_rects):
            x1_b, y1_b, x2_b, y2_b = rectangles[j]

            # Condição de interseção estrita (área > 0)
            if max(x1_a, x1_b) < min(x2_a, x2_b) and max(y1_a, y1_b) < min(y2_a, y2_b):
                count += 1

    sys.stdout.write(f"{count}\n")

if __name__ == '__main__':
    solve()