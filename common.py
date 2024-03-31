import functools
import time
import requests


def read_file(file_name: str):
    with open(file_name, 'r') as file:
        while line := file.readline():
            yield line.strip('\n')


def sum_tuple(a: tuple, b: tuple) -> tuple:
    # return a[0] + b[0], a[1] + b[1]
    return tuple(f + s for f, s in zip(a, b))


def find_start(maze: list) -> tuple:
    for line in maze:
        x = line.find('S')
        if x != -1:
            y = maze.index(line)
            break
    return y, x


def to_numbers(data: str, sep: str = None) -> tuple:
    return tuple(int(i) for i in data.split(sep))


# This is not a timer! It is a stopwatch...
def timer(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} took {runtime:.15f} secs")
        return result
    return _wrapper


# !!! Very bad written...
def get_data(year: int, day: int) -> tuple:
    token = {'session': ""}
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    data = requests.get(url, cookies=token)

    # return tuple(data.text.split('\n'))

    for item in data.text.split('\n'):
        if item:
            yield item


# url = f'https://adventofcode.com/2015/day/4/input'
# get_data(2015, 4)
