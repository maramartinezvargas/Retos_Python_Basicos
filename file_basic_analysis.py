#!/usr/bin/env python3

def file_basic_analysic(textFile):
    
    with open(textFile,"r") as f:
        content = f.read()
    
        lines = content.split("\n")
        countLines = len(lines)
        
        for ch in [".", ",", "!", "?", ";", ":"]:
            content = content.replace(ch, "")
        
        words = content.split()
        
        freq = {}
        for word in words:
            w = word.lower()
            if w in freq:
                freq[w] += 1
            else:
                freq[w] = 1
        most_common = max(freq, key=freq.get)
            
    print("Número de lineas: ", countLines)
    print("Número de palabras: ", len(words))
    print("Palabra con más frecuencia: ", most_common)

def main():
    file_basic_analysic("text.txt")
    
if __name__ == "__main__":
    main()