# Lesson 5
# Task 3.1
import math
import numpy


def monte_carlo(k, n):
    a = numpy.random.randint(0, 2, n)
    b = numpy.random.randint(0, 2, n)
    c = numpy.random.randint(0, 2, n)
    d = numpy.random.randint(0, 2, n)

    x = a + b + c + d

    count = 0
    for i in range(0, n):
        if x[i] == k:
            count = count + 1

    p = count / n
    return p


def bernoulli(k, n):
    c = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    p = (c * 1) / 2 ** n
    return p


print(f'Вероятность выпадения 2 раз орла или 2 раз решки по методу Монте-Карло: \n'
      f'{monte_carlo(2, 1000)}')

print(f'Вероятность выпадения 2 раз орла или 2 раз решки по формуле Бернулли: \n'
      f'{bernoulli(2, 4)}')
