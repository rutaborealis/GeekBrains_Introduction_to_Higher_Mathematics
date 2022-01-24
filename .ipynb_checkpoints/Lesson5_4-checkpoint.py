# Lesson 5
# Task 4
import itertools

for p in itertools.permutations('012345', 2):
    print(''.join(str(x) for x in p))

print()

for p in itertools.combinations('012345', 3):
    print(''.join(str(x) for x in p))
