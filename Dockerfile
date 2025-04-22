FROM python:3.13.3-bookworm

WORKDIR /server

RUN pip install --upgrade pip wheel "poetry==1.8.3"

RUN poetry config virtualenvs.create false

COPY server/pyproject.toml server/poetry.lock ./

RUN poetry install

COPY /server .

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]