import math

class Terminal:
  def clear_lines(lines: int) -> None:
    for _ in range(lines):
      print('\033[1A', end = '\x1b[2k')

  def status_stdout(ratio: int | float, args: tuple = None) -> None:
    max_progression_line = 10
    print('\n'.join([
      '-'*round(ratio * max_progression_line) + f' {ratio*100:.2f}%',
      (args and ('Plotting %s to %s' % args)) or ''
    ]))

class Coordinate:
  def __init__(self, x: int, y: int) -> None:
    self.x = x
    self.y = y

  def __str__(self) -> str:
    return f'({self.x}, {self.y})'

class Canvas:
  def __init__(self, size: Coordinate, scale: Coordinate) -> None:
    """
    #### :param size: Coordinate
    #### :param scale Coordinate
    """
    self.start = None
    self.size = size
    self.scale = scale
    self.plot_points: list = [[] for _ in range(size.y)]

  def _y_to_index(self, yValue: float) -> int:
    return round((1 - yValue) * self.scale.y)
  
  def _x_to_index(self, xValue: float) -> int:
    return round((xValue - self.start.x) * (self.scale.x))

  def add_plot_point(self, cord: Coordinate) -> Coordinate:
    """
    #### :param cord: Coordinate
    #### :return Coordinate
      - where the point was plotted to on the canvas
    """
    if not self.start: self.start = cord
    index = Coordinate(self._x_to_index(cord.x), self._y_to_index(cord.y))
    self.plot_points[index.y].append(index.x)

    return index

  def draw(self) -> list:
    graph = [
      ''.join([
        ( ((i) in self.plot_points[y]) and '*' ) or ' '#or ( (y == ((self.size.y // 2))) and '-' ) or ' '
        for i in range(self.size.x + 1)
      ])
      for y in range(self.size.y)
    ]# list[str, ...]

    #draw prefix and suffix
    _prefix = [f'{i/10:.1f}' for i in range(10, -11, -1)]
    largest_prefix = len(max(_prefix, key = len))
    prefixes = [' '*(largest_prefix - len(i)) + i for i in _prefix]

    for y, y_line in enumerate(graph):
      graph[y] = f'{prefixes[y]} {y_line} |'



    return ['Sine Graph'] + graph



  def stdout(self) -> None:
    with open('result.txt', 'w') as file:
      file.writelines('\n'.join(self.draw()))
    print('Drew graph to results.txt')





def draw(x1: float, x2: float, scale: Coordinate):
  """
  #### :param x1: float
    -x0 value
  #### :param x2: flaot
    -x1 value
  #### :param scale: int
    -How many spaces 1pi is equal to on both axises
  """
  if x2 <= x1: raise ValueError('Invalid X-value range')
  x1, x2 = round(x1, 1), round(x2, 1)

  new_canvas = Canvas(Coordinate(
    x = (x2 - x1)*scale.x,
    y = (2 * scale.y) + 1
  ), scale)

  p1 = x1
  while p1 < x2:
    to_plot = Coordinate(
      p1,
      math.sin(p1 * math.pi)
    )
    canvas_plot_point = new_canvas.add_plot_point(to_plot)

    #stdout
    Terminal.status_stdout(
      p1/x2,
      (
        to_plot,
        canvas_plot_point
      )
    )
    Terminal.clear_lines(2)
    p1 += 0.025

  Terminal.status_stdout(1)
  new_canvas.stdout()


if __name__ == '__main__':
  draw(0, 2, Coordinate(40, 10))