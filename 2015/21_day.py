from common import read_file, get_data
from dataclasses import dataclass
from math import ceil
# from collections import Iterator


@dataclass
class Item:
    name: str
    kind: str
    cost: int
    damage: int
    armor: int


@dataclass
class Hero:
    hit_points: int
    damage: int
    armor: int

    def __add__(self, other: tuple):
        new_hero = Hero(self.hit_points, *other)
        new_hero.damage += self.damage
        new_hero.armor += self.armor
        return new_hero


def test_all() -> None:
    player = Hero(8, 5, 5)
    boss = Hero(12, 7, 2)
    result = is_player_won(player, boss)
    correct = True
    assert correct == result, f'Should be {correct}, got {result} instead.'

    player = Hero(20, 5, 2)
    boss = Hero(20, 7, 1)
    result = is_player_won(player, boss)
    correct = True
    assert correct == result, f'Should be {correct}, got {result} instead.'


def spend_with_armor(armors: list, gold_left: int, player: Hero, boss: Hero) -> list:
    for armor in armors:  # type: Item
        player_with_armor = player + (armor.damage, armor.armor)
        if armor.cost <= gold_left and is_player_won(player_with_armor, boss):
            yield armor.cost


def part_one(shop: dict, boss: Hero) -> int:
    gold = 100
    player_hit = 100
    spend = set()

    for weapon in shop['Weapons']:  # type: Item
        player = Hero(player_hit, weapon.damage, weapon.armor)
        spending = weapon.cost

        if spending <= gold and is_player_won(player, boss):
            spend.add(spending)

        for extra_spend in spend_with_armor(shop['Armor'], gold - spending, player, boss):
            spend.add(spending + extra_spend)

        for i, ring in enumerate(shop['Rings']):  # type: int, Item
            spend_ring = spending + ring.cost
            player_with_ring = player + (ring.damage, ring.armor)

            if spend_ring <= gold and is_player_won(player_with_ring, boss):
                spend.add(spend_ring)

            for extra_spend in spend_with_armor(shop['Armor'], gold - spend_ring, player_with_ring, boss):
                spend.add(spend_ring + extra_spend)

            if i < len(shop['Rings']) - 1:
                for second_ring in shop['Rings'][i+1:]:  # type: Item
                    spend_two_rings = spend_ring + second_ring.cost
                    player_with_two_rings = player_with_ring + (second_ring.damage, second_ring.armor)

                    if spend_two_rings <= gold and is_player_won(player_with_two_rings, boss):
                        spend.add(spend_two_rings)

                    for extra_spend in spend_with_armor(shop['Armor'], gold - spend_two_rings,
                                                        player_with_two_rings, boss):
                        spend.add(spend_two_rings + extra_spend)

    if spend:
        return min(spend)
    else:
        return 0


def shop_items() -> dict:
    shop = dict()
    kind = ''
    for line in read_file('data/21_item_shop.txt'):
        if ':' in line:
            kind, _ = line.split(':')
            shop[kind] = list()
        elif line:
            data = line.split()
            if len(data) == 4:
                name, *rest = data
            elif len(data) == 5:
                name = f'{data[0]} {data[1]}'
                rest = data[2:]
            item = Item(name, kind, *map(int, rest))
            shop[kind].append(item)

    for key, value in shop.items():
        shop[key] = sorted(value, key=lambda item: item.cost)
    return shop


def is_player_won(player: Hero, boss: Hero) -> bool:
    player_damage = player.damage - boss.armor
    boss_damage = boss.damage - player.armor

    player_moves = ceil(boss.hit_points / player_damage)
    boss_moves = ceil(player.hit_points / boss_damage)

    return player_moves <= boss_moves + 1


def main() -> None:
    shop = shop_items()

    boss = Hero(*map(lambda line: int(line.split()[-1]), get_data(2015, 21)))
    print('Part one:', part_one(shop, boss))
    # print('Part two:', result)


if __name__ == '__main__':
    test_all()
    main()
