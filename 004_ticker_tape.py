import time
def ticker_tape(message: str):
  print('<-- left  :   space stop  :  right -->')
  message = '<---- ' + message + ' ---->'
  message = message + ' '*len(message)

  while True:
    message = message[-1] + message[:-1]
    print(message)
    print('\033[1A', end = '\x1b[2k')

    time.sleep(0.05)


if __name__ == '__main__':
  ticker_tape('I like to play with python')