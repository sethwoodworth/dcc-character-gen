from __future__ import annotations
from typing import Optional, Tuple
from functools import partial
from random import sample
from dataclasses import dataclass, field

from .equipment import random_equipment


def roll(count: int, die: int):
    return sum(sample(range(1, die), count))

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
        elif 5 < self.score < 9:
            return -1
        elif 9 <= self.score <= 12:
            return 0
        elif 12 < self.score < 16:
            return 1
        elif 16 < self.score < 18:
            return 2
        elif self.score > 18:
            return 3

    mod = modifier


@dataclass
class Character:
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

    def __post_init__(self):
        self.max_hp = roll(1, 4) + self.stamina.mod
        self.hp = self.max_hp

if __name__ == "__main__":
    c = Character()
