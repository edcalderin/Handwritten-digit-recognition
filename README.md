# Handwritten Digit Recognition with Cosine Similarity

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

![Cover image](./images/cover.jpg)
*<p align="center">Image credits: <a href='https://aigeekprogrammer.com/keras-python-mnist-handwritten-digit-recognition/'>AI Geek Programmer article</a></p>*

## Table of Contents

* [Problem statement](#problem-statement)
* [Directory layout](#directory-layout)
* [Running the app with Docker (Recommended)](#running-the-app-with-docker-recommended)
* [Running the app manually](#running-the-app-manually)
* [Checkpoints](#checkpoints)
* [References](#references)

## Problem statement

Brief problem statement

### Cosine similarity

Text about this topic

## Directory layout

```
.
├── images              # Assets for the project
│   └── digits          # Images of digits from 0 to 9
├── src                 # Source python files
│   └── array_digits    # Directory with files representing arrays of digits (zero.py to nine.py)
└── tests               # Test files

5 directories
```

## Running the app with Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/edcalderin/Handwritten-digit-recognition.git
```
2. Build and run the docker image:
```bash
docker build -t digit-recognition .
docker run -it --rm -p 8501:8501 digit-recognition
```

3. Go to `http://localhost:8501`

The output should look like this:

![Alt text](./images/app.png)

## Running the app manually

> :warning: You will need **Python 3.12** installed on your system in order to reproduce this app manually.

Run the following commands from root project directory:

1. Clone the repository:
```bash
git clone https://github.com/edcalderin/Handwritten-digit-recognition.git
```
2. Install Poetry (Skip this if you already installed it)
```bash
pip install poetry
```
3. Create and activate environment:
```bash
poetry shell
```
4. Install dependencies:
```bash
poetry install
```
5. Run the streamlit command:
```bash
streamlit run src/app.py
```
6. Go to `http://localhost:8501`

## Checkpoints

- [x] Problem description
- [x] Reproducibility
- [x] Dependency and enviroment management
- [x] Containerization (Docker with multi-stage)
- [x] Linter
- [x] Unit tests
- [x] CI/CD workflow (Linter and Unit tests)
- [ ] Cloud deployment

## References

* https://en.wikipedia.org/wiki/Cosine_similarity