# ContextFilter

### Minimum Viable Product (MVP) per al filtratge de contingut

[![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/) [![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow.svg)](https://huggingface.co/docs/transformers) [![PyTorch](https://img.shields.io/badge/PyTorch-red.svg)](https://pytorch.org/)

Aplicació per analitzar i filtrar ressenyes o contingut textual mitjançant *pipelines zero-shot* de Transformers segons un llindar d'avaluació configurable.

## Traduccions

* [Read in English](README.md)
* [Leer en Castellano](README_es.md)

## Visió General

Aquest repositori conté una aplicació MVP desenvolupada en el marc de l'assignatura de la Universitat Oberta de Catalunya (UOC) **Disseny de Productes de Dades**.

El prototip, implementat en un notebook Jupyter de Python, utilitza classificació **Zero-Shot** mitjançant models de llenguatge per avaluar el grau de correspondència d'un text amb un conjunt d'etiquetes semàntiques candidates.

El funcionament consisteix en enviar un text a una API, que avalua la seva relació amb les etiquetes definides i calcula un score global a partir dels resultats obtinguts pel model. Aquest valor es compara amb un llindar configurable per determinar si el contingut compleix o no els criteris establerts.

El sistema està dissenyat per ser flexible, permetent afegir o substituir etiquetes semàntiques, modificar el llindar d'avaluació i processar tant textos individuals com fitxers amb múltiples registres en diferents formats.

L'objectiu és proporcionar als *stakeholders* un prototip funcional que permeti explorar quina configuració d'etiquetes i quin llindar d'avaluació s'adapten millor als criteris que una organització necessita valorar.

## Característiques Principals

* Suport per a textos individuals en diferents idiomes mitjançant normalització del contingut.
* Possibilitat d'afegir o substituir filtres semàntics respecte als definits inicialment en l'aplicació.
* Pipeline classificador Zero-Shot basat en models de **Hugging Face Transformers**.
* Execució local dels models mitjançant **PyTorch**.
* Enviament i processament de fitxers amb paquets de ressenyes o textos en diferents formats.
* API implementada amb **FastAPI** dins del mateix notebook, controlada mitjançant *ipywidgets*.
* Configuració flexible dels criteris de classificació mitjançant etiquetes semàntiques personalitzables.
* Registre i auditoria de les peticions processades.

## Resultats

La finalitat principal del projecte és avaluar el comportament del sistema de filtratge i estudiar la capacitat d'adaptació mitjançant diferents configuracions d'etiquetes semàntiques.

Aquesta fase no té com a objectiu determinar la combinació definitiva d'etiquetes, sinó analitzar el funcionament del producte i establir una base per a futures optimitzacions.

Els resultats de les avaluacions del model es poden consultar a la versió HTML del [*notebook de mètriques*](metrics.html).

## Context del Món Real

L'aplicació està plantejada com un servei de filtratge semàntic capaç de rebre contingut des de diferents clients i determinar si aquest s'ajusta als criteris definits per una organització.

Un possible cas d'ús és la moderació de ressenyes, diferenciant entre comentaris tòxics i opinions negatives però constructives. Una plataforma amb únicament opinions positives pot perdre credibilitat, mentre que la identificació de contingut inadequat permet mantenir un entorn de participació de qualitat.

La flexibilitat del sistema permet adaptar els filtres a diferents necessitats mitjançant la configuració de parelles semàntiques i llindars d'avaluació. Per exemple, es podria seleccionar contingut relacionat amb restauració i diferenciar entre una crítica vàlida i un comentari no relacionat o ofensiu.

## Stack Tecnològic

> Centrat en el processament del llenguatge natural mitjançant models de llenguatge i inferència local.

* **Llenguatge de Programació**: Python (>= 3.12)
* **Models de Llenguatge i Inferència**: Hugging Face Transformers, PyTorch
* **Processament de Dades**: Pandas, NumPy
* **Machine Learning**: Scikit-learn
* **Visualització de Dades**: Matplotlib, Seaborn
* **Auditoria i registre de servei**: TinyDB
* **Interfície Interactiva**: Jupyter Notebook, ipywidgets
* **Gestió d'API i servidor**: FastAPI, Uvicorn
* **Gestió de l'entorn**: uv / pip (mitjançant pyproject.toml)
* **Gestió d'idiomes**: langdetect, deep-translator
* **Enfocament de Modelatge**: Classificació Zero-Shot mitjançant Transformers

## Conjunts de Dades

El conjunt de dades utilitzat per validar el filtre de toxicitat s'ha obtingut del repositori de GitHub de Prajwal Krishna, desenvolupat per al repte *Toxic Comment Classification Challenge* de Kaggle.

El repositori original es pot consultar a:

https://github.com/praj2408/Jigsaw-Toxic-Comment-Classification

La competició corresponent de Kaggle està disponible a:

https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge

Moltes gràcies a Prajwal Krishna i a Kaggle per posar aquests recursos a disposició de la comunitat i contribuir al desenvolupament d'eines relacionades amb el processament del llenguatge natural i la detecció de toxicitat.

A més, s'ha generat un conjunt propi de 200 ressenyes:

* 100 ressenyes relacionades amb restaurants.
* 100 ressenyes no relacionades amb aquesta temàtica.

Aquest conjunt s'ha utilitzat per avaluar altres filtres semàntics, especialment la detecció de relació amb un domini concret.

## Estructura del Repositori

El repositori comprèn el notebook principal del prototip/MVP, un notebook d'avaluació de mètriques, els scripts auxiliars i els diferents fitxers de dades utilitzats en les proves.

* `contextFilter.ipynb`: Notebook principal del prototip. Un cop executat, activa una API per avaluar textos i permet realitzar proves mitjançant una interfície interactiva amb widgets.
* `metrics.ipynb`: Notebook on s'avalua el funcionament del prototip mitjançant diferents conjunts de dades i configuracions.
* `metrics.html`: Conversió del notebook de mètriques a format HTML per facilitar-ne la visualització.
* `ipy_multil_mvm.py`: Script amb rutines, variables i etiquetes necessàries pel notebook `contextFilter.ipynb`.
* `requirements.txt`: Dependències necessàries per executar els notebooks.
* `pyproject.toml`: Fitxer utilitzat per `uv` amb la descripció i dependències del projecte.
* Carpeta `data/`: Conté els fitxers de prova preparats:

  * `en_3000.csv`: Primeres 3000 ressenyes del dataset de toxicitat preparades per a l'avaluació.
  * `en_1_10.csv`: Selecció inicial de 10 ressenyes del dataset tòxic.
  * `en_11_20.txt`: Ressenyes 11 a 20 del dataset tòxic en format TXT.
  * `en_21_30.json`: Ressenyes 21 a 30 del dataset tòxic en format JSON.
  * `rev_restaurants.csv`: Dataset propi amb 200 ressenyes relacionades i no relacionades amb restaurants.
  * `rest_1_10.csv`: Primeres 10 ressenyes del dataset de restaurants.
  * `rest_11_20.csv`: Ressenyes 11 a 20 del dataset de restaurants en format TXT.
  * `rest_21_30.csv`: Ressenyes 21 a 30 del dataset de restaurants en format JSON.

> Nota: Aquesta adaptació del projecte se centra en l'execució i l'avaluació del producte final, i no inclou l'anàlisi específica de la importància individual de les etiquetes seleccionades.

## Instal·lació i Configuració

1. **Clonar el repositori:**

```bash
git clone <repository-url>
cd <repository-name>
```

2. **Instal·lar dependències:**

El repositori utilitza `uv` per facilitar la gestió de l'entorn i les dependències.

Si fas servir `uv`:

```bash
uv sync
```

Alternativament, mitjançant `pip`:

```bash
pip install -r requirements.txt
```

## Execució

S'ha d'executar el notebook `contextFilter.ipynb`. Un cop inicialitzat, el sistema funciona de manera interactiva.

El notebook inclou exemples de crides des de línia de comandaments i des d'altres aplicacions, però totes les funcionalitats del prototip es poden provar directament mitjançant la interfície visual basada en widgets.

## Autor

**Manuel Vázquez Martí**
Graduat en Ciència de Dades Aplicada (UOC)
Nota final: 9.02 / 10

* Experiència en sistemes sanitaris (CatSalut).
* Enfocat en modelatge predictiu i presa de decisions basada en dades.

## Agraïments

A més de les mencions realitzades anteriorment, vull destacar:

* A Victor Morant Cantero i Josep Corbasí Morales, professor i responsable respectivament de l'assignatura **Disseny de Productes de Dades**, pel seu enfocament orientat a entendre que les eines de dades han de respondre a les necessitats dels seus usuaris i stakeholders.

Aquesta assignatura ha estat especialment rellevant per entendre que el desenvolupament d'un producte de dades no depèn únicament de la tecnologia utilitzada, sinó també de la seva capacitat per aportar valor real a les persones que l'utilitzen.

## Llicència

Aquest projecte i la seva fonamentació teòrica, basada en el Treball Final de Grau original, es distribueixen sota la llicència [Creative Commons Attribution 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

*Maig 2026*
