#!/usr/bin/env python3
import os

import json
path_conf = input("enter path for config file")
path_data = input("enter path for data file")
if not os.path.isfile(path_conf):
    print(f"Error: Config file '{path_conf}' not found.")
    exit()

if not os.path.isfile(path_data):
    print(f"Error: Data file '{path_data}' not found.")
    exit()
with open(path_conf, "r") as file:
    content_conf = json.load(file)

with open(path_data, "r") as file:
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

