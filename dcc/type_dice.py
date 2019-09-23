"""Dynamically create dice class objects."""
from random import choice, choices


#: Dungeon Crawl Classics uses the following types of dice:
DICE = [3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 20, 24, 30]

#: A function to return a random int given a number of die sides
_roll = lambda s: choice(range(1, s.sides + 1))
#: Allows using the multiply operator to return N * die rolls
_multiply = lambda s, o: choices(range(1, s.sides + 1), k=o)

#: A function to dynamically create
typecast = lambda sides: type(
    f"d{sides}",
    (object,),
    {"__call__": _roll, "__mul__": _multiply, "__rmul__": _multiply, "sides": sides},
)()
globals().update({"d" + str(d): typecast(d) for d in DICE})
