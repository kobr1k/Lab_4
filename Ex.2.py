"""
2.Визначити, чи є задане натуральне число досконалим, тобто рівним сумі всіх своїх дільників, крім
самого цього числа (наприклад, число 6 досконале: 6 = 1 + 2 + 3).
"""


def main(n: int):
    sum_ = 0
    for divisor in range(1, n):
        if n % divisor == 0:
            sum_ += divisor

    return 'Yes' if sum_ == n else 'No'


if __name__ == '__main__':
    value = int(input('Enter value: '))
    result = main(value)
    print(result)

