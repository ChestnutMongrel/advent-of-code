from common import read_file, get_data, timer


def test_all() -> None:

    result = len(look_and_say('1', 5))
    correct = 6
    assert correct == result, f'Should be {correct}, got {result} instead.'


@timer
def look_and_say(line: str, repeat: int = 40) -> int:
    for _ in range(repeat):
        new_line = ''
        symbol = ''
        amount = 0
        for i in line:
            if i == symbol:
                amount += 1
            else:

                if amount:
                    new_line += str(amount) + symbol
                symbol = i
                amount = 1
        else:
            if amount:
                new_line += str(amount) + symbol
        line = new_line

    return line


def main() -> None:
    data = tuple(get_data(2015, 10))[0]
    new_line = look_and_say(data)
    print('Part one:', len(new_line))
    print('Part two:', len(look_and_say(new_line, 10)))
    # print('Part two:', result)
    # 195962 is too low


if __name__ == '__main__':
    test_all()
    main()
