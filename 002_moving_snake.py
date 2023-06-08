import time
if __name__ == '__main__':
  snake = '>===0-'
  while True:
    snake = f' {snake}'
    print(snake)
    
    print('\033[1A', end = '\x1b[2k')
    time.sleep(0.05)