#!/usr/bin/env python3

nums = [25,65,89,10,122,568,5]

min = nums[0]
max = nums[0]

for n in nums:
    if n > max:
        max = n
    if n < min:
        min = n

print("El máximo es: ", max)
print("El mínimo es: ", min)