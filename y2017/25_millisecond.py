from common import read_file, get_data
from collections import defaultdict, namedtuple
import re

YEAR = 2017
DAY = 25
Actions = namedtuple('Actions', ['value', 'shift', 'next'])


def test_all() -> None:
    data = read_file('data/25_example.txt')
    result = part_one(*parse_data(data))
    correct = 3
    assert correct == result, f'Should be {correct}, got {result} instead.'


def parse_data(data) -> tuple:
    # The data looks like this:
    # Begin in state A.
    # Perform a diagnostic checksum after 6 steps.
    #
    # In state A:
    #   If the current value is 0:
    #     - Write the value 1.
    #     - Move one slot to the right.
    #     - Continue with state B.
    #   If the current value is 1:
    #     - Write the value 0.
    #     - Move one slot to the left.
    #     - Continue with state B.

    one_letter = '([A-Z])'
    begin_pattern = re.compile(rf'Begin in state {one_letter}\.')
    steps_pattern = re.compile(r'Perform a diagnostic checksum after (\d+) steps\.')
    state_pattern = re.compile(rf'In state {one_letter}:')
    current_value_pattern = re.compile(r'If the current value is (0|1):')
    write_pattern = re.compile(r'- Write the value (0|1)\.')
    move_pattern = re.compile(r'- Move one slot to the (left|right)\.')
    continue_pattern = re.compile(rf'- Continue with state {one_letter}\.')

    begin = begin_pattern.match(next(data)).groups()[0]
    steps = int(steps_pattern.match(next(data)).groups()[0])

    instructions = dict()
    for line in data:
        if not line:
            continue
        state = state_pattern.search(line).groups()[0]
        instructions[state] = dict()
        for _ in range(2):
            current_value = int(current_value_pattern.search(next(data)).groups()[0])
            to_write = int(write_pattern.search(next(data)).groups()[0])
            direction = move_pattern.search(next(data)).groups()[0]
            shift = 1 if direction == 'right' else -1
            next_state = continue_pattern.search(next(data)).groups()[0]
            instructions[state][current_value] = Actions(to_write, shift, next_state)

    return begin, steps, instructions


# part_one took 3.641115352045745 secs
def part_one(state: str, steps: int, instructions: dict[str, dict]) -> int:
    checksum = defaultdict(int)
    index = 0

    for _ in range(steps):
        value = checksum[index]
        actions: Actions = instructions[state][value]
        checksum[index] = actions.value
        index += actions.shift
        state = actions.next

    return sum(checksum.values())


def main() -> None:
    data = (get_data(year=YEAR, day=DAY))
    print('Part one:', part_one(*parse_data(data)))


if __name__ == '__main__':
    test_all()
    main()
