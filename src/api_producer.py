import requests
import json
import time
from kafka import KafkaProducer

API_URL = "https://api.openaq.org/v2/latest?limit=1&page=1"

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def fetch_air_quality():
    response = requests.get(API_URL)
    return response.json()

while True:
    try:
        data = fetch_air_quality()
        producer.send("air-quality-stream", data)
        print("Published data:", data)
    except Exception as e:
        print("Error:", e)
    time.sleep(300)  # every 5 mins
