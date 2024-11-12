# TODO решите задачу
import json
def task():
    with open('input.json', 'r') as f:
        data = json.load(f)
    total_sum = 0
    for item in data:
        total_sum += item["score"] * item["weight"]
    return round(total_sum, 3)
result = task()
print(result)






























