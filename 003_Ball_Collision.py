import time

def collision(ball2_position: int = 20):
  data = [' ' for _ in range(ball2_position + 1 + 10)]

  def animate(from_pos: int, to_pos: int, t: float = 0.1):
    for newpos in range(from_pos, to_pos):
      data[newpos - 1] = ' '
      data[newpos] = 'O'

      print('\033[1A', end = '\x1b[2k')
      print(''.join(data))
      time.sleep(t)


  data[ball2_position] = 'O'
  data[0] = 'O'
  print(''.join(data))

  animate(1, ball2_position, 0.005+(ball2_position/100))
  animate(ball2_position + 1, len(data), 0.1+(len(data) - ball2_position)/100)

if __name__ == '__main__':
  collision()