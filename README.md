# ContextFilter  

### Minimum Viable Product (MVP) for content filtering

[![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/) [![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow.svg)](https://huggingface.co/docs/transformers) [![PyTorch](https://img.shields.io/badge/PyTorch-red.svg)](https://pytorch.org/)  

Application for analyzing and filtering reviews or textual content using _Transformers zero-shot pipelines_ according to a configurable evaluation threshold.

## Translations

- [Read in Catalan](README_ca.md)
- [Leer en Castellano](README_es.md)

## Overview

This repository contains an MVP application developed within the framework of the **Data Product Design** course at the Open University of Catalonia (UOC).

The prototype, implemented as a Python Jupyter Notebook, uses **Zero-Shot classification** through language models to evaluate the degree of correspondence between a text and a set of candidate semantic labels.

The system works by sending a text request to an API, which evaluates its relationship with the defined labels and calculates a global score based on the results obtained from the model. This value is compared against a configurable threshold to determine whether the content meets the established criteria.

The system is designed to be flexible, allowing users to add or replace semantic labels, modify the evaluation threshold, and process both individual texts and files containing multiple records in different formats.

The objective is to provide stakeholders with a functional prototype that allows them to explore which label configuration and evaluation threshold best fit the criteria an organization needs to assess.

## Main Features

- Support for individual texts in different languages through content normalization.
- Ability to add or replace semantic filters compared to the initial application configuration.
- Zero-Shot classification pipeline based on **Hugging Face Transformers** models.
- Local model execution through **PyTorch**.
- Upload and processing of files containing reviews or text collections in different formats.
- API implemented with **FastAPI** inside the same notebook, controlled through _ipywidgets_.
- Flexible classification criteria configuration through customizable semantic labels.
- Logging and auditing of processed requests.

## Results

The main purpose of this project is to evaluate the behavior of the filtering system and analyze its adaptability through different semantic label configurations.

This phase does not aim to determine the final optimal label combination, but rather to analyze the product behavior and establish a foundation for future optimization.

The model evaluation results can be found in the HTML version of the [_metrics notebook_](metrics.html).

## Real-World Context

The application is designed as a semantic filtering service capable of receiving content from different clients and determining whether it matches the criteria defined by an organization.

One possible use case is review moderation, distinguishing between toxic comments and negative but constructive opinions. A platform containing only positive opinions may lose credibility, while identifying inappropriate content helps maintain a higher-quality participation environment.

The flexibility of the system allows filters to be adapted to different needs through configurable semantic pairs and evaluation thresholds. For example, it could identify restaurant-related content and differentiate between a valid customer review and an unrelated or offensive comment.

## Technology Stack

> Focused on natural language processing through language models and local inference.

- **Programming Language**: Python (>= 3.12)
- **Language Models and Inference**: Hugging Face Transformers, PyTorch
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **Data Visualization**: Matplotlib, Seaborn
- **Service Logging and Auditing**: TinyDB
- **Interactive Interface**: Jupyter Notebook, ipywidgets
- **API and Server Management**: FastAPI, Uvicorn
- **Environment Management**: uv / pip (through pyproject.toml)
- **Language Management**: langdetect, deep-translator
- **Modeling Approach**: Zero-Shot Classification using Transformers

## Datasets

The dataset used to validate the toxicity filter was obtained from the GitHub repository by Prajwal Krishna, developed for the Kaggle *Toxic Comment Classification Challenge*.

The original repository can be found at:

https://github.com/praj2408/Jigsaw-Toxic-Comment-Classification

The corresponding Kaggle competition is available at:

https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge

Many thanks to Prajwal Krishna and Kaggle for making these resources available to the community and contributing to the development of tools related to natural language processing and toxicity detection.

Additionally, a custom dataset containing 200 reviews was created:
- 100 reviews related to restaurants.
- 100 reviews unrelated to this topic.

This dataset was used to evaluate other semantic filters, especially domain-related content detection.

## Repository Structure

The repository contains the main prototype/MVP notebook, a metrics evaluation notebook, auxiliary scripts, and the different data files used during testing.

* `contextFilter.ipynb`: Main prototype notebook. Once executed, it starts an API to evaluate texts and allows interactive testing through a widget-based interface.
* `metrics.ipynb`: Notebook used to evaluate prototype performance through different datasets and configurations.
* `metrics.html`: HTML conversion of the metrics notebook for easier visualization.
* `ipy_multil_mvm.py`: Script containing routines, variables, and labels required by `contextFilter.ipynb`.
* `requirements.txt`: Dependencies required to run the notebooks.
* `pyproject.toml`: File used by `uv` containing the project description and dependencies.
* `data/` folder: Contains the prepared test files:
  * `en_3000.csv`: First 3000 reviews from the toxicity dataset prepared for evaluation.
  * `en_1_10.csv`: Initial selection of 10 reviews from the toxicity dataset.
  * `en_11_20.txt`: Reviews 11 to 20 from the toxicity dataset in TXT format.
  * `en_21_30.json`: Reviews 21 to 30 from the toxicity dataset in JSON format.
  * `rev_restaurants.csv`: Custom dataset containing 200 restaurant-related and unrelated reviews.
  * `rest_1_10.csv`: First 10 reviews from the restaurant dataset.
  * `rest_11_20.csv`: Reviews 11 to 20 from the restaurant dataset in TXT format.
  * `rest_21_30.csv`: Reviews 21 to 30 from the restaurant dataset in JSON format.

> Note: This project adaptation focuses on the execution and evaluation of the final product and does not include the specific analysis of the individual importance of the selected labels.

## Installation and Configuration

1. **Clone the repository:**

```bash
git clone <repository-url>
cd <repository-name>
```

2. **Install dependencies:**

This repository uses `uv` to simplify environment and dependency management.

Using `uv`:

```bash
uv sync
```

Alternatively, using standard `pip`:

```bash
pip install -r requirements.txt
```

## Execution

Run the `contextFilter.ipynb` notebook. Once initialized, the system works interactively.

The notebook includes examples of command-line requests and external application calls, but all prototype features can be tested directly through the widget-based visual interface.

## Author

**Manuel Vázquez Martí**  
BSc in Applied Data Science (UOC)  
Final grade: 9.02 / 10

- Experience in healthcare information systems (CatSalut).
- Focused on predictive modeling and data-driven decision making.

## Acknowledgements

In addition to the previous references, I would like to acknowledge:

- Victor Morant Cantero and Josep Corbasí Morales, professor and coordinator respectively of the **Data Product Design** course, for their user-oriented approach and for emphasizing that data tools should be designed around the needs and requirements of the people who use them.

This course was especially valuable in understanding that developing a data product depends not only on the technology used, but also on its ability to provide real value to its users.

## License

This project and its theoretical foundation, based on the original Final Degree Project, are distributed under the [Creative Commons Attribution 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) license.

_May 2026_