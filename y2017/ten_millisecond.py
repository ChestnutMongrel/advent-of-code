from common import read_file, get_data, timer

YEAR = 2017
DAY = 10


ADDITIONAL_LENGTHS = tuple(map(int, '17, 31, 73, 47, 23'.split(', ')))


def test_all() -> None:
    test_part_one()
    test_chunks()
    test_part_two()


def test_part_one() -> None:
    number = 5
    lengths = tuple(map(int, '3, 4, 1, 5'.split(', ')))
    correct = 12
    numbers = part_one(lengths, amount=number)
    result = numbers[0] * numbers[1]
    assert correct == result, f'Should be {correct}, got {result} instead.'


def test_chunks() -> None:
    line = '65 ^ 27 ^ 9 ^ 1 ^ 4 ^ 3 ^ 40 ^ 50 ^ 91 ^ 7 ^ 6 ^ 0 ^ 2 ^ 5 ^ 68 ^ 22'
    data = tuple(map(int, line.split(' ^ ')))

    check = (
        (convert_to_bytes('1,2,3'), (49, 44, 50, 44, 51)),
        (xor(data), 64),
        (convert_to_hex((64, 7, 255)), '4007ff')
    )
    for result, correct in check:
        assert correct == result, f'Should be {correct}, got {result} instead.'


def test_part_two() -> None:
    check = (
        ('', 'a2582a3a0e66e6e86e3812dcb672a272'),
        ('AoC 2017', '33efeb34ea91902bb2f59c9920caa6cd'),
        ('1,2,3', '3efbe78a8d82f29979031a4aa0b16a9d'),
        ('1,2,4', '63960835bcdc130f0b66d7ff4f6a5a8e')
    )
    for data, correct in check:
        result = knot_hashing(data)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def part_one(lengths: tuple, amount: int = 256, repetitions: int = 1) -> tuple:
    numbers = list(range(amount))
    skip_size = 0
    current = 0
    for _ in range(repetitions):
        for value in lengths:
            if current + value > amount:
                portion = numbers[current:] + numbers[:current + value - amount]
            else:
                portion = numbers[current:current + value]
            for ind, symbol in enumerate(reversed(portion)):
                numbers[(current + ind) % amount] = symbol
            current = (current + value + skip_size) % amount
            skip_size += 1
    return numbers


def convert_to_bytes(line: str) -> tuple:
    result = list()
    for symbol in line:
        result.append(ord(symbol))
    return tuple(result)


def xor(numbers: tuple) -> int:
    result = numbers[0]
    for num in numbers[1:]:
        result ^= num
    return result


def convert_to_hex(numbers: tuple) -> str:
    result = ''
    for num in numbers:
        line = hex(num)[2:]
        if len(line) == 1:
            result += '0'
        result += line
    return result


def knot_hashing(lengths_str: str) -> str:
    # 1. Convert characters (your input) to bytes using their ASCII codes.
    # 2. Once you have determined the sequence of lengths to use, add the following lengths to the end of the sequence:
    #       17, 31, 73, 47, 23.
    lengths = convert_to_bytes(lengths_str) + ADDITIONAL_LENGTHS

    # 3. Second, instead of merely running one round like you did above, run a total of 64 rounds, using the same
    #       length sequence in each round. The current position and skip size should be preserved between rounds.
    repetitions = 64
    sparse_hash = part_one(lengths, repetitions=repetitions)

    # Use numeric bitwise XOR to combine each consecutive block of 16 numbers
    size = 16
    dense_hash = list()
    for i in range(0, size ** 2, size):
        dense_hash.append(xor(sparse_hash[i:i + size]))

    # Finally, convert in hexadecimal notation
    return convert_to_hex(tuple(dense_hash))


def main() -> None:
    data = get_data(year=YEAR, day=DAY)[0]
    numbers = tuple(map(int, data.split(',')))
    result = part_one(numbers)
    print('Part one:', result[0] * result[1])
    print('Part two:', knot_hashing(data))


if __name__ == '__main__':
    test_all()
    main()
