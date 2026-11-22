
# ============================================================
# PROYECTO: LA POKEDEX COMPLETA
# Fundamentos de Python - Entrega final
# ============================================================

# Importamos las librerías necesarias
import requests
import json
import os
import webbrowser


# Dirección principal de la API
API_URL = "https://pokeapi.co/api/v2/pokemon/"


def consultar_pokemon(nombre):
    """Consulta los datos de un Pokémon mediante la PokéAPI."""

    url = API_URL + nombre.lower()

    try:
        respuesta = requests.get(url, timeout=15)

        # Validamos el código de respuesta HTTP
        if respuesta.status_code == 200:
            return respuesta.json()

        elif respuesta.status_code == 404:
            print("\nError 404: Pokémon no encontrado.")
            return None

        else:
            print("Error HTTP:", respuesta.status_code)
            return None

    except requests.exceptions.Timeout:
        print("Error: Se agotó el tiempo de espera.")

    except requests.exceptions.ConnectionError:
        print("Error: No hay conexión a Internet.")

    except requests.exceptions.RequestException as error:
        print("Error al consultar la API:", error)

    return None


def mostrar_informacion(datos):
    """Muestra las características principales del Pokémon."""

    print("\n" + "=" * 45)
    print("           INFORMACIÓN DEL POKÉMON")
    print("=" * 45)

    print("Nombre:", datos["name"].capitalize())
    print("Número:", datos["id"])
    print("Peso:", datos["weight"] / 10, "kg")
    print("Altura:", datos["height"] / 10, "m")

    # Mostramos los tipos del Pokémon
    tipos = [tipo["type"]["name"] for tipo in datos["types"]]
    print("Tipos:", ", ".join(tipos))

    # Mostramos las habilidades
    habilidades = [
        habilidad["ability"]["name"]
        for habilidad in datos["abilities"]
    ]
    print("Habilidades:", ", ".join(habilidades))

    # Mostramos las estadísticas
    print("\nESTADÍSTICAS:")
    for estadistica in datos["stats"]:
        nombre = estadistica["stat"]["name"]
        valor = estadistica["base_stat"]
        print(f"- {nombre.capitalize()}: {valor}")

    # Mostramos algunos movimientos
    print("\nMOVIMIENTOS:")
    for movimiento in datos["moves"][:10]:
        print("-", movimiento["move"]["name"])

    # Obtenemos la imagen frontal del Pokémon
    imagen = datos["sprites"]["front_default"]

    if imagen:
        print("\nImagen frontal:", imagen)
        webbrowser.open(imagen)
    else:
        print("\nEl Pokémon no tiene imagen frontal disponible.")


def guardar_pokemon(datos):
    """Guarda los datos del Pokémon en un archivo JSON."""

    # Creamos la carpeta si todavía no existe
    os.makedirs("pokemon", exist_ok=True)

    nombre = datos["name"].lower()
    archivo = os.path.join("pokemon", nombre + ".json")

    try:
        with open(archivo, "w", encoding="utf-8") as documento:
            json.dump(datos, documento, indent=4, ensure_ascii=False)

        print("\nDatos guardados correctamente en:", archivo)

    except OSError as error:
        print("Error al guardar el archivo:", error)


def iniciar_pokedex():
    """Controla el funcionamiento general de la Pokédex."""

    print("=" * 45)
    print("          ¡BIENVENIDO A LA POKÉDEX!")
    print("=" * 45)

    while True:
        nombre = input(
            "\nEscribe el nombre de un Pokémon "
            "o escribe 'salir' para terminar: "
        ).strip()

        if nombre.lower() == "salir":
            print("\nGracias por utilizar la Pokédex.")
            break

        if not nombre:
            print("Debes escribir un nombre.")
            continue

        datos = consultar_pokemon(nombre)

        # Si la consulta fue exitosa, mostramos y guardamos
        if datos:
            mostrar_informacion(datos)
            guardar_pokemon(datos)


# Punto de entrada del programa
if __name__ == "__main__":
    iniciar_pokedex()
