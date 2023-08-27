import random

def roll_dice():
  """Rolls a dice and returns a random number between 1 and 6."""
  return random.randint(1, 6)

def main():
  """The main function."""
  while True:
    print("Rolling the dice...")
    number = roll_dice()
    print("The number is:", number)
    print("Would you like to roll the dice again? (y/n)")
    answer = input()
    if answer == "y":
      continue
    else:
      break

if __name__ == "__main__":
  main()
