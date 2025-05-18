#!/usr/bin/env python3

import json

with open("config.json", "r") as file:
    content_conf = json.load(file)

with open("data.json", "r") as file:
    content_data = json.load(file)

def check_data(content_conf, content_data):
    for key, conf in content_conf.items():
        if key not in content_data:
            print(f"Missing key: {key}")
            continue

        value = content_data[key]
        min_val = conf.get("min")
        max_val = conf.get("max")

        if value < min_val or value > max_val:
            print(f"The value {value} in '{key}' is incorrect.")
        else:
            print(f"The value {value} in '{key}' is correct. Good for you!")

