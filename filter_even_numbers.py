#!/usr/bin/env python3

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result = [n for n in nums if n % 2 == 0]

print("Lista original: ", nums)
print("\nLista por comprensión: ", result)