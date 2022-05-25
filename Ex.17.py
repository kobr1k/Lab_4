"""Дано ціле число N (> 1). Знайти найменше ціле число K, при якому виконується нерівність 3K> N."""


def main(n: int, k=1):
    while not 3 ** k > n:
        k += 1
    return k


if __name__ == '__main__':
    N = int(input('N = '))

    result = main(N, 1)
    print(result)