"""
--- Day 6: Wait For It ---
"""
from math import prod


def to_numbers(data: str) -> list:
    return [int(i) for i in data.split()]


def get_data(file_name: str):
    with open(file_name, 'r') as file:
        time = file.readline().replace('Time:', '').strip()
        distance = file.readline().replace('Distance:', '').strip()
        return zip(to_numbers(time), to_numbers(distance))


def get_data_without_space(file_name: str) -> tuple:
    with open(file_name, 'r') as file:
        time = file.readline().replace('Time:', '').replace(' ', '')
        distance = file.readline().replace('Distance:', '').replace(' ', '')
        return int(time), int(distance)


def count_win_amount(time: int, distance: int) -> int:
    num = int((time - (time ** 2 - 4 * distance) ** 0.5) / 2) + 1
    return time - 2 * num + 1


def main() -> None:
    file_name = 'data/06_input.txt'

    results = list()
    for time, distance in get_data(file_name):
        num = count_win_amount(time, distance)
        results.append(num)

    print('Few races:', prod(results))

    num = count_win_amount(*get_data_without_space(file_name))
    print('One race:', num)


if __name__ == '__main__':
    main()
