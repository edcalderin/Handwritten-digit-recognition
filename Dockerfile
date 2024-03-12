# Stage 1: Build
FROM python:3.12-slim as builder

RUN pip install poetry==1.8.2

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.in-project true && poetry install --no-root

# Stage 2: Runtime
FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /app .

ENV PATH="/app/.venv/bin:$PATH"

COPY src ./src
COPY images/digits ./images/digits

EXPOSE 8501

ENTRYPOINT ["python", "-m", "streamlit", "run", "src/app.py"]