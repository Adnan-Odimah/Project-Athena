# Dockerfile, Image, Container

#SELECT VERSION
FROM python:3.12

ADD src/main/ ./src/main/
ADD requirements.txt ./


RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_md

CMD ["python", "src/main/main.py"]