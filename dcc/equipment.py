from dataclasses import dataclass, field
from functools import partial
from random import choice

equipment = [
  ("Backpack", "2gp"),
  ("Candle", "1cp"),
  ("Chain, 10'", "30gp"),
  ("Chalk, 1 piece", "1cp"),
  ("Chest, empty", "2gp"),
  ("Crowbar", "2gp"),
  ("Flask, empty", "3cp"),
  ("Flint & steel", "15cp"),
  ("Grappling hook", "1gp"),
  ("Hammer, small", "5sp"),
  ("Holy symbol", "25gp"),
  ("Holy water, 1 vial**", "25gp"),
  ("Ironspikes, each", "1sp"),
  ("Lantern", "10gp"),
  ("Mirror, hand-sized", "10gp"),
  ("Oil, 1 flask***", "2sp"),
  ("Pole, 10-foot", "15cp"),
  ("Rations, per day", "5cp"),
  ("Rope, 50'", "25cp"),
  ("Sack, large", "12cp"),
  ("Sack, small", "8cp"),
  ("Thieves' tools", "25gp"),
  ("Torch, each", "1cp"),
  ("Waterskin", "5sp")
]

random_equipment = partial(choice(equipment))
