#!/usr/bin/env python3

def count_vowels(data):
    
    data = data.lower()
    count = 0
    
    for c in data:
        if c in "aeiou":
            count += 1
            
    return count

data = "Born To Code"
print(count_vowels(data))