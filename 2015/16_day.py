from common import read_file, get_data


def part_one(aunts: str, data: dict) -> None:
    for line in aunts:
        sue, information = line.split(': ', 1)
        for pair in information.split(', '):
            key, value = pair.split(': ')
            if data[key] != value:
                break
        else:
            return sue.split()[-1]


def part_two(aunts: str, data: dict) -> None:
    for line in aunts:
        sue, information = line.split(': ', 1)
        for pair in information.split(', '):
            key, value = pair.split(': ')
            if key in ('cats', 'trees'):
                if int(value) <= int(data[key]):
                    break
            elif key in ('pomeranians', 'goldfish'):
                if int(value) >= int(data[key]):
                    break
            elif data[key] != value:
                break
        else:
            return sue.split()[-1]


def analyse(data: tuple) -> dict:
    result = dict()
    for item in data:
        key, value = item.split(': ')
        result[key] = value
    return result


def main() -> None:
    from_analysis_machine = analyse(read_file('data/16_detected_data.txt'))
    print('Part one:', part_one(get_data(2015, 16), from_analysis_machine))
    print('Part two:', part_two(get_data(2015, 16), from_analysis_machine))


if __name__ == '__main__':
    main()
