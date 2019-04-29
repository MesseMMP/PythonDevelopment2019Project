import time
import logic as lg
from tkinter import *
from threading import Thread, Event
'''
class Clock(Thread):
    def __init__(self, root, grain=1, event="<<Tick>>"):
        super().__init__()
        self.root = root    # Окно, которому посылать событие
        self.grain = grain  # Размер одного тика в секундах (м. б дробный)
        self.event = event  # TKinter-событие, которое надо посылать
        self.done = Event() # threading-событие, которое останавливет тред

    def run(self):
        while not self.done.wait(self.grain):
            self.root.event_generate(self.event)
            '''

class AppBase(Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.grid(sticky=N+E+S+W)
        self.rowconfigure(0, weight=2)
        self.rowconfigure(6, weight=2)
        self.columnconfigure(0, weight=2)
        self.create()

'''
    def start(self):
        self.Clock.start()

    def quit(self, *events):
        self.Clock.done.set()
        self.master.quit()
'''
class Area(Canvas):
    def buttondown(self, event):
        left_border_cell = event.x
        top_border_cell = event.y
        while (left_border_cell - self.start_x) % self.delta_x:
            left_border_cell -= 1
        while (top_border_cell - self.start_y) % self.delta_y:
            top_border_cell -= 1
        row = (top_border_cell - self.start_y) // self.delta_y
        column = (left_border_cell - self.start_x) // self.delta_x
        if matrix_grid[row][column]:
            matrix_grid[row][column] = 0
            self.create_rectangle(left_border_cell+1, top_border_cell+1, \
                left_border_cell+self.delta_x-1, top_border_cell+self.delta_y-1, fill='white',outline='white')
        else:
            matrix_grid[row][column] = 1
            self.create_rectangle(left_border_cell+1, top_border_cell+1, \
                left_border_cell+self.delta_x-1, top_border_cell+self.delta_y-1, fill='black')




    def __init__(self, master=None):
        Canvas.__init__(self, master)
        self.bind("<Button-1>", self.buttondown)  
        self.delta_x = 15
        self.delta_y = 15 
        self.start_x = 2
        self.start_y = 2

    def create_grid(self):
        self.area_width = COLUMN_MATRIX*self.delta_x
        self.area_height = ROW_MATRIX*self.delta_y
        self.finish_x = self.area_width-3
        self.finish_y = self.area_height-3
        self.create_rectangle(self.start_x, self.start_y, self.finish_x, self.finish_y, fill='white', outline='white')
        for x in range(self.start_x+self.delta_x, self.finish_x, self.delta_x):
            self.create_line(x, self.start_y+1, x, self.finish_y, fill='lightgray')
        for y in range(self.start_y+self.delta_y, self.finish_y, self.delta_y):
            self.create_line(self.start_x+1, y, self.finish_x, y, fill='lightgray') 


    def draw_cells(self, matrix):
        for row, row_cells in enumerate(matrix):
            for col, cell in enumerate(row_cells):
                if cell:
                    self.create_rectangle(self.start_x+col*self.delta_x+1, self.start_y+row*self.delta_y+1, \
                        self.start_x+(col+1)*self.delta_x-1, self.start_y+(row+1)*self.delta_y-1, fill='black')
                else:
                    self.create_rectangle(self.start_x+col*self.delta_x+1, self.start_y+row*self.delta_y+1, \
                        self.start_x+(col+1)*self.delta_x-1, self.start_y+(row+1)*self.delta_y-1, fill='white',outline='white')


    def draw_cells_life_dead(self, life, dead):
        for row, col in life:
            self.create_rectangle(self.start_x+col*self.delta_x+1, self.start_y+row*self.delta_y+1, \
                self.start_x+(col+1)*self.delta_x-1, self.start_y+(row+1)*self.delta_y-1, fill='black')
        for row, col in dead:
            self.create_rectangle(self.start_x+col*self.delta_x+1, self.start_y+row*self.delta_y+1, \
                self.start_x+(col+1)*self.delta_x-1, self.start_y+(row+1)*self.delta_y-1, fill='white',outline='white')
    

class App(AppBase):
    def create(self):
        self.Canvas = Area(self)
        self.Canvas.grid(row=0, column=0, rowspan=7, sticky = N+E+S+W)
        self.Canvas.update()
        self.Canvas.create_grid()
        self.create_buttons()


    def create_buttons(self):
        self.Start = Button(self, text="Start")
        self.Start.grid(row=1, column=1, sticky=E+W, padx=5, pady=7)
        self.Stop = Button(self, text="Stop")
        self.Stop.grid(row=2, column=1, sticky=E+W, padx=5, pady=7)
        self.Step = Button(self, text="Step", command=self.one_step)
        self.Step.grid(row=3, column=1, sticky=E+W, padx=5, pady=7)
        self.Clear = Button(self, text="Clear")
        self.Clear.grid(row=4, column=1, sticky=E+W, padx=5, pady=7)
        self.AddPattern = Button(self, text="AddPattern")
        self.AddPattern.grid(row=5, column=1, sticky=E+W, padx=5, pady=7)


    def one_step(self):
        global matrix_grid
        life_list, dead_list, matrix_grid = lg.one_step_life_dead(matrix_grid)
        self.Canvas.draw_cells_life_dead(life_list, dead_list)


ROW_MATRIX = 150
COLUMN_MATRIX = 200


matrix_grid = [[0 for i in range(COLUMN_MATRIX)] for j in range(ROW_MATRIX)]

Tick = App()
Tick.mainloop()

