#!/usr/bin/env python3

"""
14. Implementar un CRUD sencillo
Fichero: simple_crud_manager.py

Crea una clase que gestione una lista de elementos y permita realizar estas operaciones:

añadir un elemento,
eliminar un elemento,
comprobar si un elemento existe,
listar todos los elementos almacenados.
"""

class BookCollection():
    
    def __init__(self):
        self.books = []
        
    def add(self, book):
        self.books.append(book)
    
    def exists(self, book):
        return book in self.books
    
    def delete(self, book):
         if book in self.books:
            self.books.remove(book)
    
    def list_all(self):
        return self.books
    
    def __str__(self):
        return "\n".join(self.books)

collection = BookCollection()
collection.add("1984")
collection.add("Un mundo feliz")
collection.add("El cuento de la criada")
collection.add("Una habitación propia")
collection.add("Lore")
collection.add("Los reinos del este")

print("--- LISTADO COMPLETO ---")

print(collection)

book = "Lore"
if collection.exists(book):
    print(f"El libro {book} SI existe")
else:
    print(f"El libro {book} NO existe")

print(f"\nSe elimina el libro {book}\n")
collection.delete(book)

print("--- LISTADO TRAS ELIMINAR UN LIBRO ---")
print(collection)