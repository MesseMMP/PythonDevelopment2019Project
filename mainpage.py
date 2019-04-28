import time
from tkinter import *
from threading import Thread, Event

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

class AppBase(Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.master.rowconfigure(0, weight = 1)
        self.master.rowconfigure(6, weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.grid()
        self.create()

    def start(self):
        self.Clock.start()

    def quit(self, *events):
        self.Clock.done.set()
        self.master.quit()

class Area(Canvas):
    def buttondown(*args):
        print(*args)

    def __init__(self, master=None):
        Canvas.__init__(self, master)
        self.bind("<Button-1>", self.buttondown)

class App(AppBase):
    def create(self):
        self.Canvas = Area(self)
        self.Canvas.grid(row=0, column=0, sticky = N+E+S+W, rowspan=7)
        self.create_buttons()

    def create_buttons(self):
        self.Start = Button(text="Start")
        self.Start.grid(row=1, column=1, sticky=E+W, padx=5, pady=7)
        self.Stop = Button(text="Stop")
        self.Stop.grid(row=2, column=1, sticky=E+W, padx=5, pady=7)
        self.Step = Button(text="Step")
        self.Step.grid(row=3, column=1, sticky=E+W, padx=5, pady=7)
        self.Clear = Button(text="Clear")
        self.Clear.grid(row=4, column=1, sticky=E+W, padx=5, pady=7)
        self.AddPattern = Button(text="AddPattern")
        self.AddPattern.grid(row=5, column=1, sticky=E+W, padx=5, pady=7)


Tick = App()
Tick.mainloop()
