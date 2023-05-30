FROM python:3.11-alpine3.18

RUN pip install flask

CMD ["python3", "./main.py"]
