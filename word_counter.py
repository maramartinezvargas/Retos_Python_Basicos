#!/usr/bin/env python3

def word_counter(text):
    text = text.lower()

    counter = {}
    
    words = text.split()
    
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    
    return counter

text = "Hola qué tal mundo Hola muy bien mundo"
print(word_counter(text))