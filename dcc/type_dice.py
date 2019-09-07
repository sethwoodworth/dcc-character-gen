"""Dynamically create dice class objects."""
from random import choice


DICE = [3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 20, 24, 30]
_roll = lambda s: choice(range(1, s.sides + 1))
_multiply = lambda s, o: [s() for _ in range(o)]


typecast = lambda sides: type(
    f"d{sides}",
    (object,),
    {"__call__": _roll, "__mul__": _multiply, "__rmul__": _multiply, "sides": sides},
)()
globals().update({"d" + str(d): typecast(d) for d in DICE})
