import random

def guess(x):
  random_number = random.randint(1,x)
  guess= 0
  while guess != random_number:
    guess=int(input(f'I\'m thinking of a number, guess a number between 1 and {x}: '))
    if guess < random_number:
      print("Too low, guess again! ")
    elif guess > random_number:
      print("Too high, guess again! ")

  print(f'Correct! The Number I was thinking of was  {random_number} ')


def computer_guess(x):
  low = 1
  high = x
  feedback = ''
  while feedback !='c':
    if low != high: 
      guess = random.randint(low, high)
    else:
      guess = low
    feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)?\n').lower()
    if feedback == 'h':
      high = guess - 1
    elif feedback == 'l':
      low = guess + 1 
  print(f'Horray! the number was {guess}, I guessed correctly!')

computer_guess (100)
