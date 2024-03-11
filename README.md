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

In this project, I introduce a different and naive approach to the popular problem of handwritten digit recognition, which is widely used in Machine Learning and Convolutional Neural Network by enthusiasts who start in this area. Maybe it is unnecesary to describe the idea behind as you have probably read, seen or implemented this kind of problems on your own, but in this opportunity I decided go through an algebraic solution to identify digits written by hand employing the cosine similarity metric [(See on references)](#references). 

The metric is calculated by measuring the similarity between two vectors and corresponds to the following formula:

$$ cos(\theta) = {\sum_{i=0}^{n} A_iB_i \over  {\sqrt{\sum_{i=0}^{n}A_i^2}}\sqrt{\sum_{i=0}^{n}B_i^2}} $$

Where *A* and *B* represents bi-dimensional arrays; the digit drawn by the user and the original digit intended to be the expected figure, these can be placed interchangeably in the formula.

I have designed a minimal yet functional Streamlit application to expose this algorithm: The user pick a number from a select box and draw the number selected afterwards. The output will after press the `Compare` button. I also created three categories depending on the score: **Excellent** (`score > .7`), **Good** (`score > .4`) and **Incorrect** (`score < .4`) 

![Alt text](./images/code_gif.gif)

The applications of the cosine similarity go beyond of a simple array comparition, it is mostly used in Large Languaje Models, Recommender Systems, Information Retrieval and so on, so you can still leverage its potential to develop a great variety of projects.

## Directory layout

```
.
├── images              # Assets for the project
│   └── digits          # Images of digits from 0 to 9
├── src                 # Directory with source python files
│   └── array_digits    # Directory with files representing arrays of digits (zero.py to nine.py)
└── tests               # Directory contianint test files

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