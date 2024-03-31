"""
--- Day 22: Sand Slabs ---
3d tetris but in two 2D XD I hope to make it...
"""


from common import read_file
from common import to_numbers
from copy import deepcopy


class Brick:
    def __init__(self, first: tuple, second: tuple):
        # It might be helpful to orient all bricks by z.
        if second[2] < first[2]:
            second, first = first, second
        self.x0 = first[0]
        self.y0 = first[1]
        self.z0 = first[2]
        self.x1 = second[0]
        self.y1 = second[1]
        self.z1 = second[2]

    def __repr__(self):
        return f'{self.x0}, {self.y0}, {self.z0} - {self.x1}, {self.y1}, {self.z1}'


def can_be_safely_disintegrated(lay_under: dict, supports: dict) -> tuple:
    safely = set()
    for brick, above in supports.items():
        for item in above:
            if len(lay_under[item]) == 1:
                break
        else:
            safely.add(brick)

    return tuple(safely)


def how_many_fall(lay_under: dict, supports: dict, can_be_removed: tuple) -> int:
    new_supports = dict()
    for brick, values in reversed(supports.items()):
        all_bricks = set(values)
        for item in values:
            all_bricks.update(new_supports[item])
        new_supports[brick] = all_bricks

    for brick, values in reversed(new_supports.items()):
        new_values = values.copy()
        # Why values was unsorted? I know that set has not to be sorted, but it was before...
        for item in sorted(values):
            if lay_under[item] != {brick} and lay_under[item].intersection(new_values) != lay_under[item]:
                new_values.remove(item)
        new_supports[brick] = new_values

    for item, value in new_supports.items():
        if item in can_be_removed and len(value) != 0:
            print(item, value)
    total = sum(len(new_supports[item]) for item in new_supports if item not in can_be_removed)
    return total


def under_and_above(stack: tuple) -> tuple:
    # How many bricks lie under the key brick (a.k.a. how many ones support the key brick).
    lay_under = dict()
    # Which bricks are supported by the key brick (a.k.a. which bricks are lying down on the key brick).
    supports = dict()

    size = 10
    level = [[0] * size for _ in range(size)]
    new_ = {1: deepcopy(level)}

    for i, brick in enumerate(stack, 1):
        for z in range(brick.z0 - 1, 0, -1):
            if z not in new_:
                continue
            under = set()
            # x0, y0 might be > than x1, y1 !!! Weak spot !!!
            for x in range(brick.x0, brick.x1 + 1):
                for y in range(brick.y0, brick.y1 + 1):
                    num = new_[z][x][y]
                    if num:
                        under.add(num)
            if not under:
                continue
            lay_under[i] = under
            for item in under:
                supports[item] = supports.get(item, list()) + [i]
            dif_z = brick.z0 - (z + 1)
            brick.z0 -= dif_z
            brick.z1 -= dif_z
            break
        else:
            brick.z1 += -brick.z0 + 1
            brick.z0 = 1

        for z in range(brick.z0, brick.z1 + 1):
            # x0, y0 might be > than x1, y1 !!! Weak spot !!!
            if z not in new_:
                new_[z] = deepcopy(level)
            for x in range(brick.x0, brick.x1 + 1):
                for y in range(brick.y0, brick.y1 + 1):
                    new_[z][x][y] = i

        if i not in supports:
            supports[i] = list()

    return lay_under, supports


def bricks_stack(lines) -> tuple:
    bricks = list()
    for data in lines:
        first, second = data.split('~')
        bricks.append(Brick(to_numbers(first, ','), to_numbers(second, ',')))
    return tuple(bricks)


def main() -> None:
    for name in ('data/example_22.txt', 'data/22_input.txt',):  #
        stack = bricks_stack(read_file(name))

        stack = tuple(sorted(stack, key=lambda x: x.z0))
        lay_under, supports = under_and_above(stack)
        bricks_to_destroy = can_be_safely_disintegrated(lay_under, supports)
        print('How many bricks could be safely chosen as the one to get disintegrated?')
        print(len(bricks_to_destroy),)

        total = how_many_fall(lay_under, supports, bricks_to_destroy)
        print('What is the sum of the number of other bricks that would fall?')
        print(total, '\n')


if __name__ == '__main__':
    main()
