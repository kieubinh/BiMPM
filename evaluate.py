import json
import io
import sys


def evaluation(out_file=None):
    if out_file is None:
        print("no file json output!")
        return 0.0
    total = 0
    correct = 0
    try:
        json_data = json.load(io.open(out_file, 'r', encoding='utf-8'))
        for key in json_data:
            json_instance = json_data[key]
            total += 1
            truth = int(json_instance["truth"])
            predict = int(json_instance["prediction"][2])
            if truth == predict:
                correct += 1

    except Exception as e:
        print('Error reading JSON document:', out_file, file=sys.stderr)
        print(e, file=sys.stderr)
        return None
    print(correct, total)
    return correct * 100.0 / total


def main():
    print(evaluation(out_file="result.json"))


if __name__ == '__main__':
    main()
