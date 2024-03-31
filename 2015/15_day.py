from common import read_file, get_data
import numpy as np
from itertools import product


def test_all() -> None:
    ingredients = get_ingredients(read_file('data/15_example.txt'))

    check = (
        (part_one(ingredients), 62842880),
        (part_one(ingredients, 500), 57600000)
    )
    for result, correct in check:
        assert correct == result, f'Should be {correct}, got {result} instead.'


def part_one(data: dict, calories_goal: int = 0) -> int:
    size = 4
    array = np.array([item[:size] for item in data.values()])
    calories_per_ingredient = np.array([item[-1] for item in data.values()])
    array_t = np.transpose(array)
    total_score = 0

    for unknowns in product(range(0, 101), repeat=array.shape[0] - 1):
        z = 100 - sum(unknowns)
        if z <= 0:
            continue
        unknowns = unknowns + (z,)
        multiplied = np.matmul(array_t, unknowns)
        for num in multiplied:
            if num <= 0:
                break
        else:
            result = multiplied.prod()
            if calories_goal:
                current_calories = sum(calories_per_ingredient * unknowns)
                if current_calories == calories_goal and result > total_score:
                    total_score = result
            elif result > total_score:
                total_score = result

    return total_score


def get_ingredients(data: tuple) -> dict:
    # The line looks like this:
    # Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

    ingredients = dict()
    for line in data:
        name, properties = line.split(': ')
        only_numbers = tuple(int(item.split()[1]) for item in properties.split(', '))
        ingredients[name] = only_numbers

    return ingredients


def main() -> None:
    data = get_data(2015, 15)
    ingredients = get_ingredients(data)

    print('Part one:', part_one(ingredients))
    print('Part two:', part_one(ingredients, 500))


if __name__ == '__main__':
    test_all()
    main()
