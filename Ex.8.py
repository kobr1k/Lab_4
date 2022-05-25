"""
 8.Дано дійсне A та ціле число N (> 0). Вивести 1 – A + A2 – A3 + ... + (–1)^N*AN.
"""


def main(a: float, n: int, x=1, result=1):
    if n > 0:
        for i in range(n):
            x *= -a
            result += x
        print("Відповідь: ", result)
    else:
        print("Помилка: Введіть N > 0")


if __name__ == '__main__':
    A = float(input("Введіть дійсне A = "))
    N = int(input("Введіть ціле N = "))
    main(A, N, 1, 1)
