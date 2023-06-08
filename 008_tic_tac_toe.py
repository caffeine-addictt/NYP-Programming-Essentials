class Canvas:
  canvas: str
  player: tuple[str]

  def __init__(self, player1Letter: str, player2Letter: str) -> None:
    self._generate_canvas()
    self.player = (player1Letter, player2Letter)

  def _matches(self) -> list[str]:
    return [
      '111------',
      '---111---',
      '------111',
      '1--1--1--',
      '-1--1--1-',
      '--1--1--1',
      '1---1---1',
      '--1-1-1--'
    ]

  def _generate_canvas(self) -> None:
    self.canvas = '---------'

  def convert(self) -> list:
    final = []
    for i, v in enumerate(self.canvas):
      if (i + 1) % 3 == 0:
        final.append([])

      final[-1].append(v)
    return final


  def validate_match(self) -> dict:
    player1 = []
    player2 = []

    for matchCase in self._matches():
      p1 = []
      p2 = []

      for cellNum, cell in enumerate(matchCase):
        if cell != '-':
          p1.append(self.canvas[cellNum] == self.player[0])
          p2.append(self.canvas[cellNum] == self.player[1])

      player1.append(all(p1))
      player2.append(all(p2))

    return {
      'Player1': any(player1),
      'Player2': any(player2)
    }
  
  def check_avail(self, pos: int) -> bool:
    return self.canvas[pos] == '-'
  
  def draw(self, playerNum: int, pos: int) -> None:
    if not self.check_avail(pos - 1):
      raise ValueError('Unable to write to existing cell')
    self.canvas = self.canvas[:pos-1] + self.player[playerNum - 1] + self.canvas[pos:]

  def stdout(self, *args, **kwargs) -> None:
    final = ' '
    for i, cell in enumerate(self.canvas):
      if i % 3 == 0:
        final += '\n '

      final += f' {(cell == "-" and i+1 or cell)}'

    print(final, *args, **kwargs)




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

def is_integer(x) -> bool:
  try:
    float(x)
  except ValueError:
    return False
  else:
    return float(x).is_integer()



if __name__ == '__main__':
  while True:
    print('Tic-Tac-Toe Game')

    #init new game
    p1 = persistent_input('Player 1, please enter your letter: ', [
      ('Please use only one character!', lambda x: len(x) == 1),
      ('Please use a non-number!', lambda x: not x.isnumeric())
    ])
    p2 = persistent_input('Player 2, please enter your letter: ', [
      ('Cannot be same as player 1!', lambda x: x != p1),
      ('Please use only one character!', lambda x: len(x) == 1),
      ('Please use a non-number!', lambda x: not x.isnumeric())
    ])
    TicTacToe = Canvas(p1, p2)

    while ('-' in TicTacToe.canvas):
      #Stdout
      TicTacToe.stdout(end = '\n\n')

      # Get Player1
      p1_choice = int(persistent_input(
        'Player1 (%s): Which square number? ' % p1,
        [
          ('Please enter an integer!', lambda x: is_integer(x)),
          ('Space is occupied! Pick another.', lambda x: TicTacToe.check_avail(int(x) - 1))
        ]
      ))

      TicTacToe.draw(1, p1_choice)
      if TicTacToe.validate_match()['Player1']:
        print('Hooray! Player1 (%s) has won!' % p1, end = '\n\n')
        break
      elif not '-' in TicTacToe.canvas:
        break

      #Stdout
      TicTacToe.stdout(end = '\n\n')

      # Get Player2
      p2_choice = int(persistent_input(
        'Player2 (%s): Which square number? ' % p2,
        [
          ('Please enter an integer!', lambda x: is_integer(x)),
          ('Space is occupied! Pick another.', lambda x: TicTacToe.check_avail(int(x) - 1))
        ]
      ))

      TicTacToe.draw(2, p2_choice)
      if TicTacToe.validate_match()['Player2']:
        print('Hooray! Player2 (%s) has won!' % p2, end = '\n\n')
        break


    replay = persistent_input(
      'Do you want to play again (y/n)? ',
      [('Please enter "n" or "y"!', lambda x: x in ['n', 'y'])]
    )

    if replay == 'n':
      print('Goodbye!', end = '\n\n')
      break