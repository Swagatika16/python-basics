from enum import Enum
from random import randint
import sys

class Options(Enum):
    __order__ = "Rock Paper Scissor Exit"
    Rock = 1
    Paper = 2
    Scissor = 3
    Exit = 4

winning_options = {
    Options.Rock: Options.Paper,
    Options.Paper: Options.Scissor,
    Options.Scissor: Options.Rock
}

print("Welcome to Play Arena!!!!")
while True:
    print("Choose your option:")
    val = int(input("\n".join([f"{option.value}. {option.name}" for option in Options])+"\n"))
    if val == Options.Exit.value:
        sys.exit()
    comp = randint(1, 3)
    if winning_options.get(Options(comp)) == Options(val):
        print("You Won!!!\n")
    elif comp == val:
        print("It's a Tie!!!\n")
    else:
        print("You Lost!!!\n")
