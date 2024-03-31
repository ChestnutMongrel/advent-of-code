"""
--- Day 8: Haunted Wasteland ---
The second part only works, because it's all quite precise.
I don't like it this way...
"""

from re import match
from math import lcm
from itertools import cycle


def read_file(file_name: str) -> tuple:
    with open(file_name, 'r') as file:
        instructions = file.readline().strip()

        nodes = dict()
        pattern = r'(\w{3}) = \((\w{3}), (\w{3})\)'
        while line := file.readline():
            if data := match(pattern, line):
                key, *rest = data.groups()
                nodes[key] = tuple(rest)

    return instructions, nodes


def how_many_steps(instructions: str, nodes: dict) -> int:
    if 'AAA' not in nodes:
        return -1

    start = 'AAA'
    finish = 'ZZZ'
    steps = 0
    side = {'L': 0, 'R': 1}

    while True:
        for instr in instructions:
            turn = side[instr]
            start = nodes[start][turn]
            steps += 1
            if start == finish:
                return steps


def go_many_ways(instructions: str, nodes: dict) -> int:
    start = filter(lambda x: x[-1] == 'A', nodes.keys())
    result = 1

    for current in start:
        step = 0
        instructions = cycle(instructions)
        for instr in instructions:
            turn = instr == 'R'
            current = nodes[current][turn]
            step += 1

            if current[-1] == 'Z':
                break

        result = lcm(step, result)

    return result


def main() -> None:
    ex_1 = '12_example.txt'
    task = '08_input.txt'

    print('For part one:', how_many_steps(*read_file(task)))
    print('For part two:', go_many_ways(*read_file(task)))


if __name__ == '__main__':
    main()
