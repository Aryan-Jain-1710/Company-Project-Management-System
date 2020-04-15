from tkinter import *
import sqlite3
import About_Us
import Add_Project
import  Show_Project
from ttkthemes import themed_tk as tk
from tkinter import ttk

class Logged_In(Toplevel):

    def __init__(self):

        Toplevel.__init__(self)
        self.title("LADDERRISE")
        self.geometry("650x650+680+20")
        self.iconbitmap()
        self.resizable(False, False)

        # FRAMES
        self.top = Frame(self, height=150, bg="#FFF3F3")
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg="#FFD28E")
        self.bottom.pack(fill=X)

        # TITLE
        self.title_lbl = Label(self.top, text="MEMBER PORTAL", font="Broadway 50 bold", fg="#BD2312", bg="#FFF3F3")
        self.title_lbl.place(x=4, y=20)

        # PROJECT BUTTON
        self.show_project_btn = ttk.Button(self.bottom, text = "Show Projects", width = 18, command = self.show_project_pressed)
        self.show_project_btn.place(x=260, y=50)

        self.add_project_btn = ttk.Button(self.bottom, text = "Add Project", width = 18, command = self.add_project_pressed)
        self.add_project_btn.place(x=260, y=110)

        self.about_us_btn = ttk.Button(self.bottom, text = "About Us", width = 18, command = self.about_us_pressed)
        self.about_us_btn.place(x=260, y=170)


    def about_us_pressed(self):

        about_us = About_Us.About_us()
        self.destroy()

    def add_project_pressed(self):

        add_project = Add_Project.Add_Project()
        self.destroy()

    def show_project_pressed(self):

        show_project = Show_Project.Show_project()