# 📊 Proyectos colaborativos con Streamlit

Este repositorio contiene tres propuestas de proyectos colaborativos para estudiantes, donde podrán practicar análisis exploratorio de datos, visualización interactiva con Streamlit, uso de Git y despliegue en Render 🚀

---

## 🚲 Bike Sharing Dataset

**Descripción**:  
Datos de alquiler de bicicletas por hora/día en Washington DC durante 2011 y 2012. Incluye variables meteorológicas y tipo de día.

### Diccionario de datos

| Columna       | Descripción                                                                 |
|---------------|------------------------------------------------------------------------------|
| season        | Estación del año (1: invierno, 2: primavera, 3: verano, 4: otoño)            |
| yr            | Año (0: 2011, 1: 2012)                                                       |
| mnth          | Mes del año (1 a 12)                                                         |
| hr            | Hora del día (0 a 23)                                                        |
| weekday       | Día de la semana (0: domingo, ..., 6: sábado)                                |
| workingday    | Día laboral (1) o no (0)                                                     |
| weathersit    | Situación climática (1: despejado, 2: nubes, 3: lluvia ligera, 4: tormenta)  |
| temp          | Temperatura normalizada en Celsius                                           |
| atemp         | Sensación térmica normalizada                                                |
| hum           | Humedad relativa                                                             |
| windspeed     | Velocidad del viento normalizada                                             |
| casual        | Usuarios ocasionales                                                         |
| registered    | Usuarios registrados                                                         |
| cnt           | Total de bicicletas alquiladas                                               |

### EDA sugerido

1. Distribución de uso por hora (`cnt` vs `hr`)
2. Comparación de uso entre días laborales y fines de semana
3. Influencia del clima (`weathersit`) en la cantidad de bicicletas alquiladas

### Requisitos mínimos de la app

* Título: *Análisis del uso de bicicletas en DC*
* Filtro: Selección por estación o tipo de día
* Gráficos sugeridos:
  - Histograma del total de alquileres (`cnt`)
  - Boxplot de `cnt` por tipo de clima (`weathersit`)
  - Gráfico de barras de uso promedio por hora

---

## 🎮 Steam Games Dataset

**Descripción**:  
Información de juegos publicados en Steam, incluyendo su género, precio, número de reseñas y número estimado de jugadores.

### Diccionario de datos

| Columna           | Descripción                                 |
|-------------------|----------------------------------------------|
| name              | Nombre del juego                             |
| release_date      | Fecha de lanzamiento                         |
| price             | Precio en USD                                |
| positive_ratings  | Número de reseñas positivas                  |
| negative_ratings  | Número de reseñas negativas                  |
| owners            | Rango estimado de propietarios               |
| genres            | Géneros del juego                            |

### EDA sugerido

1. Relación entre precio y reseñas positivas
2. Juegos más populares por cantidad de propietarios
3. Distribución de juegos por género

### Requisitos mínimos de la app

* Título: *Explorando juegos populares en Steam*
* Filtro: Por género o rango de precio
* Gráficos sugeridos:
  - Dispersión: Precio vs. Reseñas positivas
  - Barras: Top géneros más comunes
  - Histograma de precios

---

## 🎬 IMDB Movies Dataset

**Descripción**:  
Películas mejor valoradas en IMDB, con datos como duración, recaudación y género.

### Diccionario de datos

| Columna       | Descripción                   |
|---------------|-------------------------------|
| Title         | Título de la película         |
| Year          | Año de estreno                |
| Genre         | Género(s)                     |
| IMDB_Rating   | Calificación IMDB             |
| Duration      | Duración (minutos)            |
| Gross         | Recaudación en taquilla (USD) |

### EDA sugerido

1. Distribución de calificaciones IMDB
2. Comparación de recaudación por género
3. Evolución del rating por año

### Requisitos mínimos de la app

* Título: *Análisis de películas destacadas en IMDB*
* Filtro: Por década, género o duración
* Gráficos sugeridos:
  - Histograma de calificaciones
  - Boxplot de recaudación (`Gross`) por género
  - Línea promedio de rating por año

---



## 📁 Estructura mínima del proyecto

Cada equipo o estudiante debe mantener esta estructura de archivos para asegurar orden y facilidad de despliegue:

```
my_project/
├── app.py                  # Script principal de Streamlit
├── requirements.txt        # Lista de paquetes necesarios (mínimo: streamlit, pandas, plotly-express)
├── README.md               # Descripción del proyecto
├── <dataset>.csv           # Archivo CSV con el conjunto de datos
├── notebooks/
│   └── EDA.ipynb           # Análisis exploratorio con Jupyter Notebook
```

### 📌 Notas importantes:

* El nombre del CSV puede variar (`bikes.csv`, `steam_games.csv`, `imdb_movies.csv`), pero debe estar en la raíz del proyecto.
* El archivo `requirements.txt` debe contener al menos:
  ```
  pandas
  plotly-express
  streamlit
  ```
* El archivo `EDA.ipynb` debe contener gráficos y primeras impresiones sobre los datos.
* `README.md` debe incluir:
  - Descripción del dataset
  - Instrucciones para ejecutar la app
  - URL del despliegue (una vez publicado en Render)

