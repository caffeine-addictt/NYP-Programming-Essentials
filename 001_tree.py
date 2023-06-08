def draw(height: int) -> None:
  tbl = []
  leaves = height*2 // 3
  trunk = height // 3

  leaves_largest = leaves*2 + 1
  for i in range(leaves + 1):
    floating_spaces = ((leaves_largest - (i*2+1)) // 2)*' '
    tbl.append(floating_spaces + '*'*(i*2+1) + floating_spaces)

  largest_trunk = min(leaves_largest, 3)
  floating_spaces = ((leaves_largest - largest_trunk) // 2)*' '
  trunk_line = floating_spaces + '|'*largest_trunk + floating_spaces

  stdout = '\n'.join(tbl + [trunk_line]*trunk)
  print(stdout)

draw(2)