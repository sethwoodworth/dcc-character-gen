from functools import partial
from random import sample


def roll(count: int, die: int):
    return sum(sample(range(1, die), count))


dice_chain = (
    "d3",
    "d4",
    "d5",
    "d6",
    "d7",
    "d8",
    "d10",
    "d12",
    "d14",
    "d16",
    "d20",
    "d24",
    "d30",
)


def cast_die(name):
    die = partial(roll, 1, int(name.replace("d", "")))
    die.name = name
    return die


globals().update({die: cast_die(die) for die in dice_chain})
