from tkinter import *
from ttkthemes import themed_tk as tk
from tkinter import ttk

class About_us(Toplevel):

    def __init__(self):

        Toplevel.__init__(self)
        self.title("COMPANY")
        self.geometry("650x650+680+20")
        self.iconbitmap()
        self.resizable(False, False)

        # FRAMES
        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg="#FABC5F")
        self.bottom.pack(fill=X)

        # TITLE
        self.title_lbl = Label(self.top, text="ABOUT US", font="Broadway 60 bold", fg="#BD2312", bg="white")
        self.title_lbl.place(x=100, y=20)

        #INFO ABOUT COMPANY
        self.title_info = Label(self.bottom, text="Company is an end to end solutions company. Our endeavor is to offer a hassle free experience in the areas of design, project supervision, execution and much more.", font="Gothem 12 bold", fg="#B07F1C", bg="#FABC5F", wraplength = 560,)
        self.title_info.place(x=50, y=30)