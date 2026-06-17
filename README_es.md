# ContextFilter  

### Minimum Viable Product (MVP) para el filtrado de contenido

[![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/) [![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow.svg)](https://huggingface.co/docs/transformers) [![PyTorch](https://img.shields.io/badge/PyTorch-red.svg)](https://pytorch.org/)  

Aplicación para analizar y filtrar reseñas o contenido textual mediante _pipelines zero-shot_ de Transformers según un umbral de evaluación configurable.

## Traducciones

- [Read in English](README.md)
- [Llegir en Català](README_ca.md)

## Visión General

Este repositorio contiene una aplicación MVP desarrollada en el marco de la asignatura de la Universitat Oberta de Catalunya (UOC) **Diseño de Productos de Datos**.

El prototipo, implementado en un notebook Jupyter de Python, utiliza clasificación **Zero-Shot** mediante modelos de lenguaje para evaluar el grado de correspondencia entre un texto y un conjunto de etiquetas semánticas candidatas.

El sistema funciona enviando un texto a una API, que evalúa su relación con las etiquetas definidas y calcula un score global a partir de los resultados obtenidos por el modelo. Este valor se compara con un umbral configurable para determinar si el contenido cumple los criterios establecidos.

El sistema está diseñado para ser flexible, permitiendo añadir o sustituir etiquetas semánticas, modificar el umbral de evaluación y procesar tanto textos individuales como archivos con múltiples registros en diferentes formatos.

El objetivo es proporcionar a los _stakeholders_ un prototipo funcional que permita explorar qué configuración de etiquetas y qué umbral de evaluación se adaptan mejor a los criterios que una organización necesita valorar.

## Características Principales

- Soporte para textos individuales en diferentes idiomas mediante normalización del contenido.
- Posibilidad de añadir o sustituir filtros semánticos respecto a los definidos inicialmente en la aplicación.
- Pipeline clasificador Zero-Shot basado en modelos de **Hugging Face Transformers**.
- Ejecución local de los modelos mediante **PyTorch**.
- Envío y procesamiento de archivos con conjuntos de reseñas o textos en diferentes formatos.
- API implementada con **FastAPI** dentro del mismo notebook, controlada mediante _ipywidgets_.
- Configuración flexible de los criterios de clasificación mediante etiquetas semánticas personalizables.
- Registro y auditoría de las peticiones procesadas.

## Resultados

La finalidad principal del proyecto es evaluar el comportamiento del sistema de filtrado y analizar su capacidad de adaptación mediante diferentes configuraciones de etiquetas semánticas.

Esta fase no tiene como objetivo determinar la combinación definitiva de etiquetas, sino analizar el funcionamiento del producto y establecer una base para futuras optimizaciones.

Los resultados de las evaluaciones del modelo pueden consultarse en la versión HTML del [_notebook de métricas_](metrics.html).

## Contexto del Mundo Real

La aplicación está planteada como un servicio de filtrado semántico capaz de recibir contenido desde diferentes clientes y determinar si este se ajusta a los criterios definidos por una organización.

Un posible caso de uso es la moderación de reseñas, diferenciando entre comentarios tóxicos y opiniones negativas pero constructivas. Una plataforma con únicamente opiniones positivas puede perder credibilidad, mientras que la identificación de contenido inadecuado ayuda a mantener un entorno de participación de mayor calidad.

La flexibilidad del sistema permite adaptar los filtros a diferentes necesidades mediante la configuración de parejas semánticas y umbrales de evaluación. Por ejemplo, se podría identificar contenido relacionado con restauración y diferenciar entre una crítica válida de un cliente y un comentario no relacionado u ofensivo.

## Stack Tecnológico

> Centrado en el procesamiento del lenguaje natural mediante modelos de lenguaje e inferencia local.

- **Lenguaje de Programación**: Python (>= 3.12)
- **Modelos de Lenguaje e Inferencia**: Hugging Face Transformers, PyTorch
- **Procesamiento de Datos**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **Visualización de Datos**: Matplotlib, Seaborn
- **Auditoría y registro del servicio**: TinyDB
- **Interfaz Interactiva**: Jupyter Notebook, ipywidgets
- **Gestión de API y servidor**: FastAPI, Uvicorn
- **Gestión del entorno**: uv / pip (mediante pyproject.toml)
- **Gestión de idiomas**: langdetect, deep-translator
- **Enfoque de Modelado**: Clasificación Zero-Shot mediante Transformers

## Conjuntos de Datos

El conjunto de datos utilizado para validar el filtro de toxicidad se ha obtenido del repositorio de GitHub de Prajwal Krishna, desarrollado para el reto *Toxic Comment Classification Challenge* de Kaggle.

El repositorio original se puede consultar en:

https://github.com/praj2408/Jigsaw-Toxic-Comment-Classification

La competición correspondiente de Kaggle está disponible en:

https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge

Muchas gracias a Prajwal Krishna y a Kaggle por poner estos recursos a disposición de la comunidad y contribuir al desarrollo de herramientas relacionadas con el procesamiento del lenguaje natural y la detección de toxicidad.

Además, se ha generado un conjunto propio de 200 reseñas:
- 100 reseñas relacionadas con restaurantes.
- 100 reseñas no relacionadas con esta temática.

Este conjunto se ha utilizado para evaluar otros filtros semánticos, especialmente la detección de contenido relacionado con un dominio concreto.

## Estructura del Repositorio

El repositorio contiene el notebook principal del prototipo/MVP, un notebook de evaluación de métricas, scripts auxiliares y los diferentes archivos de datos utilizados durante las pruebas.

* `contextFilter.ipynb`: Notebook principal del prototipo. Una vez ejecutado, activa una API para evaluar textos y permite realizar pruebas mediante una interfaz interactiva basada en widgets.
* `metrics.ipynb`: Notebook donde se evalúa el funcionamiento del prototipo mediante diferentes conjuntos de datos y configuraciones.
* `metrics.html`: Conversión del notebook de métricas a formato HTML para facilitar su visualización.
* `ipy_multil_mvm.py`: Script con rutinas, variables y etiquetas necesarias para el notebook `contextFilter.ipynb`.
* `requirements.txt`: Paquetes necesarios para ejecutar los notebooks.
* `pyproject.toml`: Archivo utilizado por `uv` con la descripción y dependencias del proyecto.
* Carpeta `data/`: Contiene los archivos de prueba preparados:
  * `en_3000.csv`: Primeras 3000 reseñas del dataset de toxicidad preparadas para la evaluación.
  * `en_1_10.csv`: Selección inicial de 10 reseñas del dataset tóxico.
  * `en_11_20.txt`: Reseñas 11 a 20 del dataset tóxico en formato TXT.
  * `en_21_30.json`: Reseñas 21 a 30 del dataset tóxico en formato JSON.
  * `rev_restaurants.csv`: Dataset propio con 200 reseñas relacionadas y no relacionadas con restaurantes.
  * `rest_1_10.csv`: Primeras 10 reseñas del dataset de restaurantes.
  * `rest_11_20.csv`: Reseñas 11 a 20 del dataset de restaurantes en formato TXT.
  * `rest_21_30.csv`: Reseñas 21 a 30 del dataset de restaurantes en formato JSON.

> Nota: Esta adaptación del proyecto se centra en la ejecución y evaluación del producto final, y no incluye el análisis específico de la importancia individual de las etiquetas seleccionadas.

## Instalación y Configuración

1. **Clonar el repositorio:**

```bash
git clone <repository-url>
cd <repository-name>
```
2. **Instalar dependencias:**

El repositorio utiliza `uv` para facilitar la gestión del entorno y las dependencias.

Si utilizas `uv`:

```bash
uv sync
```

Alternativamente, mediante `pip`:

```bash
pip install -r requirements.txt
```

## Ejecución

Se debe ejecutar el notebook `contextFilter.ipynb`. Una vez inicializado, el sistema funciona de manera interactiva.

El notebook incluye ejemplos de peticiones desde línea de comandos y llamadas desde otras aplicaciones, pero todas las funcionalidades del prototipo pueden probarse directamente mediante la interfaz visual basada en widgets.

## Autor

**Manuel Vázquez Martí**
Graduado en Ciencia de Datos Aplicada (UOC)
Nota final: 9.02 / 10

* Experiencia en sistemas de información sanitarios (CatSalut).
* Enfocado en modelado predictivo y toma de decisiones basada en datos.

## Agradecimientos

Además de las referencias realizadas anteriormente, quisiera destacar:

* A Victor Morant Cantero y Josep Corbasí Morales, profesor y responsable respectivamente de la asignatura **Diseño de Productos de Datos**, por su enfoque orientado al usuario y por transmitir que las herramientas de datos deben diseñarse teniendo en cuenta las necesidades y requisitos de las personas que las utilizan.

Esta asignatura ha sido especialmente relevante para comprender que el desarrollo de un producto de datos no depende únicamente de la tecnología utilizada, sino también de su capacidad para aportar valor real a sus usuarios.

## Licencia

Este proyecto y su fundamentación teórica, basada en el Trabajo Final de Grado original, se distribuyen bajo la licencia [Creative Commons Attribution 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

*Mayo 2026*
