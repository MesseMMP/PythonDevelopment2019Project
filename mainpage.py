import logic as lg
from tkinter import Frame, Canvas, N, E, S, W, Button


class AppBase(Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=N + E + S + W)
        self.rowconfigure(0, weight=2)
        self.rowconfigure(6, weight=2)
        self.columnconfigure(0, weight=2)
        self.create()

    def create(self):
        raise NotImplementedError


class GameGrid(Canvas):
    def __init__(self, master=None, rows=200, columns=200):
        Canvas.__init__(self, master)
        self.bind("<Button-1>", self.click_cell)
        self.bind("<B1-Motion>", self.hold_down_cell)
        self.cell_width = 15
        self.cell_height = 15
        self.rows = rows
        self.columns = columns
        self.matrix = [[0 for i in range(columns)] for j in range(rows)]
        self.last_drawn_cell = None
        self._create_grid()

    def click_cell(self, event):
        top_border = event.y - event.y % self.cell_height
        left_border = event.x - event.x % self.cell_width
        row = top_border // self.cell_height
        column = left_border // self.cell_width
        if self.matrix[row][column]:
            self.matrix[row][column] = 0
            self._draw_dead_cell(row, column)
        else:
            self.matrix[row][column] = 1
            self._draw_alive_cell(row, column)

    def hold_down_cell(self, event):
        top_border = event.y - event.y % self.cell_height
        left_border = event.x - event.x % self.cell_width
        row = top_border // self.cell_height
        column = left_border // self.cell_width
        if not self.matrix[row][column]:
            self.matrix[row][column] = 1
            self._draw_alive_cell(row, column)

    def _create_grid(self):
        self.grid_width = self.columns * self.cell_width
        self.grid_height = self.rows * self.cell_height
        self.create_rectangle(
            0,
            0,
            self.grid_width,
            self.grid_height,
            fill="white",
            outline="white",
        )
        for x in range(
            self.cell_width, self.grid_width, self.cell_width
        ):
            self.create_line(
                x, 0, x, self.grid_height, fill="lightgray"
            )
        for y in range(
            self.cell_height, self.grid_height, self.cell_height
        ):
            self.create_line(
                0, y, self.grid_width, y, fill="lightgray"
            )

    def make_step(self):
        alive_cells, dead_cells, self.matrix = lg.one_step_life_dead(
            self.matrix
        )
        for row, column in alive_cells:
            self._draw_alive_cell(row, column)
        for row, column in dead_cells:
            self._draw_dead_cell(row, column)

    def clear(self):
        for row, row_cells in enumerate(self.matrix):
            for column, cell in enumerate(row_cells):
                self.matrix[row][column] = 0
                if cell:
                    self._draw_dead_cell(row, column)

    def _draw_alive_cell(self, row, column):
        self.create_rectangle(
            column * self.cell_width + 1,
            row * self.cell_height + 1,
            (column + 1) * self.cell_width - 1,
            (row + 1) * self.cell_height - 1,
            fill="black",
        )

    def _draw_dead_cell(self, row, column):
        self.create_rectangle(
            column * self.cell_width + 1,
            row * self.cell_height + 1,
            (column + 1) * self.cell_width - 1,
            (row + 1) * self.cell_height - 1,
            fill="white",
            outline="white",
        )


class App(AppBase):
    def create(self):
        self.game_grid = GameGrid(self)
        self.game_grid.grid(row=0, column=0, rowspan=7, sticky=N + E + S + W)
        self.create_buttons()

    def create_buttons(self):
        self.start_button = Button(self, text="Start")
        self.start_button.grid(row=1, column=1, sticky=E + W, padx=5, pady=7)
        self.stop_button = Button(self, text="Stop")
        self.stop_button.grid(row=2, column=1, sticky=E + W, padx=5, pady=7)
        self.step_button = Button(self, text="Step", command=self.one_step)
        self.step_button.grid(row=3, column=1, sticky=E + W, padx=5, pady=7)
        self.clear_button = Button(self, text="Clear", command=self.clear)
        self.clear_button.grid(row=4, column=1, sticky=E + W, padx=5, pady=7)
        self.add_pattern_button = Button(self, text="AddPattern")
        self.add_pattern_button.grid(
            row=5, column=1, sticky=E + W, padx=5, pady=7
        )

    def one_step(self):
        self.game_grid.make_step()

    def clear(self):
        self.game_grid.clear()


if __name__ == "__main__":
    Tick = App()
    Tick.mainloop()
