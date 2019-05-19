class GameMatrix:
    def __init__(self, rows=200, columns=200):
        self.rows = rows
        self.columns = columns
        self._alive = set()
        self.died = set()

    def __getitem__(self, position):
        row, column = position
        return (
            row > 0
            and row < self.rows
            and column > 0
            and column < self.columns
            and (row, column) in self._alive
        )

    def __setitem__(self, position, value):
        row, column = position
        if row < 0 or row > self.rows or column < 0 or column > self.columns:
            return
        if value is True:
            self._alive.add((row, column))
        elif value is False:
            self._alive.discard((row, column))

    def make_step(self):
        self.died = set()
        new_alive = self.alive
        for cell in self._alive:
            alive_neighbours = self.alive_neighbours(cell)
            if len(alive_neighbours) < 2 or len(alive_neighbours) > 3:
                new_alive.remove(cell)
                self.died.add(cell)
        for cell in self.all_dead_neighbours:
            alive_neighbours = self.alive_neighbours(cell)
            if (
                len(alive_neighbours) == 3
                and cell[0] > 0
                and cell[0] < self.rows
                and cell[1] > 0
                and cell[1] < self.columns
            ):
                new_alive.add(cell)
        self._alive = new_alive

    @property
    def alive(self):
        return self._alive.copy()

    @property
    def all_dead_neighbours(self):
        res = set()
        for cell in self._alive:
            res = res | self.dead_neighbours(cell)
        return res

    def alive_neighbours(self, cell):
        return self.neighbours(cell) & self._alive

    def dead_neighbours(self, cell):
        return self.neighbours(cell) - self._alive

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
