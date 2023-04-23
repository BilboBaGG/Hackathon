FROM python:latest

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT [ "python3", "-m" ,"app", "--host=0.0.0.0", "--port=5000" ]