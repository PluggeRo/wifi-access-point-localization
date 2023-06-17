import tkinter as tk
from MainPage import PageOne
from ControlPage import PageTwo


class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.title("IFITEX")
        #self.attributes('-fullscreen', True)

        self.frames = {}
        for F in (PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PageOne")

        # Set window size and background
        self.minsize(800, 480)
        self.maxsize(800, 480)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


app = MainApplication()
app.mainloop()
