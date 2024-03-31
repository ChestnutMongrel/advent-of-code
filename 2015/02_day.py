from common import read_file
from math import prod


def test_all() -> None:
    example = '2x3x4'
    result = surface_plus(example)
    correct = 58
    assert result == correct, f'Should be {correct}, got {result} instead.'

    result_2 = ribbon_length(example)
    correct_2 = 34
    assert result_2 == correct_2, f'Should be {correct_2}, got {result_2} instead.'


def side_lengths(dimensions: str) -> tuple:
    return tuple(map(int, dimensions.split('x')))


def surface_plus(dimensions: str) -> int:
    l, w, h = side_lengths(dimensions)
    faces = l * w, w * h, h * l
    return 2 * sum(faces) + min(faces)


def ribbon_length(dimensions: str) -> int:
    edges = sorted(side_lengths(dimensions))
    return 2 * (edges[0] + edges[1]) + prod(edges)


def main() -> None:
    name = 'data/02_input.txt'
    print('Part one:', sum(map(surface_plus, read_file(name))))
    print('Part two:', sum(map(ribbon_length, read_file(name))))


if __name__ == '__main__':
    test_all()
    main()
