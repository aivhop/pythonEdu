import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

indent = 4


def task() -> None:
    with open(INPUT_FILENAME, "rt", encoding='utf-8') as inp:
        csv_dict_reader = csv.DictReader(inp, delimiter=',', quotechar='\n')
        data = [dic for dic in csv_dict_reader]

    with open(OUTPUT_FILENAME, "wt", encoding='utf-8') as output:
        json.dump(data, output, indent=indent)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
