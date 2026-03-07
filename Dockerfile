FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5060

CMD ["python","app.py"]
