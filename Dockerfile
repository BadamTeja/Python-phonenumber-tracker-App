FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install phonenumbers folium opencage

CMD ["python","tracker.py"]
