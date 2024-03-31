from common import read_file, get_data
from dataclasses import dataclass
from math import ceil
# from collections import Iterator


@dataclass
class Item:
    # name: str
    # kind: str
    cost: int
    damage: int
    armor: int

    def __add__(self, other: 'Item'):
        cost = self.cost + other.cost
        damage = self.damage + other.damage
        armor = self.armor + other.armor
        return Item(cost, damage, armor)


@dataclass
class Hero:
    hit_points: int
    damage: int
    armor: int

    def __add__(self, other: 'Hero|Item'):
        hit_points = self.hit_points
        if type(other) == Hero:  # ??
            hit_points += other.hit_points
        damage = self.damage + other.damage
        armor = self.armor + other.armor
        return Hero(hit_points, damage, armor)


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


# Lots of repetitive code...
def part_one(shop: dict, boss: Hero) -> tuple:
    gold = 100
    player_hit = 100
    spend = set()
    spend_and_lose = set()
    player = Hero(player_hit, 0, 0)

    for weapon in shop['Weapons']:  # type: Item
        if not is_player_won(player + weapon, boss):
            spend_and_lose.add(weapon.cost)
        elif weapon.cost <= gold:
            spend.add(weapon.cost)

        for armor in shop['Armor']:  # type: Item
            current_items = weapon + armor
            if not is_player_won(player + current_items, boss):
                spend_and_lose.add(current_items.cost)
            elif current_items.cost <= gold:
                spend.add(current_items.cost)

        for i, ring in enumerate(shop['Rings']):
            current_items = weapon + ring
            if not is_player_won(player + current_items, boss):
                spend_and_lose.add(current_items.cost)
            elif current_items.cost <= gold:
                spend.add(current_items.cost)

            for armor in shop['Armor']:
                current_items = weapon + ring + armor
                if not is_player_won(player + current_items, boss):
                    spend_and_lose.add(current_items.cost)
                elif current_items.cost <= gold:
                    spend.add(current_items.cost)

            for second_ring in shop['Rings'][i + 1:]:
                current_items = weapon + ring + second_ring
                if not is_player_won(player + current_items, boss):
                    spend_and_lose.add(current_items.cost)
                elif current_items.cost <= gold:
                    spend.add(current_items.cost)

                for armor in shop['Armor']:
                    current_items = weapon + ring + second_ring + armor
                    if not is_player_won(player + current_items, boss):
                        spend_and_lose.add(current_items.cost)
                    elif current_items.cost <= gold:
                        spend.add(current_items.cost)

    if spend:
        return min(spend), max(spend_and_lose)
    else:
        return 0, 0


def shop_items() -> dict:
    shop = dict()
    kind = ''
    for line in read_file('data/21_item_shop.txt'):
        if ':' in line:
            kind, _ = line.split(':')
            shop[kind] = list()
        elif line:
            data = line.split()
            item = Item(*map(int, data[-3:]))
            shop[kind].append(item)

    for key, value in shop.items():
        shop[key] = sorted(value, key=lambda item: item.cost)
    return shop


def is_player_won(player: Hero, boss: Hero) -> bool:
    player_damage = player.damage - boss.armor
    if player_damage < 1:
        player_damage = 1
    boss_damage = boss.damage - player.armor
    if boss_damage < 1:
        boss_damage = 1

    player_moves = ceil(boss.hit_points / player_damage)
    boss_moves = ceil(player.hit_points / boss_damage)

    return player_moves <= boss_moves + 1


def main() -> None:
    shop = shop_items()

    boss = Hero(*map(lambda line: int(line.split()[-1]), get_data(2015, 21)))
    win, lose = part_one(shop, boss)
    print('Part one:', win)
    print('Part two:', lose)


if __name__ == '__main__':
    test_all()
    main()
