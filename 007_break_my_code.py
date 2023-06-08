import random

def persistent_input(message: str, validate: list[tuple[callable, str]]) -> str:
  while True:
    passFlag = True
    response = input(message)

    for exec in validate:
      if not exec[1](response):
        passFlag = False
        print(exec[0], end = '\n\n')
        break

    if passFlag: break

  return response

if __name__ == '__main__':
  while True:
    tries = 0
    num = random.randint(1, 50)

    guess = int(persistent_input(
      'What is your guess? ',
      [
        ('Please enter a number!', lambda x: x.isnumeric()),
        ('Please enter an integer!', lambda x: int(x))
      ]
    ))

    if guess < num:
      print('Oops. Too low.', end = '\n\n')
    elif guess > num:
      print('Oops. Too high.', end = '\n\n')
    else:
      print('Correct!', end = '\n\n')

      print('You managed to guess my secret code in %s tries!' % tries)
      replay = persistent_input(
        'Play again? ',
        [('Please enter "n" or "y"!', lambda x: x in ['n', 'y'])]
      )

      if replay == 'n':
        print('Goodbye.', end = '\n\n')
        break

    tries += 1

  