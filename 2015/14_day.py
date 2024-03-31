from common import read_file, get_data


class Reindeer:
    # Is it an allowed practice to parce the string here?
    def __init__(self, name: str, speed: int, time: int, rest: int):
        self.name = name
        self.speed = speed
        self.time = time
        self.rest = rest


def test_all() -> None:
    data = tuple(map(create_deer, read_file('data/14_example.txt')))
    time = 1000
    check = (
        (race(data, time), 1120),
        (new_race(data, time), 689)
    )
    for result, correct in check:
        assert correct == result, f'Should be {correct}, got {result} instead.'


def create_deer(line: str) -> Reindeer:
    name, *information = line.split()
    data = list()
    for item in information:
        if item.isdigit():
            data.append(int(item))
    return Reindeer(name, *data)


def race(contestants: tuple, time: int) -> int:
    distances = list()
    for deer in contestants:
        distance = time // (deer.time + deer.rest) * deer.speed * deer.time
        time_left = time % (deer.time + deer.rest)
        distance += min(time_left, deer.time) * deer.speed
        distances.append(distance)

    return max(distances)


def new_race(contestants: tuple, time: int) -> int:
    points = dict().fromkeys((deer.name for deer in contestants), 0)
    distances = points.copy()

    for seconds in range(1, time + 1):
        for deer in contestants:
            moving_time = seconds % (deer.time + deer.rest)
            if moving_time and moving_time <= deer.time:
                distances[deer.name] += deer.speed
        max_dist = max(distances.values())
        for deer, dist in distances.items():
            if dist == max_dist:
                points[deer] += 1

    return max(points.values())


def main() -> None:
    data = tuple(map(create_deer, get_data(2015, 14)))
    time = 2503
    print('Part one:', race(data, time))
    print('Part two:', new_race(data, time))

if __name__ == '__main__':
    test_all()
    main()
