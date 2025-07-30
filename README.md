# 📊  Sprint 7 Herramientas para desarrollo de software


## 🎯 Actividad 1: Diseño y despliegue de un dashboard con Streamlit y Render

Este proyecto tiene como objetivo que los estudiantes trabajen en equipo para construir y desplegar una aplicación web interactiva utilizando **Streamlit**, a partir del análisis exploratorio de un conjunto de datos. Cada equipo podrá elegir entre tres datasets disponibles: uso de bicicletas, juegos de Steam o películas de IMDB.  

Deberán:
* Clonar el repositorio base.
* Realizar el EDA inicial en Jupyter Notebook.
* Crear una aplicación con al menos un filtro y una visualización interactiva.
* Cargar el repositorio en GitHub. 



El repo incluye un ejemplo que puedes usar de referencia:

```bash

streamlit run movie_app.py

```

![Ejemplo en render](https://sp7-colaborative-project.onrender.com/)



### 📌 Notas importantes:

* El nombre del CSV puede variar (`bikes.csv`, `steam_games.csv`, `imdb_movies.csv`), pero debe estar en la raíz del proyecto.
* El archivo `requirements.txt` debe contener al menos:
  ```
  pandas
  plotly
  streamlit
  ```
* El archivo `EDA.ipynb` debe contener gráficos y primeras impresiones sobre los datos.
* `README.md` debe incluir:
  - Descripción del dataset
  - Instrucciones para ejecutar la app
  - URL del despliegue (una vez publicado en Render)



---

## 🐍 Actividad 2: Diseña una calculadora

En este ejercicio trabajarás con clases en Python y el módulo `argparse` para construir una calculadora simple que puedas usar desde la terminal.

A partir del siguiente código base, deberás completar los métodos faltantes e implementar la lógica que permita ejecutar diferentes operaciones desde línea de comandos.

### Objetivos

1. Agregar los siguientes métodos a la clase `Calculator`:
   * `subtract(a, b)`
   * `multiply(a, b)`
   * `divide(a, b)` → **Manejo especial si `b == 0`**

2. Completar la lógica dentro del método `operate()` para que se ejecuten correctamente las nuevas operaciones según el argumento `--operation`.

3. (Opcional) Crear un nuevo método llamado `show_memory()` que imprima el último resultado guardado en el atributo `memory`.

4. Cargar el repositorio en GitHub

---

### Ejemplos de uso esperado

```bash
# Suma simple
python calculadora.py --operation add --numbers 5 3
```

> 8.0

```bash
# Multiplicación en modo verbose
python calculadora.py --operation multiply --numbers 2 4 --verbose
```

> 🧮 Multiplying 2.0 * 4.0 = 8.0

```bash
# División por cero
python calculadora.py --operation divide --numbers 10 0
```

> ❌ Error: No se puede dividir entre cero.

---

> ✅ ¡Usa `--verbose` para ver mensajes detallados!
> ✅ Recuerda que puedes usar `argparse` para recibir argumentos desde la línea de comandos.
