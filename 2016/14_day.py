from common import get_data, timer
from hashlib import md5
from functools import lru_cache


def test_all() -> None:
    salt = 'abc'
    correct = 22728
    result = part_one(salt)
    assert correct == result, f'Should be {correct}, got {result} instead.'
    correct = 22551
    result = part_one(salt, True)
    assert correct == result, f'Should be {correct}, got {result} instead.'


@lru_cache()
def find_hash(data: str) -> str:
    data = data.encode()
    return md5(data).hexdigest()


def find_tripled_symbol(data: str) -> str | None:
    for i in range(len(data) - 2):
        if data[i:i + 3] == data[i] * 3:
            return data[i]

    return None


@lru_cache()  # How does it work? And why it does not...
def repeat_hashing(data: str) -> str:
    # Will it be faster if I would not encode and decode it repeatedly...
    for _ in range(2016):
        data = md5(data.encode('utf-8')).hexdigest()
    return data


@timer
def part_one(data: str, stretching: bool = False) -> int:
    amount_to_find = 64
    result = None
    index = 0
    hash_results = dict()

    while amount_to_find:
        hash_line = find_hash(data + str(index))
        if stretching:
            hash_line = repeat_hashing(hash_line)

        if tripled := find_tripled_symbol(hash_line):
            # print(f'{index = }')
            for i in range(index + 1, index + 1001):
                if i not in hash_results:
                    hash_results[i] = find_hash(data + str(i))
                    if stretching:
                        hash_results[i] = repeat_hashing(hash_results[i])
                new_hash = hash_results[i]
                if tripled * 5 in new_hash:
                    amount_to_find -= 1
                    result = index
                    # print(result)
                    break

        index += 1

    return result


def main() -> None:
    data = get_data(2016, 14)[0]
    print('Part one:', part_one(data))
    print('Part two:', part_one(data, True))
    # part_one took 142.674389273044653 secs


if __name__ == '__main__':
    test_all()
    main()
