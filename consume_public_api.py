#!/usr/bin/env python3

# 1. Importar la librería requests para poder hacer peticiones HTTP
import requests

def get_estimated_age(name):
    # 2. URL base de la api pública agify
    url = "https://api.agify.io/"
    # 3. Definir parámetros con el nombre
    params = {"name": name}
    
    # 4. Construir la URL completa y hacer la petición HTTP (con request.get())
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Lanza excepción si no es 200 OK
    except Exception as e:
        # 5. En caso de error, se muestra un mensaje y se devuelve None
        print(f"Error al hacer la petición: {e}")
        return None
    # 6. Parsear la respuesta JSON a dict
    data = response.json()

    # 7. Devolver la edad usando .get("age")
    return data.get("age")

if __name__ == "__main__":
    # 8. Pedir al usuario un nombre
    name = input("Escribe tu nombre: ")
    # 9. Llamar a la función
    age = get_estimated_age(name)
    # 10. Controlar si el valor recibido es None
    if age is not None:
        print(f"La gente de nombre {name} tiene una media de {get_estimated_age(name)} años.")
    else:
        print(f"No se ha podido obtener la edad estimada para '{name}'.")

