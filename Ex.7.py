"""Дано ціле число N (> 2) і дві дійсні точки на числовій осі: A, B (A <B).
Функція F (X) задана формулою F (X) = 1 - sin (X). Вивести значення функції F в N
рівновіддалених точках, що утворюють розбиття відрізка
[A, B]: F (A), F (A + H), F (A + 2H), ..., F (B)"""


import math


def main(x):
    return 1 - math.sin(x)


if __name__ == "__main__":

    n = int(input(f"N (>2) = "))
    while n <= 2:
        n = int(input(f"Помилка! N (>2) = "))

    a = float(input(f"A = "))

    b = float(input(f"B (>A) = "))
    while b <= a:
        b = float(input(f"Помилка! B (>A) = "))

    h = (b - a) / n

    for i in range(n + 1):
        f = a + i * h
        print(main(f))