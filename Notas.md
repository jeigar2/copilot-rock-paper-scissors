# Notas

## prompts para resolver el ejercicio

1.  prompt describir someramente el juego

```yml
quiero crear el juego de piedra papel o tijera con dos elementos mas lizard y spock. piedra pierde ante spock, papel gana a spock, tijera gana a lizard y lizard gana a papel... el juego será en la terminal $ Choose your option:

- Rock
- Paper
- Scissors
- Lizard
- Spock
```

2. prompt crear test de covertura

```yml
@workspace /tests Implement unit tests using pytest or any testing module of your choice. Try to aim for 100% coverage
```

3. Me pide habilitar algo
  - `@workspace /tests Accept: "Configure Test Framework"`

3. prompt insisto en la creación de test
  - `implementa ahora los test`

4. prompt crear una api

```yml
Adding a REST API Turn it into a REST API E.g. sending a POST /rock (or json payload) should return a 200 OK response with the result in the body
```

5. prompt extra, para crear módulo de estadísticas

```yml
puedes hacer un módulo que vaya almacenado las estadísticas de cuantas veces gana cada uno y que opciones han salido más, ya sea jugando desde consola o desde la api, y muestras una gráfica el resultado
```

6. prompt extra para tener entorno

`quiero crear un entorno para instalar las dependencias`

## Generar un fichero requirements.txt

Guardar las dependencias en un archivo requirements.txt:

Ejecuta el siguiente comando para guardar las dependencias instaladas en un archivo requirements.txt:

`pip freeze > requirements.txt`

El archivo requirements.txt debería verse algo así:

```ini
click==8.0.1
Flask==2.0.1
itsdangerous==2.0.1
Jinja2==3.0.1
MarkupSafe==2.0.1
matplotlib==3.4.2
numpy==1.21.0
Pillow==8.2.0
pyparsing==2.4.7
python-dateutil==2.8.1
six==1.16.0
sqlite3==0.0.1
Werkzeug==2.0.1
```

- Ahora, cualquier persona que quiera replicar tu entorno puede hacerlo siguiendo estos pasos:
  1. Clonar el repositorio o copiar los archivos del proyecto.
    - `git clone https://github.com/copilot-workshops/copilot-rock-paper-scissors`
  2. Crear y activar un entorno virtual.
    - `python3 -m venv venv`
    - activar el entorno en Windows
        - `source venv/Scripts/activate`
    - activar el entorno en Windows
        - `.\venv\Scripts\activate`
  3. Instalar las dependencias desde el archivo requirements.txt:
    - `pip install -r requirements.txt` 

Esto asegurará que todas las dependencias necesarias estén instaladas en el entorno virtua