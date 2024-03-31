from common import read_file, to_numbers


class Hail:
    def __init__(self, position: tuple, velocity: tuple):
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        self.dx = velocity[0]
        self.dy = velocity[1]
        self.dz = velocity[2]
        self.a, self.b = self.xy_coefficient()
        self.z_a, self.z_b = self.xz_coefficient()

    def __repr__(self):
        return f'{self.x}, {self.y}, {self.z} | {self.dx}, {self.dy}, {self.dz} ({self.a}, {self.b})'

    def xy_coefficient(self):
        a = self.dy / self.dx
        b = (self.y * self.dx - self.x * self.dy) / self.dx
        return a, b

    def xz_coefficient(self):
        a = self.dz / self.dx
        b = (self.z * self.dx - self.x * self.dz) / self.dx
        return a, b

    def z_coefficient(self):
        z_a = self.a * self.dy / self.dz
        z_b = self.b * self.dz / self.dy - self.y * self.dz / self.dy + self.z
        return z_a, z_b

    # Need to add 'first: Hail'...
    def xy_intersection(self, other) -> tuple:
        # y = a * x + b
        if (self.a - other.a) == 0:
            return None, None
        inter_x = (other.b - self.b) / (self.a - other.a)
        inter_y = self.a * inter_x + self.b
        return inter_x, inter_y

    def xyz_intersection(self, other) -> tuple:
        # y = a * x + b
        # z = z_a * x + z_b
        if (divider := self.z_a - other.z_a) == 0:
            return None, None, None
        x = (other.z_b - self.z_b) / divider
        y = self.a * x + self.b
        z = self.z_a * x + self.z_b
        return x, y, z

    # How to write a method for a class, not for an instance?


def get_hail(line: str) -> Hail:
    # Can I make it a oneliner? Yep, I can... But should I?
    position, velocity = line.split(' @ ')
    position = to_numbers(position, ', ')
    velocity = to_numbers(velocity, ', ')
    return Hail(position, velocity)


def count_intersections(data: tuple, at_least: int, at_most: int) -> int:
    # intersections = list()
    amount = len(data)
    total_intersections = 0

    # I believe there is a function for this...
    for i, first in enumerate(data):
        for ii in range(i + 1, amount):

            second = data[ii]
            x, y = first.xy_intersection(second)
            if x is not None:
                if (x - first.x) / first.dx >= 0 and \
                        (x - second.x) / second.dx >= 0:
                    if at_least <= x <= at_most and at_least <= y <= at_most:
                        # print('x, y = ', x, y)
                        total_intersections += 1

    return total_intersections


def main() -> None:
    name1 = 'data/12_example.txt'
    data = tuple(get_hail(item) for item in read_file(name1))
    # print(*data, sep='\n')

    at_least = 7
    at_most = 27

    print(count_intersections(data, at_least, at_most))

    new_ = Hail((24, 13, 10), (-3, 1, 2))
    for item in data:
        print(item)
        print('inter:', item.xyz_intersection(new_))

    name2 = 'data/24_input.txt'
    data = tuple(get_hail(item) for item in read_file(name2))
    at_least = 200000000000000
    at_most = 400000000000000
    print(count_intersections(data, at_least, at_most))


if __name__ == '__main__':
    main()
