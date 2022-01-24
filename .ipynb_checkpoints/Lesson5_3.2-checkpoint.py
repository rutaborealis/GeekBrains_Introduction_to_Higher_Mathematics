# Lesson 5
# Task 3.2
import math


def bernoulli(k, n):
    p = 0.5
    q = 1 - p
    c = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    result = c * (p ** k) * (q ** (n - k))
    return result


k = 3
n = 4
print(f'Расчет по формуле Бернулли: \n'
      f'{bernoulli(k, n)}')
