"""
--- Day 5: If You Give A Seed A Fertilizer ---
"""
# The worst code ever >_<


def make_rules(data: str) -> list:
    return [[int(i) for i in item.split()] for item in data.split('\n') if item]


def to_numbers(data: str) -> list:
    return [int(i) for i in data.split()]


def seed_opening(start: int, amount: int) -> list:
    for ii in range(amount):
        yield start + ii


def convert(value: int, rules: list) -> int:
    for rule in rules:
        for to_, from_, amount in rule:
            if from_ <= value < from_ + amount:
                value += to_ - from_
                break
    return value


def test_convert() -> None:
    values = '79 14 55 13'
    rules = '''50 98 2
52 50 48'''
    result = '81 14 57 13'
    assert convert(to_numbers(values), make_rules(rules)) == to_numbers(result)

    values = '81 14 57 13'
    rules = '''0 15 37
37 52 2
39 0 15'''
    result = '81 53 57 52'
    assert convert(to_numbers(values), make_rules(rules)) == to_numbers(result)


def open_file(file_name: str) -> tuple:
    with open(file_name, 'r') as file:
        seeds = file.readline().strip().replace('seeds: ', '')
        all_rules = list()
        rules: str = ''

        while True:
            line = file.readline()

            if line and line.find('-to-') == -1:
                rules += line

            elif rules.strip():
                all_rules.append(make_rules(rules))
                rules = ''

            if not line:
                break

    return seeds, all_rules


def gardening(seeds: list, rules: list) -> int:
    min_ = 1_000_000_000_000

    for seed in seeds:
        seed = convert(seed, rules)
        if seed < min_:
            min_ = seed

    return min_


def seeds_to_range(data: str) -> list:
    data = to_numbers(data)
    result = list()
    for i in range(0, len(data), 2):
        result.append((data[i], data[i] + data[i + 1] - 1))
    return result


def sorting(data: list) -> None:
    data.sort(key=lambda x: x[0])


def rearranging(data: list) -> list:
    new_data = list()
    current = data[0]

    for item in data:
        if item[0] <= current[1]:
            current = (current[0], max(item[1], current[1]))
        else:
            new_data.append(current)
            current = item

    new_data.append(current)
    return new_data


def new_rules(data: list) -> list:
    result = list()
    for item in data:
        result.append((item[1], item[1] + item[2] - 1, item[0] - item[1]))
    return result


def operating(seeds: list, rules: list) -> int:
    for rule in rules:
        rule_ind = 0
        rule_len = len(rule)
        rule_start, rule_finish, step = rule[rule_ind]

        seed_ind = 0
        seed_len = len(seeds)
        seed_start, seed_finish = seeds[seed_ind]

        result = list()
        # print(f'{rule = }')
        while True:
            if rule_start >= seed_finish != seed_start:
                until = min(seed_finish, rule_start - 1)
                result.append((seed_start, until))
                seed_start = until + 1
                # print('1', result)

            elif rule_start < seed_start:
                rule_start = seed_start

            else:  # rule_start >= seed_start
                if seed_finish <= rule_finish:
                    result.append((seed_start + step, seed_finish + step))
                    seed_start = seed_finish + 1
                    # print('2', result)
                else:  # seed_finish > rule_finish
                    result.append((seed_start + step, rule_finish + step))
                    rule_start = seed_start = rule_finish + 1
                    # print('3', result)

            if seed_start > seed_finish:
                seed_ind += 1
                if seed_ind == seed_len:
                    break
                seed_start, seed_finish = seeds[seed_ind]
                # print('new seed')
            if rule_start > rule_finish:
                rule_ind += 1
                if rule_ind == rule_len:
                    break
                rule_start, rule_finish, step = rule[rule_ind]
                # print('new_rule')

        if seed_ind < seed_len:
            if seed_start <= seed_finish:
                result.append((seed_start, seed_finish))
                # print('4', result)
            for i in range(seed_ind + 1, seed_len):
                result.append(seeds[i])
                # print('5', result)

        sorting(result)
        seeds = rearranging(result)
        # print(f'{result = }')
        # print(f'{seeds = }')

    return result[0][0]


def main() -> None:
    seeds, rules = open_file('data/05_input.txt')
    # print(f'{seeds = }')
    # print(f'{rules = }')

    print('First part:', gardening(to_numbers(seeds), rules))

    seeds = seeds_to_range(seeds)
    sorting(seeds)
    seeds = rearranging(seeds)

    rules_ = list()
    for item in rules:
        item = new_rules(item)
        sorting(item)
        rules_.append(item)
    rules = rules_

    # print(f'{seeds = }')
    # print(f'{rules = }')

    print(operating(seeds, rules))

    # mins = list()
    # for i in range(0, len(seeds), 2):
    #     result = gardening(seed_opening(seeds[i], seeds[i + 1]), rules)
    #     print(result)
    #     mins.append(result)
    #
    # print(min(mins))

    # seeds, rules = open_file('05_input.txt')
    # print(gardening(to_numbers(seeds), rules))
    # print(gardening('05_input.txt', to_numbers))
    # print(gardening('12_example.txt', seed_opening))


if __name__ == '__main__':
    main()
