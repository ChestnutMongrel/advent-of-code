from common import read_file, get_data
import re


def test_all() -> None:
    data = tuple(read_file('data/10_example.txt'))
    assert parse_data(data) == parse_again(data)


# I thought the function would be shorter if I use regexes...
def parse_again(data: tuple) -> tuple:
    bots = dict()
    values = dict()
    value_pattern = re.compile(r'value (\d+) goes to bot (\d+)')
    bot_pattern = re.compile(r'bot \d* gives low to ([a-z]*) \d* and high to ([a-z]*) \d*')

    for line in data:  # type: str
        if match := value_pattern.search(line):
            value, bot = map(int, match.groups())
            values.setdefault(bot, set()).add(value)
        else:
            bot, low_num, high_num = map(int, re.findall(r'\d+', line))
            low, high = bot_pattern.search(line).groups()
            low_num -= 100 if low == 'output' else 0
            high_num -= 100 if high == 'output' else 0
            bots.setdefault(bot, set()).add((0, low_num))
            bots[bot].add((1, high_num))

    return bots, values


def parse_data(data: tuple) -> tuple:
    bots = dict()
    values = dict()

    for line in data:  # type: str
        if line.startswith('value'):
            value, bot = map(int, re.findall(r'\d+', line))
            if 'bot' not in line:
                print('WARNING')  # !!!!!!!!!!!!!!!!
            values.setdefault(bot, set()).add(value)

        if line.startswith('bot'):
            bot, num_1, num_2 = map(int, re.findall(r'\d+', line))
            low_to = re.search(f'(?<=low to )[a-z]+', line).group()
            high_to = re.search(f'(?<=high to )[a-z]+', line).group()
            if low_to == 'output':
                num_1 -= 100
            if high_to == 'output':
                num_2 -= 100
            bots.setdefault(bot, set()).add((0, num_1))
            bots[bot].add((1, num_2))

    return bots, values


def find_key_with_pair(data: dict) -> int | None:
    for key, value in data.items():
        if len(value) == 2:
            return key

    return None


def part_one(actions: dict, values: dict) -> tuple:
    compare = {17, 61}
    the_bot = None

    while (bot := find_key_with_pair(values)) is not None:
        pair = values[bot]
        values.pop(bot)

        if pair == compare:
            the_bot = bot

        low, high = sorted(pair)
        for what, whom in actions[bot]:
            if what == 0:
                values.setdefault(whom, set()).add(low)
            if what == 1:
                values.setdefault(whom, set()).add(high)

    multiply_outputs = values[-100].pop() * values[-99].pop() * values[-98].pop()
    return the_bot, multiply_outputs


def main() -> None:
    data = get_data(2016, 10)
    bots, values = parse_data(data)
    result_one, result_two = part_one(bots, values)
    print('Part one:', result_one)
    print('Part two:', result_two)


if __name__ == '__main__':
    test_all()
    main()
