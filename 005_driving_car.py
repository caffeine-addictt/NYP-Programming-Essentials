import time, keyboard

def driving_car(length: int = 30):
  global directionFlag
  directionFlag = 0 # 0-left 1-stop 2-right
  std = '=o^^o='
  pos = 0

  if length <= len(std): raise ValueError('Length too less!')

  def change(x: int) -> None:
    global directionFlag
    directionFlag = x

  keyboard.add_hotkey('left', lambda: change(0))
  keyboard.add_hotkey('right', lambda: change(2))
  keyboard.add_hotkey('space', lambda: change(1))

  while True:
    if (directionFlag == 0) and (pos != 0):
      pos -= 1
    elif (directionFlag == 2) and (pos != (length - len(std))):
      pos += 1

    print('|' + ' '*(pos) + std + ' '*(length - pos - len(std)) + '|')
    print('\033[1A', end = '\x1b[2k')

    time.sleep(0.05)


if __name__ == '__main__':
  driving_car()