# 🟡 La Pokédex Completa

## Fundamentos de Python – Entrega final

### 1. Descripción del proyecto

Este proyecto consiste en desarrollar una Pokédex utilizando Python y la API pública PokéAPI. El programa permite consultar información de diferentes Pokémon mediante su nombre y mostrar sus características principales.

### 2. Objetivo

Aplicar los conocimientos adquiridos durante el curso de Python mediante el consumo de una API web, el manejo de datos JSON, la utilización de funciones y módulos, y el almacenamiento de información en archivos.

### 3. Funcionamiento del programa

El programa solicita al usuario el nombre de un Pokémon. Posteriormente, realiza una petición a PokéAPI para obtener su información.

Cuando la consulta es exitosa, muestra los siguientes datos:

- Nombre y número del Pokémon.
- Peso y altura.
- Tipos.
- Habilidades.
- Estadísticas.
- Movimientos.
- Enlace de su imagen frontal.

También guarda automáticamente la información recibida en un archivo JSON individual dentro de la carpeta `pokemon`.

### 4. API utilizada

**PokéAPI**

https://pokeapi.co/api/v2/pokemon/

Se utiliza el método GET mediante la librería requests para obtener información de los Pokémon.

### 5. Librerías utilizadas

- requests: permite realizar solicitudes HTTP a la API.
- json: permite guardar la información en formato JSON.
- os: permite crear carpetas y administrar archivos.
- webbrowser: permite abrir la imagen frontal del Pokémon.

### 6. Manejo de errores

El programa contempla diferentes situaciones:

- Código 200: consulta exitosa.
- Código 404: Pokémon no encontrado.
- Otros códigos HTTP: muestra el código del error.
- Error de conexión: informa cuando no hay conexión a Internet.
- Tiempo de espera agotado: muestra un mensaje cuando la API tarda demasiado en responder.

### 7. Organización del proyecto

```text
CURSO PYTHON/
│
├── main.py
├── README.md
│
└── pokemon/
    ├── pikachu.json
    └── charizard.json
```

### 8. Reflexión personal

Durante el desarrollo de este proyecto aprendí a consumir una API utilizando Python y a trabajar con información que proviene de una fuente externa.

Comprendí la importancia de utilizar funciones para organizar el código y facilitar su mantenimiento. También aprendí a utilizar módulos como requests, json, os y webbrowser para realizar diferentes tareas.

Otro aprendizaje importante fue el manejo de los códigos de estado HTTP, ya que es necesario identificar cuándo una consulta se realiza correctamente y cuándo ocurre algún error.

Finalmente, comprendí cómo guardar información en archivos JSON para conservar los datos obtenidos y poder utilizarlos posteriormente.

### 9. Conclusión

La elaboración de esta Pokédex me permitió poner en práctica los conocimientos adquiridos durante el curso de Fundamentos de Python. Considero que fue una actividad útil porque pude integrar diferentes herramientas y comprender mejor cómo funcionan las API y el manejo de archivos en Python.