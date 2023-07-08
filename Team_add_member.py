from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import Combobox
from tkinter import messagebox
from Add_Project import *
from ttkthemes import themed_tk as tk
from tkinter import ttk


connection = sqlite3.connect("company.db")
crsr = connection.cursor()



class Add_member(Toplevel):

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
        self.title_lbl = Label(self.top, text="ADD MEMBER", font="Broadway 60 bold", fg="#BD2312", bg="white")
        self.title_lbl.place(x=40, y=20)

        # Name of the Member
        self.member_name_lbl = Label(self.bottom, text="Name of the Member : ", bg="#FABC5F")
        self.member_name_lbl.place(x=10, y=10)

        self.member_name_ety = ttk.Entry(self.bottom, width=40)
        self.member_name_ety.insert(0, 'Please enter the name of the Member')
        self.member_name_ety.place(x=170, y=10)

        # DOB of the member
        self.member_dob_lbl = Label(self.bottom, text="Date of Birth of the Member : ", bg="#FABC5F")
        self.member_dob_lbl.place(x=10, y=50)

        self.member_dob_ety = ttk.Entry(self.bottom, width=40)
        self.member_dob_ety.insert(0, 'Please enter the Date of Birth of the Member')
        self.member_dob_ety.place(x=170, y=50)

        # Gender of the Member
        self.member_gender_lbl = Label(self.bottom, text="Gender of the Member : ", bg="#FABC5F")
        self.member_gender_lbl.place(x=10, y=90)

        self.member_gender_combobox = ttk.Combobox(self.bottom, textvariable = "gender", values = ('Male', "Female"), state = 'readonly', width = 40)
        self.member_gender_combobox.place(x=170, y=90)

        # Role of the member
        self.member_role_lbl = Label(self.bottom, text="Job of the Member : ", bg="#FABC5F")
        self.member_role_lbl.place(x=10, y=130)

        self.member_role_combobox = ttk.Combobox(self.bottom, textvariable = "Job", values = ('Manager', "Carpenter", "Designer"), state = 'readonly', width = 40)
        self.member_role_combobox.place(x=170, y=130)

        # Address of the Member
        self.member_address_lbl = Label(self.bottom, text="Address of the Member : ", bg="#FABC5F")
        self.member_address_lbl.place(x=10, y=170)

        self.member_address_ety = Text(self.bottom, width=30, height = 10, wrap = WORD)
        self.member_address_ety.place(x=170, y=170)

        # Button to finally add
        self.add_btn = ttk.Button(self.bottom, text="Add", width =8, command=self.save_member)
        self.add_btn.place(x=350, y=350)

    def save_member(self):

        member_name = self.member_name_ety.get()
        member_dob = self.member_dob_ety.get()
        member_gender = self.member_gender_combobox.get()
        member_role = self.member_role_combobox.get()
        member_address = self.member_address_ety.get(1.0, "end-1c")
        project_name = self.project_name_ety.get()
        print(project_name)

        if (member_name and member_dob and member_gender and member_role and member_address) != "":
            try:
                query = "INSERT INTO  'Project_Team' (Member_name, Member_dob, Member_gender, Member_role, Member_address) VALUES(?,?,?,?,?)"
                crsr.execute(query, (member_name, member_dob, member_gender, member_role, member_address))
                connection.commit()
                messagebox.showinfo("Success", "Successfully added to database", icon="info")

            except:
                messagebox.showerror("Error", "Can't add to database", icon="warning")
        else:
            messagebox.showerror("Error", "Fields can't be empty", icon="warning")