import random
import csv
from datetime import datetime, timedelta

RECORDS = 250
OUTPUT = "history.csv"

start_time = datetime.now() - timedelta(minutes = RECORDS)
with open(OUTPUT, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "temperature",
        "pressure",
        "vibration",
        "rpm",
        "current",
        "state"
    ])
    for i in range(RECORDS):
        temperature = round(random.uniform(35.0, 95.0), 2)
        pressure = round(random.uniform(1.0, 10.0), 2)
        vibration = round(random.uniform(0.1, 10.0), 2)
        rpm = random.randint(500, 5000)
        current = round(random.uniform(1.0, 25.0), 2)
        if (
            temperature > 80
            or pressure > 8
            or vibration > 7
            or current > 20
        ):
            state = "FAULT"
        elif (
            temperature > 70
            or pressure > 6
            or vibration > 5
            or current > 15
        ):
            state = "WARNING"
        else:
            state = "NORMAL"
        
        writer.writerow([
            temperature,
            pressure,
            vibration,
            rpm,
            current,
            state
        ])

print(f"Successfully generated {RECORDS} history records!")
print(f"History file saved as: {OUTPUT}")