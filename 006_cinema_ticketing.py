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
  total_price = 0
  total_tickets = 0

  while True:
    ticket_price = int(persistent_input(
      'Enter price of ticket ($8, $10 or $12): ',
      [
        ('Oops. Please input a number only.', lambda x: x.isnumeric()),
        ('Oops. No such ticket. Try again.', lambda x: x in ['0', '8', '10', '12'])
      ]
    ))

    if ticket_price == 0:
      response = persistent_input(
        'Are you sure you want to end ticketing (y/n)? ',
        [('Only enter "n" or "y"!', lambda x: x in ['n', 'y'])]
      )
      if response == 'n':
        print('')
        continue
      else: break

    ticket_num = int(persistent_input(
      'Enter number of tickets: ',
      [('Oops. Please input a number only.', lambda x: x.isnumeric())]
    ))

    price = ticket_price * ticket_num

    total_price += price
    total_tickets += ticket_num
    print('Please pay $%s for %s tickets' % (
      ticket_price * ticket_num,
      ticket_num
    ), end = '\n\n')
  

  print("""
  Summary of Cinema Ticket Sales
  You sold %s tickets.
  Total sales is $%s.
  Goodbye.
  """ % (
    total_tickets,
    total_price
  ))