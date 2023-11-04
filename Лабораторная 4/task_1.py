import json

INPUT_FILE = "input.json"


def task() -> float:
    with open(INPUT_FILE, "rt", encoding='utf-8') as inp:
        data = json.load(inp)
    return round(sum([dic["score"] * dic["weight"] for dic in data]), 3)


print(task())
