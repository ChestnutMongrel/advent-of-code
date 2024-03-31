from hashlib import md5


def test_all() -> None:
    check = (
        ('abcdef', 609043),
        ('pqrstuv', 1048970),
        ('abc', 3231929)  # This one is from fifth day of 2016.
    )
    for data, correct in check:
        result = find_hash(data)
        assert correct == result, f'Should be {correct}, got {result} instead.'
    print('test is done')


# ???
def find_hash(data: str, zeros: int = 5) -> int:
    data = data.encode()
    start = '0' * zeros
    result = 1
    while result:
        check = data + str(result).encode()
        if md5(check).hexdigest().startswith(start):
            return result
        result += 1


def main() -> None:
    data = 'bgvyzdsv'  # I should not leave it here...
    print('Part one:', find_hash(data))
    print('Part two:', find_hash(data, 6))


if __name__ == '__main__':
    test_all()
    main()
