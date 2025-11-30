# 🐍 **Retos Python Básicos**🐍 

**Colección de ejercicios para desarrollar habilidades prácticas**

Este repositorio reúne una selección de 15 ejercicios de Python pensados para mejorar de forma progresiva el razonamiento, la lógica y el dominio de las estructuras fundamentales del lenguaje. Cada reto está diseñado para practicar conceptos clave de programación y para demostrar un enfoque claro, ordenado y eficaz a la hora de resolver problemas reales.

Mi objetivo al construir este repositorio es ir ampliando y practicando habilidades en Python, manteniendo buenas prácticas y código limpio. Además, sirve como referencia para cualquier persona que quiera repasar fundamentos o ver ejemplos de soluciones limpias a ejercicios comunes.

---

### **Cómo ejecutar los ejercicios (desde terminal de Linux).**

En cada script incluye la línea `#!/usr/bin/env python3`, para que pueda ejecutarse directamente desde la terminal.

1. Dale permisos de ejecución al fichero:

```sh
chmod +x nombre_ejercicio.py
```

2. Ejecútalo:

```sh
./nombre_ejercicio.py
```

---

Si prefieres ejecutarlo sin permisos, también puedes usar:

```sh
python3 nombre_ejercicio.py
```

# **Enunciados de los 15 ejercicios**

### **1. Contador de palabras**

Escribe una función que reciba un texto y devuelva un diccionario donde las claves sean las palabras y los valores el número de veces que aparece cada una de ellas. Ignora mayúsculas/minúsculas.

[word_counter.py](https://github.com/maramartinezvargas/RetosPython/word_counter.py)

---

### **2. Filtrar números pares**

Dada una lista de números enteros, genera una nueva lista que contenga únicamente los números pares utilizando comprensión de listas.

[filter_even_numbers.py](https://github.com/maramartinezvargas/RetosPython/filter_even_numbers.py)

---

### **3. Máximo y mínimo sin funciones built-in**

Dada una lista de números, calcula el valor máximo y el mínimo sin utilizar las funciones `max()` ni `min()`.

[manual_max_min.py](https://github.com/maramartinezvargas/RetosPython/manual_max_min.py)

---

### **4. Comprobar si una palabra es palíndroma**

Implementa una función que determine si una palabra o frase es un palíndromo. No debe tener en cuenta espacios ni mayúsculas.

[is_palindrome.py](https://github.com/maramartinezvargas/RetosPython/is_palindrome.py)

---

### **5. Eliminar elementos duplicados**

Crea una función que reciba una lista y devuelva una nueva lista con los elementos únicos, manteniendo cualquier orden válido.

[remove_duplicates.py](https://github.com/maramartinezvargas/RetosPython/remove_duplicates.py)

---

### **6. FizzBuzz**

Escribe un programa que imprima los números del 1 al 50.

* Si el número es múltiplo de 3, imprime “Fizz”.
* Si es múltiplo de 5, imprime “Buzz”.
* Si es múltiplo de ambos, imprime “FizzBuzz”.

[fizzbuzz.py](https://github.com/maramartinezvargas/RetosPython/fizzbuzz.py)

---

### **7. Sumar valores de un diccionario**

Dado un diccionario cuyas claves son cadenas y cuyos valores son números, implementa una función que calcule la suma total de esos valores.

[dict_sum_values.py](https://github.com/maramartinezvargas/RetosPython/dict_sum_values.py)

---

### **8. Contador de vocales**

Escribe una función que reciba una cadena de texto y devuelva cuántas vocales contiene (a, e, i, o, u), sin diferenciar mayúsculas de minúsculas.

[count_vowels.py](https://github.com/maramartinezvargas/RetosPython/count_vowels.py)

---

### **9. Frecuencia de caracteres**

Implementa una función que reciba una cadena de texto y genere un diccionario que indique cuántas veces aparece cada carácter individual.

[char_frequency.py](https://github.com/maramartinezvargas/RetosPython/char_frequency.py)

---

### **10. Invertir un diccionario**

Crea una función que reciba un diccionario y devuelva uno nuevo donde las claves sean los valores originales y los valores sean las claves. Supón que los valores no están repetidos.

[invert_dict.py](https://github.com/maramartinezvargas/RetosPython/invert_dict.py)

---

### **11. Análisis básico de un fichero de texto**

Escribe un programa que abra un fichero de texto y muestre:

1. El número total de líneas.
2. El número total de palabras.
3. La palabra que se repite con más frecuencia.

[file_basic_analysis.py](https://github.com/maramartinezvargas/RetosPython/file_basic_analysis.py)

---

### **12. Aplanar una lista**

Dada una lista que contiene listas internas (por ejemplo `[1, [2, 3], [4, 5]]`), implementa una función que devuelva una lista “aplanada” en un único nivel.

[flatten_list.py](https://github.com/maramartinezvargas/RetosPython/flatten_list.py)

---

### **13. Clase Persona**

Define una clase `Person` con los atributos `name` y `age`. Añade un método `introduce()` que muestre un mensaje utilizando ambos atributos.

[class_person.py](https://github.com/maramartinezvargas/RetosPython/class_person.py)

---

### **14. Implementar un CRUD sencillo**

Crea una clase que gestione una lista de elementos y permita realizar estas operaciones:

* añadir un elemento,
* eliminar un elemento,
* comprobar si un elemento existe,
* listar todos los elementos almacenados.
  
[simple_crud_manager.py](https://github.com/maramartinezvargas/RetosPython/simple_crud_manager.py)

---

### **15. Consumir una API pública**

Implementa una función que realice una petición GET a la API:

`https://api.agify.io/?name=<nombre>`

y devuelva la edad estimada para el nombre proporcionado. (**Explicación más detallada abajo del todo*)

[consume_public_api.py](https://github.com/maramartinezvargas/RetosPython/consume_public_api.py)

---

# **Conceptos básicos necesarios para resolver estos ejercicios**

Esta sección recopila los fundamentos de Python que resultan más útiles para abordar los retos de este repositorio. Sirve como guía rápida tanto para repasar conceptos como para profundizar en ellos mientras se practica.

---

## **1. Tipos de datos fundamentales**

### **Numéricos**

* `int`: números enteros
* `float`: números decimales

### **Texto**

* `str`: cadenas de texto
  Métodos frecuentes: `.lower()`, `.upper()`, `.split()`, `.strip()`, `.replace()`

### **Colecciones**

* `list`: ordenadas, mutables
* `tuple`: ordenadas, inmutables
* `dict`: pares clave–valor
* `set`: colecciones sin duplicados

---

## **2. Estructuras de control**

### **Condicionales**

```python
if condicion:
    ...
elif otra_condicion:
    ...
else:
    ...
```

### **Bucles**

* `for` para iterar sobre listas, strings, diccionarios…
* `while` cuando necesitas repetir hasta que algo cambie

Palabras clave útiles: `break`, `continue`, `range()`

---

## **3. Comprensiones (muy útiles en Python)**

### **List comprehension**

```python
[n for n in lista if n % 2 == 0]
```

### **Dict comprehension**

```python
{k: len(k) for k in palabras}
```

---

## **4. Funciones**

Cómo definir funciones:

```python
def nombre_funcion(parametros):
    return algo
```

Conceptos clave:

* parámetros vs argumentos
* valores por defecto
* return
* scope de variables

---

## **5. Manejo básico de ficheros**

```python
with open("archivo.txt", "r") as f:
    contenido = f.read()
```

Modos típicos:

* `"r"` leer
* `"w"` escribir
* `"a"` añadir
* `"rb"` leer binario

Funciones frecuentes:

* `.read()`
* `.readlines()`
* iteración línea a línea

---

## **6. Diccionarios: claves y valores**

Métodos clave:

* `.keys()`
* `.values()`
* `.items()`
* `.get(clave, valor_por_defecto)`

Son esenciales para ejercicios de conteo y análisis.

---

## **7. Manejo de errores**

```python
try:
    ...
except FileNotFoundError:
    ...
except Exception as e:
    ...
finally:
    ...
```

Sirve para:

* ficheros inexistentes
* accesos inválidos
* evitar que un programa se rompa

---

## **8. Programación orientada a objetos (POO)**

Clase básica:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Conceptos:

* clases
* objetos
* atributos
* métodos
* `self`

---

## **9. Módulos y organización de código**

Importar módulos:

```python
import math
import random
from collections import Counter
```

Crear modularidad:

* separar ejercicios en ficheros
* mantener funciones aisladas
* usar nombres descriptivos

---

## **10. Consumo de APIs**

Paquete más común:

```python
import requests

r = requests.get("https://api.example.com")
data = r.json()
```

### Conceptos básicos para realizar el ejercicio

En este reto se practica cómo **consumir una API pública** desde Python utilizando la librería `requests`.

La API utilizada es **Agify**:

```
https://api.agify.io/?name=<nombre>
```

Esta API devuelve una estimación de la edad media asociada a un nombre. Por ejemplo:

```
https://api/agify.io/?name=alex
```

responde algo así:

```json
{
  "name": "alex",
  "age": 32,
  "count": 12345
}
```

El objetivo del ejercicio es:

1. Pedir un nombre al usuario por consola.
2. Enviar ese nombre a la API mediante una petición **GET** con `requests.get()`.
3. Convertir la respuesta JSON en un diccionario de Python usando `response.json()`.
4. Extraer el valor de `"age"` del diccionario.
5. Mostrar la edad estimada por pantalla.
6. Manejar errores básicos de red con `try/except`.

No se necesita API key ni autenticación, así que es un ejercicio ideal para aprender a trabajar con APIs sencillas y datos en formato JSON.


