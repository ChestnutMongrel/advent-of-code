"""
--- Day 2: Cube Conundrum ---
"""

# Every line in the file contents 'game id', there 'id' is a number from 1
# and information about how many and what colour balls do we pull out of a bag separated by a comma.
# Every line describes several attempts to pull balls separated by a semicolon. Like this:
#    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red


from math import prod
from common import read_file


# data is actually a generator
def get_data(data: list) -> tuple:
    all_games = list()

    for line in data:
        _, attempts = line.split(': ')
        game = list()
        for chunk in attempts.split(';'):
            attempt = dict().fromkeys(('red', 'green', 'blue'), 0)
            for num_colour in chunk.split(','):
                number, colour = num_colour.split()
                attempt[colour] = int(number)
            game.append(attempt)
        all_games.append(tuple(game))

    return tuple(all_games)


def required_minimum(values: tuple) -> dict:
    required = dict().fromkeys(('red', 'green', 'blue'), 0)

    for item in values:
        for colour, number in item.items():
            if number > required[colour]:
                required[colour] = number

    return required


def total_minimum_multiply(data: tuple) -> int:
    total_multiply = 0

    for attempts in data:
        minimum = required_minimum(attempts)
        total_multiply += prod(minimum.values())

    return total_multiply


def possible_games_id_sum(data: tuple) -> int:
    content = {'red': 12, 'green': 13, 'blue': 14}
    sum_ids = 0

    for game_id, attempts in enumerate(data, 1):
        minimum = required_minimum(attempts)

        for colour in minimum:
            if content[colour] < minimum[colour]:
                break
        else:
            sum_ids += game_id

    return sum_ids


def main() -> None:
    example = 'data/02_example.txt'
    data_example = get_data(read_file(example))

    print('\tFor the example:')
    print('The sum of IDs of possible games:', possible_games_id_sum(data_example))
    print('The sum of the multiply of minimum set of cubes:', total_minimum_multiply(data_example))
    print()

    puzzle_input = 'data/02_input.txt'
    data_input = get_data(read_file(puzzle_input))

    print('\tFor the actual puzzle input:')
    print('The sum of IDs of possible games:', possible_games_id_sum(data_input))
    print('The sum of the multiply of minimum set of cubes:', total_minimum_multiply(data_input))
    print()


if __name__ == '__main__':
    main()
