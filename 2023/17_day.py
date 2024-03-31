"""
--- Day 17: Clumsy Crucible ---
"""


from common import read_file, sum_tuple


def create_field(data: str) -> tuple:
    return tuple(int(item) for item in data)


def path(field: tuple) -> int:
    n = len(field)
    m = len(field[0])
    weights = [[float('inf') for _ in range(m)] for _ in range(n)]
    weights[0][0] = 0

    current = (0, 0)
    to_visit = (
        {'block': (0, 0), 'diff': (0, 1), 'direction': 0, 'steps': 0},
    )
    directions = (0, -1, 1)
    visited = {current}

    while True:
        if goals := tuple(filter(lambda item: item['block'] == (n-1, m-1), to_visit)):
            return goals
        new_to_visit = list()
        for data in to_visit:

            current = data['block']
            diff = data['diff']
            direction = data['direction']
            steps = data['steps']
            visited.add(current)
            for dd in directions:
                # if dd == direction:
                #     if steps == 3:
                #         continue
                #     else:
                #         steps += 1
                # else:
                #     steps = 1
                weight = weights[current[0]][current[1]]
                i, ii = diff
                if dd:
                    i, ii = ii * dd, i * dd
                # print(f'{dd = }')
                x, y = sum_tuple(current, (i, ii))
                # print('x, y', x, y)
                if (x, y) not in visited and 0 <= x < n and 0 <= y < m:
                    weight += field[x][y]
                    if weight < weights[x][y]:
                        weights[x][y] = weight
                        new_to_visit.append({'block': (x, y), 'diff': (i, ii), 'direction': dd, 'steps': steps})
        # print('to visit')
        # print(*new_to_visit, sep='\n')
        # print(*weights, sep='\n')
        to_visit = new_to_visit


def main() -> None:
    for name in ('data/17_input.txt',):  # 'data/15_input.txt'):
        data = read_file(name)
        field = tuple(create_field(item) for item in data)
        print(*field, sep='\n')
        print(*path(field), sep='\n')


if __name__ == '__main__':
    main()
