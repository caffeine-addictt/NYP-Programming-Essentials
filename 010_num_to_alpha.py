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
  alpha = (
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
  )
  special = {
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirthy',
    '40': 'fourty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety'
  }
  suffix = (
    '',
    '',
    'hundred',
    'thousand'
  )

  while True:
    number = persistent_input(
      'Enter a number (0 to end): ',
      [
        ('Opps. Please enter an integer. Try again.', lambda x: is_integer(x)),
        ('Oops. This is out of my range. Try again.', lambda x: int(x) < 10**6)
      ]
    )

    if number == '0':
      print('Goodbye')
      break

    #       hundreds  tens   ones
    #split = ['000', '000', '000']
    split = []
    while number:
      split.append(number[-3:])
      number = number[:-3]

    cache = []
    for suffix_i, n in enumerate(reversed(split)):
      hundreds_reppresentation = []
      n = '0'*((len(n) % 3) - 1) + n

      if n[0] != '0':
        hundreds_reppresentation.append(alpha[int(n[0]) - 1] + ' hundred')

      hundreds_reppresentation.append(
        ((n[-2:] in special) and special[n[-2:]]) or
        ' '.join([num for num in [
          (n[1] != '0') and special[n[1] + '0'],
          (n[2] != '0' and alpha[int(n[2]) - 1])
        ] if num])
      )

      num_block = (
        (
          (len(hundreds_reppresentation) > 1) and
          (', '.join(hundreds_reppresentation[:-1]) + ' and ' + hundreds_reppresentation[-1])
        ) or
        hundreds_reppresentation[0]
      )
      cache.append(
        num_block +
        ((len(suffix) > suffix_i*3) and suffix[suffix_i*3]) or ''
      )

    stdout = ', '.join([item for item in cache[:-1] if item])
    if cache[-1] in suffix:
      stdout += ' ' + cache[-1]
    else:
      stdout += ((stdout and ', ') or '') + cache[-1]

    print(stdout)
