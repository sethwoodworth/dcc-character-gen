from __future__ import annotations
from collections import defaultdict
from dataclasses import dataclass, field
from functools import partial
from random import choice, sample
from typing import Callable, Dict, Optional, Tuple

from blessings import Terminal

from equipment import random_equipment
from occupations import occupations
from dice import roll, d3, d4, d5, d7, d8, d10, d12, d14, d16, d20, d24, d30


t = Terminal()

fiveD12 = partial(roll, 5, 12)
ability_roll = partial(roll, 3, 8)


@dataclass
class Ability:
    score: int = field(default_factory=ability_roll)

    @property
    def modifier(self):
        if self.score <= 3:
            return -3
        if 3 < self.score < 6:
            return -2
        elif 6 <= self.score < 9:
            return -1
        elif 9 <= self.score < 13:
            return 0
        elif 13 <= self.score < 16:
            return 1
        elif 15 < self.score < 18:
            return 2
        elif self.score >= 18:
            return 3

    mod = modifier


@dataclass
class Gender:
    type: str
    subject_pronoun: str
    object_pronoun: str
    reflexive_pronoun: str
    independent_posessive: str
    dependent_posessive: str


masc = Gender("masculine", "he", "him", "himself", "his", "his")
fem = Gender("femine", "she", "her", "herself", "hers", "her")
epicene = Gender("epicene", "they", "them", "themself", "theirs", "their")

abilities = ["strength", "agility", "stamina", "personality", "intelligence", "luck"]

@dataclass
class Character:
    name: str = "Ragnar"
    gender: Gender = field(default_factory=partial(choice, [masc, fem, epicene]))
    die: Callable[[None], int] = d20


    strength: Ability = field(default_factory=Ability)
    agility: Ability = field(default_factory=Ability)
    stamina: Ability = field(default_factory=Ability)
    personality: Ability = field(default_factory=Ability)
    intelligence: Ability = field(default_factory=Ability)
    luck: Ability = field(default_factory=Ability)

    max_hp: int = field(init=False)
    hp: int = field(init=False)

    xp: int = 0
    coins: int = field(default_factory=fiveD12)

    equipment: Tuple = field(default_factory=random_equipment)

    occupation: Dict = field(default_factory=partial(choice, occupations))
    level: int = 0

    def __post_init__(self):
        self.max_hp = roll(1, 4) + self.stamina.mod
        self.hp = self.max_hp

    @property
    def fortitude_mod(self):
        return self.stamina.mod

    @property
    def reflex_mod(self):
        return self.agility.mod

    @property
    def willpower_mod(self):
        return self.personality.mod

    @property
    def weapon(self):
        return self.occupation["weapon"]

    @property
    def attack_mod(self) -> int:
        if self.level == 0:
            return 0

    @property
    def attack_roll(self) -> str:
        return f"{self.die.name} + {self.attack_mod} + {self.strength.mod}"

    @property
    def abilities_by_type(self):
        abilities_desc = defaultdict(list)
        for ability in abilities:
            ability_mod = getattr(self, ability).mod
            if ability_mod < -2:
                abilities_desc['terrible'].append(ability)
            elif ability_mod < -1:
                abilities_desc['bad'].append(ability)
            elif ability_mod < 1:
                abilities_desc['ok'].append(ability)
            elif ability_mod < 2:
                abilities_desc['good'].append(ability)
            else:
                abilities_desc['great'].append(ability)
        return abilities_desc




def character_desc(c: Character):
    desc = (
        f"{t.bold_red(c.name)} is a {t.blue(c.occupation['title'])}. "
        f"{c.gender.subject_pronoun.capitalize()} wield a {t.bold(c.occupation['weapon'])} "
        f"by rolling {t.underline(c.attack_roll)}. "
        # f"{c.gender.subject_pronoun.capitalize()  "
    )
    for qualifier, abilities in c.abilities_by_type.items():
        desc = desc + (
            f"{c.gender.subject_pronoun.capitalize()} have {qualifier} {', '.join(abilities)}. "
        )

    return desc

def new():
    print(character_desc(Character()))

if __name__ == "__main__":
    c = Character()
    print(character_desc(c))
