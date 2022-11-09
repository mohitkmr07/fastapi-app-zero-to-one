# Pull base image
FROM python:3.9.2-slim-buster
WORKDIR /fast-app-zero-to-one/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install pipenv
RUN apt update
COPY Pipfile Pipfile.lock /fast-app-zero-to-one/
RUN pipenv install --system --deploy
RUN pipenv --clear
COPY app /fast-app-zero-to-one/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]