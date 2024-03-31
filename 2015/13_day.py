from common import read_file, get_data
from itertools import permutations, pairwise


def test_all() -> None:
    check = ()
    data = read_file('data/13_input.txt')
    correct = 330
    result = part_one(data)
    assert correct == result, f'Should be {correct}, got {result} instead.'


# This is a brute force... T_T
def part_one(data: tuple, me_invited: bool = False) -> int:
    guests = list()
    guests_data = dict()
    happiness = list()
    for item in data:
        # Each line of data looks like this:
        # 'Alice would gain 54 happiness units by sitting next to Bob.'
        name, *information, other = item.split()
        other = other[:-1]
        amount = int(information[2])
        if 'lose' in item:
            amount *= -1
        if name not in guests:
            guests.append(name)
        guests_data.setdefault(name, list()).append((other, amount))

    if me_invited:
        guests.append('me')
    # print(*guests_data.items(), sep='\n')

    guests_amount = len(guests)
    for name, information in guests_data.items():
        happiness.append([0] * guests_amount)
        ind = guests.index(name)
        for other, amount in information:
            other_ind = guests.index(other)
            happiness[ind][other_ind] = amount

    if me_invited:
        happiness.append([0] * guests_amount)
    # print(*happiness, sep='\n')

    total_happiness = set()
    for item in permutations(range(guests_amount), guests_amount):
        # print(item)
        total = 0
        for a, b in pairwise(item):
            total += happiness[a][b] + happiness[b][a]
        a = item[0]
        b = item[-1]
        total += happiness[a][b] + happiness[b][a]
        total_happiness.add(total)

    return max(total_happiness)


def main() -> None:
    # data = get_data(2015, 13)
    print('Part one:', part_one(get_data(2015, 13)))
    print('Part two:', part_one(get_data(2015, 13), True))
    # print('Part two:', result)


if __name__ == '__main__':
    test_all()
    main()
