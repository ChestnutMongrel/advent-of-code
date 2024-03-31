from common import get_data


def test_all() -> None:
    instructions = (
        'rect 3x2',
        'rotate column x=1 by 1',
        'rotate row y=0 by 4',
        'rotate column x=1 by 1'
    )

    correct = ''' #  # #
# #    
 #     '''
    result = '\n'.join(turn_on_pixels(instructions, 3, 7))
    assert correct == result, f'Should be {correct}, got {result} instead.'


def turn_on_pixels(instructions: tuple, rows: int = 6, columns: int = 50) -> tuple:
    matrix = [[' '] * columns for _ in range(rows)]

    for line in instructions:  # type: str
        action, *rest = line.split()

        if action == 'rect':
            # 'rect AxB'
            column, row = rest[0].split('x')
            for i in range(int(row)):
                for j in range(int(column)):
                    matrix[i][j] = '#'

        elif action == 'rotate':
            *_, index = rest[1].split('=')
            index = int(index)
            shift = int(rest[-1])

            if rest[0] == 'row':
                # 'rotate row y=A by B'
                # 'rotate column x=A by B'
                matrix[index] = matrix[index][-shift:] + matrix[index][:-shift]

            elif rest[0] == 'column':
                column = [matrix[i][index] for i in range(rows)]
                shifted_column = column[-shift:] + column[:-shift]
                for i in range(rows):
                    matrix[i][index] = shifted_column[i]

        # print(line)
        # print(*matrix, sep='\n')

    result = [''.join(line) for line in matrix]
    return tuple(result)


def part_one(instructions: tuple) -> int:
    matrix = turn_on_pixels(instructions)
    print(*matrix, sep='\n')
    total = ''.join(matrix).count('#')
    return total


def main() -> None:
    data = get_data(2016, 8)
    print('Part one:', part_one(data))
    # Part two blew my mind... How did they do that?


if __name__ == '__main__':
    test_all()
    main()
