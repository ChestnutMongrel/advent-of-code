"""
This code is so awful, you have no idea... >_< T_T
"""


from common import get_data, read_file
from dataclasses import dataclass, field
from copy import deepcopy


spending = float('inf')


@dataclass
class Spell:
    cost: int
    damage: int = 0
    heal: int = 0
    armor: int = 0
    mana: int = 0
    timer: int = 0


@dataclass
class Hero:
    hit_points: int = 100
    damage: int = 0


# After 'shield' is off the wizard still has the armor...
@dataclass
class Wizard:
    hit_points: int
    mana: int
    spells: dict
    armor: int = 0
    effects: dict = field(default_factory=dict)

    def cast_spell(self, name: str) -> int:
        spell = self.spells[name]
        if self.mana < spell.cost:
            return 0

        self.mana -= spell.cost
        damage = 0
        if spell.timer and name not in self.effects:
            self.effects[name] = spell.timer
        else:
            if spell.damage:
                damage = spell.damage
            if spell.heal:
                self.hit_points += spell.heal

        return damage

    def use_effects(self) -> int:
        # if not self.effects:
        #     return 0

        # print(f'{self.effects = }')
        # if 'Shield' not in self.effects:
        #     # Why is it not working?..
        #     print(f'{self.armor = }')
        #     self.armor = 0

        self.armor = 0
        damage = 0

        for name, left in self.effects.items():
            spell: Spell = self.spells[name]

            if left:
                if spell.damage:
                    damage += spell.damage
                if spell.armor:
                    self.armor = spell.armor
                self.hit_points += spell.heal
                self.mana += spell.mana
                left -= 1
                self.effects[name] = left

        self.effects = {name: left for name, left in self.effects.items() if left}

        return damage

    # def __iadd__(self, spell: Spell):
    #     self.hit_points += spell.heal
    #     self.mana += spell.mana
    #     self.armor = spell.armor
    #     return self

    def __str__(self):
        to_print = f'The Nameless Wizard has {self.hit_points} hit points, {self.armor} armor, {self.mana} mana'
        return to_print


def test_all() -> None:
    # wizard = Wizard(10, 250, spellbook())
    # boss = Hero(13, 8)
    # print('in test')
    # print(fight(wizard, boss))
    # print(f'{min(spending) = }')
    # Correct 226

    wizard = Wizard(10, 250, spellbook())
    boss = Hero(14, 8)
    print('in test')
    print(fight(wizard, boss))
    print(f'{spending = }')
    # Correct 641


def spellbook() -> dict:
    spells = dict()
    spells['Magic Missile'] = Spell(53, damage=4)
    spells['Drain'] = Spell(73, damage=2, heal=2)
    spells['Shield'] = Spell(113, armor=7, timer=6)
    spells['Poison'] = Spell(173, damage=3, timer=6)
    spells['Recharge'] = Spell(229, mana=101, timer=5)
    return spells


def fight(wizard: Wizard, boss: Hero, spend: int = 0, spells: tuple = tuple(), wizard_turn: bool = True) -> 0:
    global spending

    # print(spells)
    if spend > spending:
        return 0
    if not wizard_turn:
        spell = spells[-1]
        boss.hit_points -= wizard.cast_spell(spell)
        if boss.hit_points <= 0:
            if spend < spending:
                spending = spend
                print(spend)
                print(spells)
            return spend
    else:
        wizard.hit_points -= 1
        if wizard.hit_points <= 0:
            return 0

    boss.hit_points -= wizard.use_effects()

    if boss.hit_points <= 0:

        if spend < spending:
            spending = spend
            print(spend)
            print(spells)
        return spend

    if wizard_turn:
        wizard_turn = not wizard_turn

        for name, spell in wizard.spells.items():  # type: str, Spell
            if spell.cost <= wizard.mana and \
                    (not wizard.effects or name not in wizard.effects):
                fight(deepcopy(wizard), deepcopy(boss), spend + spell.cost, spells + (name,), wizard_turn)

    else:
        wizard.hit_points -= boss.damage - wizard.armor
        if wizard.hit_points <= 0:
            return 0
        fight(deepcopy(wizard), deepcopy(boss), spend=spend, spells=spells)


def part_one(boss: Hero) -> int:
    wizard = Wizard(50, 500, spellbook())
    print(wizard)
    # wizard_turn = True
    spend = set()

    fight(deepcopy(wizard), deepcopy(boss))

    return 0


def step_by_step_fight(spells: tuple, boss: Hero) -> int:
    wizard = Wizard(50, 500, spellbook())
    print(wizard)
    print(boss)
    print('Fight!')

    spend = 0
    for spell in spells:
        print('--Wizard turn--')
        print('=Wizard lose one hit point=')
        wizard.hit_points -= 1
        print(wizard)
        if wizard.hit_points <= 0:
            print('Boss wins!')
            return 0

        if wizard.effects:
            print('=Wizard uses effects=')
            print(wizard.effects)
            boss.hit_points -= wizard.use_effects()
            print(boss)
            if boss.hit_points <= 0:
                print('Wizard wins!')
                return spend

        print(f'=Wizard casts spell {spell}=')
        if wizard.spells[spell].cost <= wizard.mana:  # type: Spell
            spend += wizard.spells[spell].cost
            boss.hit_points -= wizard.cast_spell(spell)
            print(wizard)
            print(boss)
            if boss.hit_points <= 0:
                print('Wizard wins!')
                return spend
        else:
            print('Not enough mana!')
            return 0

        print('--Boss turn--')
        if wizard.effects:
            print('=Wizard uses effects=')
            print(wizard.effects)
            boss.hit_points -= wizard.use_effects()
            print(boss)
            if boss.hit_points <= 0:
                print('Wizard wins!')
                return spend

        print(f'=Boss attacks for {boss.damage}=')
        wizard.hit_points -= boss.damage - wizard.armor
        print(wizard)
        if wizard.hit_points <= 0:
            print('Boss wins!')
            return 0


def main() -> None:
    boss = Hero(*map(lambda line: int(line.split()[-1]), get_data(2015, 22)))
    print('Part one:', part_one(boss))
    print(spending)


if __name__ == '__main__':
    # test_all()
    main()

    # for data in read_file('data/22_spells.txt'):
    #     data = tuple(data.split(', '))
    #     spend = part_two(data, Hero(51, 9))
    #     print(f'--Wizard spend {spend} mana--')
    #     input()
