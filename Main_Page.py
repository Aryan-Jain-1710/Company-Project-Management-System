from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import datetime
import Logged_In
from ttkthemes import themed_tk as tk


connection = sqlite3.connect("Company.db")
crsr = connection.cursor()

date = datetime.datetime.now().date()
list_usernames = [""]
list_passwords = ['']

class Application( object ):

    def __init__(self, master):
        self.master = master

        #FRAMES
        self.top = Frame(master, height=400, bg ="#FFF3F3")
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=250, bg="#FFD28E")
        self.bottom.pack(fill=X)


        # #LOGO
        # self.top_image = PhotoImage(file="pics/logo.png")
        # self.top_image_lbl = Label(self.top, image=self.top_image, bg="white")
        # self.top_image_lbl.place(x=10, y=10)

        #TITLE
        self.title_lbl = Label(self.top, text = "COMPANY", font = "Broadway 60 bold", fg = "#BD2312", bg = "#FFF3F3")
        self.title_lbl.place(x=40,y=140)

        #DATE
        self.date_today = Label(self.top, text = "Today's date is: " + str(date), font = "Georgia 10 bold", fg = "#7C150A", bg = "#FFF3F3" )
        self.date_today.place(x=440, y=0)

        #INFO ABOUT COMPANY
        self.title_info = Label(self.top, text="Company is an end to end solutions company. Our endeavor is to offer a hassle free experience in the areas of design, project supervision, execution and much more.", font="Courier 12 bold", fg="#B07F1C", bg="#FFF3F3", wraplength = 560,)
        self.title_info.place(x=40, y=240)

        #LOG IN
        self.log_in_lbl = Label(self.bottom, text="Member Portal", bg = "#FFD28E", fg = "#767171",  font="broadway 25")
        self.log_in_lbl.place(x=190, y=20)

        # self.username_lbl = Label(self.bottom, text="Username: ", bg="#FABC5F")
        # self.username_lbl.place(x=10, y=35)
        #

        self.username_ety = ttk.Entry(self.bottom, width=40)
        self.username_ety.insert(0, "Please enter the username")
        self.username_ety.place(x=200, y=80)

        # self.password_lbl = Label(self.bottom, text="Password: ", bg="#FABC5F")
        # self.password_lbl.place(x=10, y=65)

        self.password_ety = ttk.Entry(self.bottom, width=40)
        self.password_ety.insert(0, "Please enter the password")
        self.password_ety.place(x=200, y=110)

        self.login_btn = ttk.Button(self.bottom, text = "Log In",  width = 10 , command = self.openloggedin)
        self.login_btn.place(x=370, y=140)

    def openloggedin(self):

        username = self.username_ety.get()
        password = self.password_ety.get()

        if username.lower() in list_usernames and password.lower() in list_passwords:

            messagebox.showinfo("Success", "You have successfully logged in", icon="info")
            log_in = Logged_In.Logged_In()


        else:
            messagebox.showerror("Error", "Incorrect username or password \nYou cannot login", icon="warning")




def main():
    root = tk.ThemedTk()
    root.get_themes()
    root.set_theme("arc")
    app = Application(root)
    root.title("Company")
    root.geometry("650x650+25+20")
    root.iconbitmap()
    root.resizable(False, False)
    root.mainloop()

if __name__ == "__main__":
    main()
