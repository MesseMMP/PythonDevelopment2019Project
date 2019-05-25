class GameMatrix:
    def __init__(self, rows=200, columns=200):
        self.rows = rows
        self.columns = columns
        self._alive = dict()
        self.dead = set()

    def __getitem__(self, position):
        row, column = position
        return (
            row > 0
            and row < self.rows
            and column > 0
            and column < self.columns
            and (row, column) in self._alive.keys()
        )

    def __setitem__(self, position, value):
        row, column = position
        if row < 0 or row > self.rows or column < 0 or column > self.columns:
            return
        if value:
            self._alive[row, column] = value
        else:
            self._alive.pop((row, column))

    def make_step(self):
        self.dead = set()
        new_alive = self.alive
        for cell in self._alive.keys():
            alive_neighbours = self.alive_neighbours(cell)
            if len(alive_neighbours) < 2 or len(alive_neighbours) > 3:
                new_alive.pop(cell)
                self.dead.add(cell)
        for cell in self.all_dead_neighbours:
            alive_neighbours = self.alive_neighbours(cell)
            if (
                    len(alive_neighbours) == 3
                    and cell[0] > 0
                    and cell[0] < self.rows
                    and cell[1] > 0
                    and cell[1] < self.columns
                ):
                neighbour_elections = set()
                for neighbour in alive_neighbours:
                    cur_color = self._alive[neighbour]
                    if cur_color in neighbour_elections:
                        new_alive[cell] = cur_color
                        break
                    else:
                        neighbour_elections.add(cur_color)
        self._alive = new_alive

    @property
    def alive(self):
        return self._alive.copy()

    @property
    def all_dead_neighbours(self):
        res = set()
        for cell in self._alive.keys():
            res = res | self.dead_neighbours(cell)
        return res

    def alive_neighbours(self, cell):
        return self.neighbours(cell) & self._alive.keys()

    def dead_neighbours(self, cell):
        return self.neighbours(cell) - self._alive.keys()

    def neighbours(self, cell):
        row, column = cell
        return {
            (row, column - 1),
            (row - 1, column),
            (row - 1, column - 1),
            (row, column + 1),
            (row + 1, column),
            (row + 1, column + 1),
            (row - 1, column + 1),
            (row + 1, column - 1),
        }
