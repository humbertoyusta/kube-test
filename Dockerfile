FROM python:3.11-alpine3.18

RUN pip install flask

COPY main.py /main.py

CMD ["python3", "./main"]
