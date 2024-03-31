from common import get_data
from collections import Counter
from string import ascii_lowercase


def test_shift_decrypt() -> None:
    data = 'qzmt-zixmtkozy-ivhz-343'
    result = shift_decrypt(data)
    correct = 'very encrypted name'
    assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def test_is_real_room() -> None:
    check = (
        ('aaaaa-bbb-z-y-x-123[abxyz]', True),
        ('a-b-c-d-e-f-g-h-987[abcde]', True),
        ('not-a-real-room-404[oarel]', True),
        ('totally-real-room-200[decoy]', False)
    )
    for data, correct in check:
        letters, sector_id, checksum = parse_data(data)
        result = is_real_room(letters, checksum)
        assert correct == result, f'For {data} should be {correct}, got {result} instead.'


def parse_data(line: str) -> tuple:
    # The line looks like this:
    # aaaaa-bbb-z-y-x-123[abxyz]

    name_id, checksum = line[:-1].split('[')
    *letters, sector_id = name_id.split('-')
    sector_id = int(sector_id)
    letters = ''.join(letters)

    return letters, sector_id, checksum


def is_real_room(name: str, checksum: str) -> bool:
    frequency_dict = Counter(name)
    check_dict = dict()
    for key, value in frequency_dict.items():
        check_dict.setdefault(value, list()).append(key)
    check_line = ''
    for key in sorted(check_dict, reverse=True):
        check_line += ''.join(sorted(check_dict[key]))
    return check_line[:len(checksum)] == checksum


def shift_decrypt(data: str) -> str:
    *name, num = data.split('-')
    num = int(num)
    letters_amount = len(ascii_lowercase)
    real = ''
    for line in name:
        for letter in line:
            index = (ascii_lowercase.find(letter) + num) % letters_amount
            real += ascii_lowercase[index]
        real += ' '
    return real[:-1]


def main() -> None:
    data = get_data(2016, 4)
    sum_id = 0
    storage_room = 'northpole object storage'
    storage_id = None

    for line in data:
        letters, sector_id, checksum = parse_data(line)
        if is_real_room(letters, checksum):
            sum_id += sector_id
            room_name, _ = line.split('[')
            if shift_decrypt(room_name) == storage_room:
                storage_id = sector_id

    print('Part one:', sum_id)
    print('Part two:', storage_id)


if __name__ == '__main__':
    test_is_real_room()
    test_shift_decrypt()
    main()
