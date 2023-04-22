FROM python:latest

COPY . /project

WORKDIR /project  

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]