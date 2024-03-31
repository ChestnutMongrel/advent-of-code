from common import read_file
from re import match
from math import prod


# px{a<2006:qkq,m>2090:A,rfg}
def read_rule(line: str) -> dict:
    name, conditions = line.replace('{', ' ').replace('}', '').split()
    conditions = conditions.split(',')
    rule = list()
    pattern = r'([xmas])([<>])(\d+):([a-zAR0-9]+)'

    for data in conditions:
        exp = match(pattern, data)
        if exp:
            category, oper, value, decision = exp.groups()
            value = int(value)
            start = 1
            finish = 4000
            if oper == '<':
                finish = value - 1
            else:  # if oper == '>'
                start = value + 1
            rule.append((category, start, finish, decision))
        else:
            rule.append((data,))

    return {name: tuple(rule)}


# {x=787,m=2655,a=1222,s=2876}
def read_parts(data: str) -> dict:
    data = data[1:-1]
    part = dict()
    for item in data.split(','):
        key, value = item.split('=')
        part[key] = int(value)
    return part


def get_rules_and_parts(data: tuple) -> tuple:
    rules = dict()
    parts = list()

    for line in data:
        if line != '':
            # print(f'{line = }')
            rules.update(read_rule(line))
        else:
            break

    for line in data:
        parts.append(read_parts(line))

    return rules, tuple(parts)


def use_rule(rule: tuple, part: dict) -> str:

    for category, start, finish, decision in rule[:-1]:
        if start <= part[category] <= finish:
            return decision
    return rule[-1][0]


def interval_intersection(first: tuple, second: tuple) -> tuple:
    start = max(first[0], second[0])
    end = min(first[1], second[1])
    if end < start:
        return None
    return start, end


def interval_subtraction(first: tuple, second: tuple) -> tuple:
    if (inter := interval_intersection(first, second)) is None:
        return None
    result = list()
    if first[0] != inter[0]:
        result.append((first[0], inter[0] - 1))
    if first[1] != inter[1]:
        result.append((inter[1] + 1, first[1]))
    return tuple(result)


def creat_new_rules(rules: dict) -> None:
    new_rules = dict()

    def rewrite_rule(rule: tuple) -> dict:
        # For begin with the rule looks like this:
        # (('a', 1, 2005, 'qkq'), ('m', 2091, 4000, 'A'), ('R',))

        for data in rule:
            name = data[-1]
            if name not in new_rules and name not in 'AR':
                new_rules[name] = rewrite_rule(rules[name])

        full = dict().fromkeys('xmas', (1, 4000))
        left = dict().fromkeys('xmas', (1, 4000))
        combinations = list()
        # left = dict()
        for data in rule:
            if len(data) == 4:
                part, start, end, name = data
                current = {part: (start, end)}
                inter = interval_intersection(full[part], current[part])
                # print(f'{inter = }')
                full[part] = inter
                # This will not work if there are two intervals
                # print(f'{full = }')
                # print(f'{part = } {left[part] = }')
                # print(f'{current[part] = }')
                int_sub = interval_subtraction(left[part], current[part])
                if int_sub is not None:
                    left[part] = int_sub[0]
                else:
                    name = 'R'
            else:
                name = data[0]

            if name == 'A':
                combinations.append(full.copy())

            elif name != 'R':
                for rule in new_rules[name]:
                    # print(rule)
                    copy_full = full.copy()
                    for key, item in rule.items():
                        # print(f'{key = }')
                        # print(f'{item = }')
                        # print(f'{copy_full[key] = }')
                        new_inter = interval_intersection(item, copy_full[key])
                        copy_full[key] = new_inter
                        # print(f'{copy_full[key] = }')
                    combinations.append(copy_full.copy())

            full = left.copy()

        # print(f'{combinations = }')
        return combinations

    for name, conditions in rules.items():
        if name not in new_rules:
            # print(f'{name = }')
            new_rules[name] = rewrite_rule(conditions)
            # print('new rules')
            # print(*new_rules.items(), sep='\n')

    # print('rules')
    # for item in rules.items():
    #     print(item)
    # print('new rules')
    # for item in new_rules.items():
    #     print(item)

    total = 0
    for data in new_rules['in']:
        result = prod((second - first + 1 for first, second in data.values()))
        total += result
    print(f'{total = }')


def sort_parts(rules: dict, parts: tuple) -> tuple:
    first = 'in'
    accepted = list()

    for part in parts:
        current = first
        while True:
            print(f'{current = }')
            print(rules[current])
            decision = use_rule(rules[current], part)
            print(f'{decision = }')
            if decision == 'A':
                accepted.append(part)
            elif decision != 'R':
                current = decision
                continue
            break

    return tuple(accepted)


def main() -> None:
    for name in ('data/example_19.txt', 'data/19_input.txt',):

        rules, parts = get_rules_and_parts((read_file(name)))
        # print(*rules.items(), sep='\n')
        # print(parts)
        # accepted = sort_parts(rules, parts)
        # print('total', sum(sum(item.values()) for item in accepted))
        creat_new_rules(rules)

        # in{s<1000:R,s<2000:abc,A}
        # abc{x<100:A,m<200:A,R}

        # in{x<200:A,x<100:R,R}


if __name__ == '__main__':
    main()
