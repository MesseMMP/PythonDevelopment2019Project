class GameMatrix:
    """Representation of Game of Life's grid

    Object of this class allows to check whether or not certain cell is
    alive, add and remove alive cells, and update a grid according to game's
    rules


    Attributes
    ----------
    rows: int
        Number of rows in a grid
    columns: int
        Number of columns in a grid
    alive: dict
        Dictionary of all alive cells in a grid with their positions as keys
        and their colors as values
    dead: set
        Set of all dead cells that died during the latest game step
    all_dead_neighbours: set
        Set of all dead cells which are neighbours of some of alive cells

    Methods
    -------
    make_step()
        Makes one step of a game
    neighbours(cell)
        Returns a set of all neighbours of a cell
    alive_neighbours(cell)
        Returns a set of all alive neighbours of a cell
    dead_neighbours(cell)
        Returns a set of all dead neighbours of a cell
    """

    def __init__(self, rows=200, columns=200):
        """
        Parameters
        ----------
        rows: int
            Number of rows in a grid
        columns: int
            Number of columns in a grid
        """

        self.rows = rows
        self.columns = columns
        self._alive = dict()
        self.dead = set()

    def __getitem__(self, position):
        """
        Parameters
        ----------
        position: tuple of int
            Position (row, column) of a cell
        """

        row, column = position
        return (
            row > 0
            and row < self.rows
            and column > 0
            and column < self.columns
            and (row, column) in self._alive.keys()
        )

    def __setitem__(self, position, value):
        """
        Parameters
        ----------
        position: tuple of int
            Position (row, column) of a cell
        value: str or False
            Value to assign to a cell with specified position
        """

        row, column = position
        if row < 0 or row > self.rows or column < 0 or column > self.columns:
            return
        if value:
            self._alive[row, column] = value
        else:
            self._alive.pop((row, column))

    def make_step(self):
        """Process one step of a game changing sets of alive and dead cells
        """

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
        """
        Parameters
        ----------
        cell: tuple of int
            Cell coordinates (row, column)
        
        Returns
        -------
        set of tuples of int
            Set of all alive neighbours of specified cell
        """

        return self.neighbours(cell) & self._alive.keys()

    def dead_neighbours(self, cell):
        """
        Parameters
        ----------
        cell: tuple of int
            Cell coordinates (row, column)
        
        Returns
        -------
        set of tuples of int
            Set of all dead neighbours of specified cell
        """

        return self.neighbours(cell) - self._alive.keys()

    def neighbours(self, cell):
        """
        Parameters
        ----------
        cell: tuple of int
            Cell coordinates (row, column)
        
        Returns
        -------
        set of tuples of int
            Set of all neighbours of specified cell
        """

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
