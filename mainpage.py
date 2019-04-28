import time
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
    def buttondown(*args):
        print(*args)

    def __init__(self, master=None):
        Canvas.__init__(self, master)
        self.bind("<Button-1>", self.buttondown)
    

class App(AppBase):
    def create(self):
        self.Canvas = Area(self)
        self.Canvas.grid(row=0, column=0, rowspan=7, sticky = N+E+S+W)
        self.Canvas.update()
        self.Canvas.bind("<Configure>", self.create_area)
        self.create_buttons()

    def create_buttons(self):
        self.Start = Button(self, text="Start")
        self.Start.grid(row=1, column=1, sticky=E+W, padx=5, pady=7)
        self.Stop = Button(self, text="Stop")
        self.Stop.grid(row=2, column=1, sticky=E+W, padx=5, pady=7)
        self.Step = Button(self, text="Step")
        self.Step.grid(row=3, column=1, sticky=E+W, padx=5, pady=7)
        self.Clear = Button(self, text="Clear")
        self.Clear.grid(row=4, column=1, sticky=E+W, padx=5, pady=7)
        self.AddPattern = Button(self, text="AddPattern")
        self.AddPattern.grid(row=5, column=1, sticky=E+W, padx=5, pady=7)


    def create_area(self, event):
        area_width = self.Canvas.winfo_width()
        area_height = self.Canvas.winfo_height()
        delta_x = int((area_width-5)/50)
        start_x = 2
        finish_x = area_width-3
        delta_y = int((area_height-5)/30)
        start_y = 2
        finish_y = area_height-3
        self.Canvas.create_rectangle(start_x, start_y, finish_x, finish_y, fill='white')
        for x in range(start_x+delta_x, finish_x, delta_x):
            self.Canvas.create_line(x, start_y+1, x, finish_y, fill='lightgray')
        for y in range(start_y+delta_y, finish_y, delta_y):
            self.Canvas.create_line(start_x+1, y, finish_x, y, fill='lightgray')



Tick = App()
Tick.mainloop()
