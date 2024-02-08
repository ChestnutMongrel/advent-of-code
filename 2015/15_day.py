from common import read_file, get_data
from math import ceil
from copy import deepcopy


def test_all() -> None:
    data = get_ingredients(read_file('data/15_example.txt'))
    print(data)
    matrix = create_matrix(data.values())
    print(*matrix, sep='\n')
    result = solve_linear_system(matrix)
    correct = 62842880
    # for data, correct in check:
    #     result = part_one(data)
    assert correct == result, f'Should be {correct}, got {result} instead.'
    print()


def part_one(data: dict) -> None:
    pass


def solve_linear_system(matrix: list) -> int:
    copy_matrix = deepcopy(matrix)
    variables = [[1, 100] for _ in range(len(copy_matrix[0]) - 1)]
    len_variables = len(variables)

    for i in range(len_variables - 1):
        for line_ind in range(i + 1, len(copy_matrix)):
            coef = copy_matrix[line_ind][i] / copy_matrix[i][i]
            for num_ind in range(i, len(copy_matrix[0])):
                copy_matrix[line_ind][num_ind] -= copy_matrix[i][num_ind] * coef
        print(f'{i = } matrix')
        print(*copy_matrix, sep='\n')

    for i in range(len_variables - 1, -1, -1):
        for line_ind in range(i - 1, -1, -1):
            coef = copy_matrix[line_ind][i] / copy_matrix[i][i]
            for num_ind in range(i, len(copy_matrix[0])):
                copy_matrix[line_ind][num_ind] -= copy_matrix[i][num_ind] * coef

    print(*copy_matrix, sep='\n')

    for i in range(len_variables):
        is_less_than = copy_matrix[i][i] < 0
        var = ceil(copy_matrix[i][-1] / copy_matrix[i][i])
        if is_less_than:
            variables[i][1] = min(var, variables[i][1])
        else:
            variables[i][0] = max(var, variables[i][0])

    for i in range(len_variables, len(copy_matrix)):
        is_less_than = copy_matrix[i][-2] < 0
        var = ceil(copy_matrix[i][-1] / copy_matrix[i][-2])
        if is_less_than:
            variables[-1][1] = min(var, variables[-1][1])
        else:
            variables[-1][0] = max(var, variables[-1][0])

    print(*variables, sep='\n')

    result = 0

    print(*matrix, sep='\n')

    for unknowns in zip(*map(lambda x: (i for i in range(x[0], x[1] + 1)), variables[1:])):
        print(f'{unknowns = }')
        z = 100 - sum(unknowns)
        if z >= 0:
            current = 1
            for line in matrix[1:]:
                summa = line[0] * z
                for i, num in enumerate(unknowns):
                    summa += line[i + 1] * num
                current *= summa
            if result < current:
                print(f'{unknowns = }')
                print(f'{z = }')
                result = current

    return result


def create_matrix(data: tuple, size: int = 4) -> list:
    matrix = [[1] * len(data) + [100]]
    for i in range(size):
        matrix.append([item[i] for item in data] + [0])
    return matrix


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
    data = get_ingredients(get_data(2015, 15))
    matrix = create_matrix(data.values())
    print(*matrix, sep='\n')
    print('result')
    print(solve_linear_system(matrix))
    # 26127360 is too high

    # ### First part:
    # x + y + z + w = 100
    # 2x > 0
    # 5y - w > 0
    # -2x - 3y + 5z > 0
    # -1z + 5w > 0

    # print('Part one:', part_one())
    # print('Part two:', result)


if __name__ == '__main__':
    test_all()
    main()
