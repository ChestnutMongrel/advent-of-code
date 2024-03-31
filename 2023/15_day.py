def read_file(file_name: str):
    with open(file_name, 'r') as file:
        while line := file.readline():
            yield line.strip()


def hash_algorithm(data: str) -> int:
    current = 0
    for i in data:
        current += ord(i)
        current *= 17
        current %= 256
    return current


def hash_map(data: list) -> dict:
    boxes = dict()
    for item in data:
        oper = '-' if '-' in item else '='
        label, power = item.split(oper)
        number = hash_algorithm(label)
        if oper == '-':
            if number in boxes:
                boxes[number].pop(label, None)
        else:
            if number in boxes:
                boxes[number][label] = power
            else:
                boxes[number] = {label: power}
    return boxes


def total_focusing_power(boxes: dict) -> int:
    total = 0
    for number, data in boxes.items():
        for i, key in enumerate(data, 1):
            total += (number + 1) * i * int(data[key])
    return total


def main() -> None:
    for name in ('data/12_example.txt', 'data/15_input.txt'):
        data = read_file(name)
        for line in data:
            print('HASH algorithm sum:', sum(hash_algorithm(data) for data in line.split(',')))
            boxes = hash_map(line.split(','))
            print('total focusing power', total_focusing_power(boxes))


if __name__ == '__main__':
    main()
