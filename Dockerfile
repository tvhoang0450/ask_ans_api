FROM python:3.6-slim
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTEVODE 1
RUN mkdir /code
WORKDIR /code

RUN pip install --upgrade pip
COPY requirements.txt /code/

RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
