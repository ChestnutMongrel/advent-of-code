from common import timer, get_data
from hashlib import md5
from functools import lru_cache


def test_all() -> None:
    data = 'abc'

    correct = '18f47a30'
    result = part_one(data)
    assert correct == result, f'Should be {correct}, got {result} instead.'
    correct = '05ace8e3'
    result = part_two(data)
    assert correct == result, f'Should be {correct}, got {result} instead.'


# I should probably start not in 0...
@lru_cache()
def find_hash(data: str, number: int) -> tuple:
    data = data.encode()
    start = '0' * 5
    while number:
        check = data + str(number).encode()
        hash_value = md5(check).hexdigest()
        if hash_value.startswith(start):
            return number, hash_value
        number += 1


@timer
def part_one(data: str) -> str:
    result = ''
    len_required = 8

    number = 111_111
    while len(result) < len_required:
        number, hash_value = find_hash(data, number + 1)
        result += hash_value[5]

    return result


@timer
def part_two(data: str) -> str:
    len_required = 8
    result = [None] * len_required
    ind_position = 5
    ind_value = 6

    number = 111_111
    while None in result:
        number, hash_value = find_hash(data, number + 1)
        if hash_value[ind_position].isdigit():
            position = int(hash_value[ind_position])
            if position < len_required and result[position] is None:
                result[position] = hash_value[ind_value]

    return ''.join(result)


def main() -> None:
    data = get_data(2016, 5)[0]
    print('Part one:', part_one(data))
    print('Part two:', part_two(data))


if __name__ == '__main__':
    test_all()
    main()
