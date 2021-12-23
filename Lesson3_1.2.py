# Lesson 3
# Task 1.2
# Calculating the length of a vector
import math


def vector_length(vector):
    if len(vector) == 2:
        lenght = math.sqrt((vector[0] ** 2) + (vector[1] ** 2))
    elif len(vector) == 3:
        lenght = math.sqrt((vector[0] ** 2) + (vector[1] ** 2) + (vector[2] ** 2))
    return lenght


vector_a = (input('Enter the coordinates of the vector separated by a space: ').strip()).split()
vector_a = [int(i) for i in vector_a]
len_vector_a = vector_length(vector_a)
print(f'The lenght of the vector: {len_vector_a}')
