from common import get_data, timer
from re import findall


def test_all() -> None:
    check = (
        ('turn off 499,499 through 500,500', 0),
        ('turn on 0,0 through 999,999', 1_000_000),
        ('toggle 0,0 through 999,0', 1000)
    )
    for data, correct in check:
        result = count_lights([data])
        assert correct == result, f'Should be {correct}, got {result} instead.'


# it's too slow...
# @timer
def count_lights(instructions: tuple, brightness: bool = False) -> int:
    size = 1000
    grid = [[0] * size for _ in range(size)]

    if brightness:
        for line in instructions:
            f_s, s_s, f_f, s_f = tuple(map(int, findall(r'\d+', line)))  # Yeh, nice joke, very funny...
            for i in range(f_s, f_f + 1):
                for ii in range(s_s, s_f + 1):
                    if line.startswith('turn on'):
                        grid[i][ii] += 1
                    elif line.startswith('turn off'):
                        grid[i][ii] -= 1 if grid[i][ii] > 0 else 0
                    else:
                        grid[i][ii] += 2

    else:
        for line in instructions:
            f_s, s_s, f_f, s_f = tuple(map(int, findall(r'\d+', line)))  # Yeh, nice joke, very funny...
            for i in range(f_s, f_f + 1):
                for ii in range(s_s, s_f + 1):
                    grid[i][ii] = int(not grid[i][ii] if line.startswith('toggle') else line.startswith('turn on'))

    return sum(sum(item) for item in grid)


def main() -> None:
    print('Part one:', count_lights(get_data(2015, 6)))
    print('Part two:', count_lights(get_data(2015, 6), True))


if __name__ == '__main__':
    test_all()
    main()
