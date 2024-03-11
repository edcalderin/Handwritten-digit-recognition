# Handwritten Digit recognition with Cosine Similarity

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

![Alt text](./images/cover.jpg)
<p align="center">
  <i>Image credits: <a href='https://aigeekprogrammer.com/keras-python-mnist-handwritten-digit-recognition/'>AI Geek Programmer article</a></i>
</p>

## Table of Contents

* [Problem statement](#problem-statement)
* [Directory layout](#directory-layout)
* [Setup](#setup)
* [Running the app with Docker (Recommended)](#running-the-app-with-docker-recommended)
* [Running the app manually](#running-the-app-manually)
* [Checkpoints](#checkpoints)
* [References](#references)

## Problem statement

Brief problem statement

## Directory layout

```
.
├── images
│   └── digits
├── src
│   └── array_digits
└── tests

5 directories
```

## Running the app with Docker (Recommended)

1. Run `docker build -t digit-recognition .` 
2. `docker run -it --rm -p 8501:8501 digit-recognition`

Go to `http://localhost:8501`

The output should look like this:

![Alt text](./images/app.png)

## Running the app manually

A virtual environment will be needed to run the app manually, run the following commands from root project directory:

1. `pip install poetry`
2. `poetry shell`
3. `poetry install`
7. `streamlit run src/app.py`
8. Go to `http://localhost:8501`

## Checkpoints

- [x] Problem description
- [x] Reproducibility
- [x] Dependency and enviroment management
- [x] Containerization (Docker with multi-stage)
- [x] Linter
- [x] CI/CD workflow (Linter and Unit tests)
- [x] Unit tests
- [ ] Cloud deployment

## References

* https://en.wikipedia.org/wiki/Cosine_similarity