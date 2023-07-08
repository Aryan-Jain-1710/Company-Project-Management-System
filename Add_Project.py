from tkinter import *
import sqlite3
import Team_add_member
import Inventory_add
from tkinter import messagebox
from tkinter.ttk import Combobox
from ttkthemes import themed_tk as tk
from tkinter import ttk


connection = sqlite3.connect("Company.db")
crsr = connection.cursor()


class Add_Project(Toplevel):

    def __init__(self):

        Toplevel.__init__(self)
        self.title("COMPANY")
        self.geometry("1000x650+300+20")
        self.iconbitmap()
        self.resizable(False, False)

        # FRAMES
        self.top = Frame(self, height=125, bg="white")
        self.top.pack(fill=X)

        self.middle = Frame(self, height=60, bg="#FABC5F")
        self.middle.pack(fill=X)

        self.bottom_left = Frame(self, height = 232.5, width = 500, bg="#DFDEDE")
        self.bottom_left.pack(fill = Y, side=LEFT)

        self.bottom_right = Frame(self, height = 232.5, width = 500, bg="#E9E8E8")
        self.bottom_right.pack(fill=Y, side=RIGHT)


        # TITLE
        self.title_lbl = Label(self.top, text="ADD PROJECT", font="Broadway 60 bold", fg="#BD2312", bg="white")
        self.title_lbl.place(x=40, y=10)

        # NAME
        self.project_name_lbl = Label(self.middle, text = "Name of the Project: ", bg = "#FABC5F")
        self.project_name_lbl.place(x=10, y=20)

        self.project_name_ety = ttk.Entry(self.middle, width=40)
        self.project_name_ety.insert(0, 'Please enter the name of the Project')
        self.project_name_ety.place(x=140, y=20)







        #TEAM MEMBER
        self.team_member_lbl = Label(self.bottom_left, text = "TEAM", bg = "#DFDEDE", font = "Broadway 35" )
        self.team_member_lbl.place(x=150,y=10)

        # Name of the Member
        self.member_name_lbl = Label(self.bottom_left, text="Name of the Member : ", bg="#DFDEDE")
        self.member_name_lbl.place(x=10, y=80)

        self.member_name_ety = ttk.Entry(self.bottom_left, width=40)
        self.member_name_ety.insert(0, 'Please enter the name of the Member')
        self.member_name_ety.place(x=170, y=80)

        # DOB of the member
        self.member_dob_lbl = Label(self.bottom_left, text="Date of Birth of the Member : ", bg="#DFDEDE")
        self.member_dob_lbl.place(x=10, y=120)

        self.member_dob_ety = ttk.Entry(self.bottom_left, width=40)
        self.member_dob_ety.insert(0, 'Please enter the Date of Birth of the Member')
        self.member_dob_ety.place(x=170, y=120)

        # Gender of the Member
        self.member_gender_lbl = Label(self.bottom_left, text="Gender of the Member : ", bg="#DFDEDE")
        self.member_gender_lbl.place(x=10, y=160)

        self.member_gender_combobox = ttk.Combobox(self.bottom_left, textvariable="gender", values=('Male', "Female"),
                                               state='readonly', width=40)
        self.member_gender_combobox.place(x=170, y=160)

        # Role of the member
        self.member_role_lbl = Label(self.bottom_left, text="Job of the Member : ", bg="#DFDEDE")
        self.member_role_lbl.place(x=10, y=200)

        self.member_role_combobox = ttk.Combobox(self.bottom_left, textvariable="Job", values=('Manager', "Carpenter", "Designer"), state='readonly', width=40)
        self.member_role_combobox.place(x=170, y=200)

        # Address of the Member
        self.member_address_lbl = Label(self.bottom_left, text="Address of the Member : ", bg="#DFDEDE")
        self.member_address_lbl.place(x=10, y=240)

        self.member_address_ety = Text(self.bottom_left, width=30, height=10, wrap=WORD)
        self.member_address_ety.place(x=170, y=240)

        # Button to finally add
        self.add_btn = ttk.Button(self.bottom_left, text="Add Member", width=14, command=self.save_member)
        self.add_btn.place(x=360, y=415)







        #ADD INVENTORY
        self.team_member_lbl = Label(self.bottom_right, text="INVENTORY", bg="#E9E8E8", font="Broadway 35")
        self.team_member_lbl.place(x=90, y=10)

        # Name of the Material
        self.material_name_lbl = Label(self.bottom_right, text="Name of the Material : ", bg="#E9E8E8")
        self.material_name_lbl.place(x=10, y=80)

        self.material_name_ety = ttk.Entry(self.bottom_right, width=40)
        self.material_name_ety.insert(0, 'Please enter the name of the Material')
        self.material_name_ety.place(x=170, y=80)

        # Quantity of the material
        self.material_qty_lbl = Label(self.bottom_right, text="Quantity of Material : ", bg="#E9E8E8")
        self.material_qty_lbl.place(x=10, y=120)

        self.material_qty_ety = ttk.Entry(self.bottom_right, width=40)
        self.material_qty_ety.insert(0, 'Please enter the Quantity of Material')
        self.material_qty_ety.place(x=170, y=120)

        # COST PRICE of the material
        self.material_cp_lbl = Label(self.bottom_right, text="Cost Price of Material : ", bg="#E9E8E8")
        self.material_cp_lbl.place(x=10, y=160)

        self.material_cp_ety = ttk.Entry(self.bottom_right, width=40)
        self.material_cp_ety.insert(0, 'Please enter the Cost Price of Material')
        self.material_cp_ety.place(x=170, y=160)

        # SELL PRICE of the material
        self.material_sp_lbl = Label(self.bottom_right, text="Sell Price of Material : ", bg="#E9E8E8")
        self.material_sp_lbl.place(x=10, y=200)

        self.material_sp_ety = ttk.Entry(self.bottom_right, width=40)
        self.material_sp_ety.insert(0, 'Please enter the Sell Price of Material')
        self.material_sp_ety.place(x=170, y=200)

        # Button to finally add
        self.add_btn = ttk.Button(self.bottom_right, text="Add Material", width=14, command = self.save_material)
        self.add_btn.place(x=350, y=250)


    def save_member(self):

        project_name = self.project_name_ety.get()
        member_name = self.member_name_ety.get()
        member_dob = self.member_dob_ety.get()
        member_gender = self.member_gender_combobox.get()
        member_role = self.member_role_combobox.get()
        member_address = self.member_address_ety.get(1.0, "end-1c")


        if (project_name and member_name and member_dob and member_gender and member_role and member_address) != "":
            try:
                query = "INSERT INTO  'Project_Team' (Project_name, Member_name, Member_dob, Member_gender, Member_role, Member_address) VALUES(?,?,?,?,?,?)"
                crsr.execute(query, (project_name, member_name, member_dob, member_gender, member_role, member_address))
                connection.commit()
                messagebox.showinfo("Success", "Successfully added to database", icon="info")

            except:
                messagebox.showerror("Error", "Can't add to database", icon="warning")
        else:
            messagebox.showerror("Error", "Fields can't be empty", icon="warning")




    def save_material(self):

        project_name = self.project_name_ety.get()
        material_name = self.material_name_ety.get()
        material_qty = self.material_qty_ety.get()
        material_cp = self.material_cp_ety.get()
        material_sp = self.material_sp_ety.get()

        if (project_name and material_name and material_qty and material_cp and material_sp) != "":
            try:
                query = "INSERT INTO 'Project_Inventory' (Project_name, Material_name, Material_qty, Material_cp, Material_sp) VALUES(?,?,?,?,?)"
                crsr.execute(query, (project_name, material_name, material_qty, material_cp, material_sp))
                connection.commit()
                messagebox.showinfo("Success", "Successfully added to database", icon="info")

            except:
                messagebox.showerror("Error", "Can't add to database", icon="warning")
        else:
            messagebox.showerror("Error", "Fields can't be empty", icon="warning")



















    #     # # SAVE PROJECT NAME
    #     # self.save_name_btn = Button(self.bottom, text="Save", width=15, command=self.save_project)
    #     # self.save_name_btn.place(x=200, y=40)
    #
    #     # SETUP TEAM
    #     self.setup_team_btn = Button(self.bottom, text="+ TEAM", width=15, command=self.team_pressed)
    #     self.setup_team_btn.place(x=20, y=100)
    #
    #     # SETUP INVENTORY
    #     self.setup_inventory_btn = Button(self.bottom, text="+ INVENTORY", width=15, command=self.inventory_pressed)
    #     self.setup_inventory_btn.place(x=160, y=100)
    #
    #     # # SETUP FINANCE
    #     # self.setup_finance_btn = Button(self.bottom, text = "+ FINANCE", width = 15, command =self.finance_pressed)
    #     # self.setup_finance_btn.place(x = 300, y=60)
    #
    # def team_pressed(self):
    #
    #
    #     project_name = self.project_name_ety.get()
    #
    #     if project_name != "":
    #         try:
    #             # query_1 =
    #             # query_2 =
    #             crsr.execute("INSERT INTO Project_Team (Project_name) VALUES (?)", (project_name,))
    #             # crsr.execute("INSERT INTO Project_Inventory (Project_name) VALUES (?)", (project_name,))
    #             connection.commit()
    #             messagebox.showinfo("Success", "Successfully added to database", icon="info")
    #
    #         except:
    #             messagebox.showerror("Error", "Can't add to database", icon="warning")
    #     else:
    #         messagebox.showerror("Error", "Fields can't be empty", icon="warning")
    #
    #     team = Team_add_member.Add_member()
    #
    # def inventory_pressed(self):
    #
    #     project_name = self.project_name_ety.get()
    #
    #     if project_name != "":
    #         try:
    #             query = "INSERT INTO Ladderrise(Project_name) VALUES(?)"
    #             crsr.execute(query, project_name)
    #             connection.commit()
    #             messagebox.showinfo("Success", "Successfully added to database", icon="info")
    #
    #
    #         except:
    #             messagebox.showerror("Error", "Can't add to database", icon="warning")
    #     else:
    #         messagebox.showerror("Error", "Fields can't be empty", icon="warning")
    #
    #     inventory = Inventory_add.Add_inventory()
    #
    # # # def save_project(self):
    # #     project_name = self.project_name_ety.get()
    # #
    # #     if project_name != "":
    # #         try:
    # #             crsr.execute("INSERT INTO 'Ladderrise' (Project_name) VALUES(?,)", project_name)
    # #             connection.commit()
    # #             messagebox.showinfo("Success", "Successfully added to database", icon="info")
    # #
    # #         except:
    # #             messagebox.showerror("Error", "Can't add to database", icon="warning")
    # #     else:
    # #         messagebox.showerror("Error", "Fields can't be empty", icon="warning")

