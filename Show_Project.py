from tkinter import *
import sqlite3
import Add_Project
import Inventory_add
from tkinter import messagebox
from tkinter.ttk import  Combobox
from ttkthemes import themed_tk as tk
from tkinter import ttk


connection = sqlite3.connect("Company.db")
crsr = connection.cursor()

class Show_project(Toplevel):

    def __init__(self):

        Toplevel.__init__(self)
        self.title("COMPANY")
        self.geometry("1000x650+300+20")
        self.iconbitmap()
        self.resizable(False, False)

        # FRAMES
        # self.top = Frame(self, height=100, bg="white")
        # self.top.pack(fill=X, side = TOP)
        #
        # self.middle = Frame(self, height = 75, bg = "#DFDEDE")
        # self.middle.pack(fill=X)
        #
        # self.bottom = Frame(self, height=475, bg="#FFD28E")
        # self.bottom.pack(fill=X, side = BOTTOM)

        self.middle = Frame(self, height=80, bg="#FFD28E")
        self.middle.pack(fill=X)

        self.bottom_left = Frame(self, height=285, width=500, bg="#DFDEDE")
        self.bottom_left.pack(fill=Y, side=LEFT)

        self.bottom_right = Frame(self, height=285, width=500, bg="#E9E8E8")
        self.bottom_right.pack(fill=Y, side=RIGHT)


        # 2nd TITLE

        self.projects_lbl = Label(self.middle, text = "MY PROJECTS", bg = "#FFD28E", fg= "#BD2312", font = "Broadway 40")
        self.projects_lbl.place(x=280, y=10)



#TEAM_________________________________________________________________________________________________________________

        #TEAM TITLE

        self.project_team_lbl = Label(self.bottom_left, text="TEAM", bg="#DFDEDE", font="Broadway 35")
        self.project_team_lbl.place(x=150, y=10)

        # LIST OF MEMBERS
        self.project_members_list = Listbox(self.bottom_left, width = 50, height = 25)
        self.project_members_list.place(x = 30, y=80)
        # self.members_list.config(yscrollcommand = self.list_scroll.set )
        #
        # self.list_scroll = Scrollbar(self.bottom, orient = VERTICAL)
        # self.list_scroll.config(command = self.members_list.yview())
        # self.list_scroll.place(x=460, y=100)

        members = crsr.execute("SELECT distinct Project_name FROM Project_Team").fetchall()
        count = 0
        for member in members:

            self.project_members_list.insert(count, str(member[0]))
            count += 1

        # ADD BUTTON

        self.team_add_a_project_btn = ttk.Button(self.bottom_left, text="Add Project", width=18, command = self.add_project)
        self.team_add_a_project_btn.place(x=350, y=80)


        # DELETE BUTTON

        self.team_delete_project_btn = ttk.Button(self.bottom_left, text="Delete Project", width=18, command = self.delete_project_team)
        self.team_delete_project_btn.place(x=350, y=110)

        # SHOW BUTTON

        self.team_show_project_btn = ttk.Button(self.bottom_left, text = "Show Project", width = 18, command = self.show_team_project)
        self.team_show_project_btn.place(x=350, y = 140)





#INVENTORY__________________________________________________________

        # TEAM TITLE

        self.project_inventory_lbl = Label(self.bottom_right, text="INVENTORY", bg="#E9E8E8", font="Broadway 35")
        self.project_inventory_lbl.place(x=120, y=10)

        # LIST OF MATERIAL
        self.project_material_list = Listbox(self.bottom_right, width=50, height=25)
        self.project_material_list.place(x=30, y=80)
        # self.members_list.config(yscrollcommand = self.list_scroll.set )
        #
        # self.list_scroll = Scrollbar(self.bottom, orient = VERTICAL)
        # self.list_scroll.config(command = self.members_list.yview())
        # self.list_scroll.place(x=460, y=100)


        materials = crsr.execute("SELECT distinct Project_name FROM Project_Inventory").fetchall()

        count = 0
        for material in materials:
            self.project_material_list.insert(count, str(material[0]))
            count += 1


        # ADD BUTTON

        self.inventory_add_a_project_btn = ttk.Button(self.bottom_right, text="Add Project", width=18, command=self.add_project)
        self.inventory_add_a_project_btn.place(x=350, y=80)

        # DELETE BUTTON

        self.inventory_delete_project_btn = ttk.Button(self.bottom_right, text="Delete Project", width=18, command = self.delete_project_inventory)
        self.inventory_delete_project_btn.place(x=350, y=110)

        # SHOW BUTTON

        self.inventory_show_project_btn = ttk.Button(self.bottom_right, text="Show Project", width=18, command=self.show_inventory_project  )
        self.inventory_show_project_btn.place(x=350, y=140)

    def add_project(self):

        add_project = Add_Project.Add_Project()

    def delete_project_team(self):

        selected_team_project = self.project_members_list.curselection()
        team_project_name_to_delete = self.project_members_list.get(selected_team_project)

        mbox = messagebox.askquestion("Warning", "Are you sure you want to delete this project ?", icon = "warning")

        if mbox == "yes":
            try:
                crsr.execute("DELETE FROM Project_Team where Project_name = ?", (team_project_name_to_delete, ))
                connection.commit()
                messagebox.showinfo("Success", "Successfully deleted from database", icon="info")


            except:
                messagebox.showerror("Error", "Can't delete from database", icon="warning")

    def delete_project_inventory(self):

        selected_inventory_project = self.project_material_list.curselection()
        inventory_project_name_to_delete = self.project_material_list.get(selected_inventory_project)

        mbox = messagebox.askquestion("Warning", "Are you sure you want to delete this project ?", icon="warning")

        if mbox == "yes":
            try:
                crsr.execute("DELETE FROM Project_Inventory where Project_name = ?", (inventory_project_name_to_delete,))
                connection.commit()
                messagebox.showinfo("Success", "Successfully deleted from database", icon="info")


            except:
                messagebox.showerror("Error", "Can't delete from database", icon="warning")

    def show_team_project(self):


        global team_project_name
        selected_team_project = self.project_members_list.curselection()
        team_project_name = self.project_members_list.get(selected_team_project)
        toshow_team_project = Show_team_project()

    def show_inventory_project(self):

        global inventory_project_name
        selected_inventory_project = self.project_material_list.curselection()
        inventory_project_name = self.project_material_list.get(selected_inventory_project)
        toshow_inventory_project = Show_inventory_project()


class Show_team_project(Toplevel):

    def __init__(self):

        Toplevel.__init__(self)
        self.title("COMPANY")
        self.geometry("650x650+680+20")
        self.iconbitmap()
        self.resizable(False, False)


        global team_project_name

        # FRAMES
        self.top = Frame(self, height=150, bg="#FFF3F3")
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg="#FFD28E")
        self.bottom.pack(fill=X)

        # TITLE
        self.title_lbl = Label(self.top, text="TEAM", font="Broadway 60 bold", fg="#BD2312", bg="#FFF3F3")
        self.title_lbl.place(x=40, y=20)

        # LIST OF MEMBERS
        self.members_list = Listbox(self.bottom, width = 50, height = 25)
        self.members_list.place(x = 30, y=30)
        # self.members_list.config(yscrollcommand = self.list_scroll.set )
        #
        # self.list_scroll = Scrollbar(self.bottom, orient = VERTICAL)
        # self.list_scroll.config(command = self.members_list.yview())
        # self.list_scroll.place(x=460, y=100)

        members = crsr.execute("SELECT * FROM Project_Team WHERE Project_name = ?", (team_project_name, )).fetchall()
        count = 0
        for member in members:
            self.members_list.insert(count, str(member[2]))
            count += 1

        # ADD BUTTON

        self.add_a_member_btn = ttk.Button(self.bottom, text="Add Member", width=18, command=self.add_member_pressed)
        self.add_a_member_btn.place(x=360, y=30)


        # DELETE BUTTON

        self.delete_member_btn = ttk.Button(self.bottom, text="Delete Member", width=18,command = self.delete_member_pressed)
        self.delete_member_btn.place(x=500, y=30)

        # UPDATE BUTTON

        self.update_member_btn = ttk.Button(self.bottom, text="Update Member", width=18, command = self.update_member_pressed)
        self.update_member_btn.place(x=360, y=60)

        # VIEW BUTTON

        self.show_member_btn = ttk.Button(self.bottom, text="View Member", width=18, command = self.view_member_pressed)
        self.show_member_btn.place(x=500, y=60)

    def add_member_pressed(self):

        global team_project_name
        add_project = Add_member()

    def view_member_pressed(self):

        global member_name_view
        selected_member_name = self.members_list.curselection()
        member_name_view = self.members_list.get(selected_member_name)

        view_member = View_member()

    def update_member_pressed(self):

        global member_name_update
        global team_project_name
        selected_member_name = self.members_list.curselection()
        member_name_update = self.members_list.get(selected_member_name)

        update_member = Update_member()


    def delete_member_pressed(self):

        selected_member = self.members_list.curselection()
        member_name_to_delete = self.members_list.get(selected_member)

        mbox = messagebox.askquestion("Warning", "Are you sure you want to delete this member ?", icon="warning")

        if mbox == "yes":
            try:
                crsr.execute("DELETE FROM Project_Team where Member_name = ?", (member_name_to_delete, ))
                connection.commit()
                messagebox.showinfo("Success", "Successfully deleted from database", icon="info")


            except:
                messagebox.showerror("Error", "Can't delete from database", icon="warning")


class Add_member(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        self.title("COMPANY")
        self.geometry("650x650+680+20")
        self.iconbitmap()
        self.resizable(False, False)

        global team_project_name

        # FRAMES
        self.top = Frame(self, height=150, bg="#FFF3F3")
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg="#FFD28E")
        self.bottom.pack(fill=X)

        # TITLE
        self.title_lbl = Label(self.top, text="ADD MEMBER", font="Broadway 60 bold", fg="#BD2312", bg="#FFF3F3")
        self.title_lbl.place(x=40, y=20)

        # Name of the Member
        self.member_name_lbl = Label(self.bottom, text="Name of the Member : ", bg="#FFD28E")
        self.member_name_lbl.place(x=10, y=10)

        self.member_name_ety = ttk.Entry(self.bottom, width=40)
        self.member_name_ety.insert(0, 'Please enter the name of the Member')
        self.member_name_ety.place(x=170, y=10)

        # DOB of the member
        self.member_dob_lbl = Label(self.bottom, text="Date of Birth of the Member : ", bg="#FFD28E")
        self.member_dob_lbl.place(x=10, y=50)

        self.member_dob_ety = ttk.Entry(self.bottom, width=40)
        self.member_dob_ety.insert(0, 'Please enter the Date of Birth of the Member')
        self.member_dob_ety.place(x=170, y=50)

        # Gender of the Member
        self.member_gender_lbl = Label(self.bottom, text="Gender of the Member : ", bg="#FFD28E")
        self.member_gender_lbl.place(x=10, y=90)

        self.member_gender_combobox = ttk.Combobox(self.bottom, textvariable = "gender", values = ('Male', "Female"), state = 'readonly', width = 40)
        self.member_gender_combobox.place(x=170, y=90)

        # Role of the member
        self.member_role_lbl = Label(self.bottom, text="Job of the Member : ", bg="#FFD28E")
        self.member_role_lbl.place(x=10, y=130)

        self.member_role_combobox = ttk.Combobox(self.bottom, textvariable = "Job", values = ('Manager', "Carpenter", "Designer"), state = 'readonly', width = 40)
        self.member_role_combobox.place(x=170, y=130)

        # Address of the Member
        self.member_address_lbl = Label(self.bottom, text="Address of the Member : ", bg="#FFD28E")
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

        if (team_project_name and member_name and member_dob and member_gender and member_role and member_address) != "":
            try:
                query = "INSERT INTO  'Project_Team' (Project_name, Member_name, Member_dob, Member_gender, Member_role, Member_address) VALUES(?,?,?,?,?,?)"
                crsr.execute(query, (team_project_name, member_name, member_dob, member_gender, member_role, member_address))
                connection.commit()
                messagebox.showinfo("Success", "Successfully added to database", icon="info")

            except:
                messagebox.showerror("Error", "Can't add to database", icon="warning")
        else:
            messagebox.showerror("Error", "Fields can't be empty", icon="warning")


class View_member(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        self.title("COMPANY")
        self.geometry("650x650+680+20")
        self.iconbitmap()
        self.resizable(False, False)

        global member_name_view

        # FRAMES
        self.top = Frame(self, height=150, bg="#FFF3F3")
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg="#FFD28E")
        self.bottom.pack(fill=X)

        # TITLE
        self.title_lbl = Label(self.top, text="VIEW MEMBER", font="Broadway 60 bold", fg="#BD2312", bg="#FFF3F3")
        self.title_lbl.place(x=40, y=20)

        member = crsr.execute("SELECT * from Project_Team where Member_name = ?", (member_name_view, )).fetchall()
        member_name = member[0][2]
        member_dob = member[0][3]
        member_gender = member[0][4]
        member_role = member[0][5]
        member_address = member[0][6]


        # Name of the Member
        self.member_name_lbl = Label(self.bottom, text="Name of the Member : ", bg="#FFD28E")
        self.member_name_lbl.place(x=10, y=10)

        self.member_name_ety = ttk.Entry(self.bottom, width=40)
        self.member_name_ety.insert(0, member_name)
        self.member_name_ety.config(state = "disabled")
        self.member_name_ety.place(x=170, y=10)

        # DOB of the member
        self.member_dob_lbl = Label(self.bottom, text="Date of Birth of the Member : ", bg="#FFD28E")
        self.member_dob_lbl.place(x=10, y=50)

        self.member_dob_ety = ttk.Entry(self.bottom, width=40)
        self.member_dob_ety.insert(0, member_dob)
        self.member_dob_ety.config(state = "disabled")
        self.member_dob_ety.place(x=170, y=50)

        # Gender of the Member
        self.member_gender_lbl = Label(self.bottom, text="Gender of the Member : ", bg="#FFD28E")
        self.member_gender_lbl.place(x=10, y=90)

        self.member_gender_ety = ttk.Entry(self.bottom, width=40)
        self.member_gender_ety.insert(0, member_gender)
        self.member_gender_ety.config(state = "disabled")
        self.member_gender_ety.place(x=170, y=90)

        # Role of the member
        self.member_role_lbl = Label(self.bottom, text="Job of the Member : ", bg="#FFD28E")
        self.member_role_lbl.place(x=10, y=130)

        self.member_role_ety = ttk.Entry(self.bottom, width=40)
        self.member_role_ety.insert(0, member_role)
        self.member_role_ety.config(state = "disabled")
        self.member_role_ety.place(x=170, y=130)

        # Address of the Member
        self.member_address_lbl = Label(self.bottom, text="Address of the Member : ", bg="#FFD28E")
        self.member_address_lbl.place(x=10, y=170)

        self.member_address_ety = Text(self.bottom, width=30, height=10, wrap=WORD)
        self.member_address_ety.insert("1.0", member_address)
        self.member_address_ety.config(state = "disabled")
        self.member_address_ety.place(x=170, y=170)

class Update_member(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        self.title("COMPANY")
        self.geometry("650x650+680+20")
        self.iconbitmap()
        self.resizable(False, False)

        global member_name_update
        global team_project_name
        global member_id

        # FRAMES
        self.top = Frame(self, height=150, bg="#FFF3F3")
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg="#FFD28E")
        self.bottom.pack(fill=X)

        # TITLE
        self.title_lbl = Label(self.top, text="UPDATE MEMBER", font="Broadway 60 bold", fg="#BD2312", bg="#FFF3F3")
        self.title_lbl.place(x=40, y=20)

        member = crsr.execute("SELECT * from Project_Team where Member_name = ?", (member_name_update, )).fetchall()

        member_id = member[0][0]
        member_name = member[0][2]
        member_dob = member[0][3]
        member_gender = member[0][4]
        member_role = member[0][5]
        member_address = member[0][6]



        # Name of the Member
        self.member_name_lbl = Label(self.bottom, text="Name of the Member : ", bg="#FFD28E")
        self.member_name_lbl.place(x=10, y=10)

        self.member_name_ety = ttk.Entry(self.bottom, width=40)
        self.member_name_ety.insert(0, member_name)
        self.member_name_ety.place(x=170, y=10)

        # DOB of the member
        self.member_dob_lbl = Label(self.bottom, text="Date of Birth of the Member : ", bg="#FFD28E")
        self.member_dob_lbl.place(x=10, y=50)

        self.member_dob_ety = ttk.Entry(self.bottom, width=40)
        self.member_dob_ety.insert(0, member_dob)
        self.member_dob_ety.place(x=170, y=50)

        # Gender of the Member
        self.member_gender_lbl = Label(self.bottom, text="Gender of the Member : ", bg="#FFD28E")
        self.member_gender_lbl.place(x=10, y=90)

        self.member_gender_combobox = ttk.Combobox(self.bottom, textvariable="gender", values=('Male', "Female"), state='readonly', width=40)
        self.member_gender_combobox.set(member_gender)
        self.member_gender_combobox.place(x=170, y=90)

        # Role of the member
        self.member_role_lbl = Label(self.bottom, text="Job of the Member : ", bg="#FFD28E")
        self.member_role_lbl.place(x=10, y=130)

        self.member_role_ety = ttk.Combobox(self.bottom, textvariable="role", values=('Manager', "Carpenter", "Designer"), state='readonly', width=40)
        self.member_role_ety.set(member_role)
        self.member_role_ety.place(x=170, y=130)

        # Address of the Member
        self.member_address_lbl = Label(self.bottom, text="Address of the Member : ", bg="#FFD28E")
        self.member_address_lbl.place(x=10, y=170)

        self.member_address_ety = Text(self.bottom, width=30, height=10, wrap=WORD)
        self.member_address_ety.insert("1.0", member_address)
        self.member_address_ety.place(x=170, y=170)

        # Button to finally update
        self.add_btn = ttk.Button(self.bottom, text="Update Member", width=14, command=self.update_member)
        self.add_btn.place(x=200, y=370)

    def update_member(self):

        global member_id
        member_name = self.member_name_ety.get()
        member_dob = self.member_dob_ety.get()
        member_gender = self.member_gender_combobox.get()
        member_role = self.member_role_ety.get()
        member_address = self.member_address_ety.get(1.0, "end-1c")

        try:

            crsr.execute("UPDATE Project_Team SET Member_name=? , Member_dob=? , Member_gender=? , Member_role=? , Member_address=? WHERE ID=? ", (member_name, member_dob, member_gender, member_role, member_address, member_id, ))
            messagebox.showinfo("Success", "Member has been successfully updated.")

            connection.commit()

        except:

            messagebox.showinfo("Warning", "Member has not been updated.", icon = "warning")


class Show_inventory_project(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        self.title("COMPANY")
        self.geometry("650x650+680+20")
        self.iconbitmap()
        self.resizable(False, False)

        global inventory_project_name

        # FRAMES
        self.top = Frame(self, height=150, bg="#FFF3F3")
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg="#FFD28E")
        self.bottom.pack(fill=X)

        # TITLE
        self.title_lbl = Label(self.top, text="INVENTORY", font="Broadway 60 bold", fg="#BD2312", bg="#FFF3F3")
        self.title_lbl.place(x=40, y=20)

        # LIST OF MATERIALS
        self.materials_list = Listbox(self.bottom, width=50, height=25)
        self.materials_list.place(x=30, y=30)
        # self.members_list.config(yscrollcommand = self.list_scroll.set )
        #
        # self.list_scroll = Scrollbar(self.bottom, orient = VERTICAL)
        # self.list_scroll.config(command = self.members_list.yview())
        # self.list_scroll.place(x=460, y=100)

        materials = crsr.execute("SELECT * FROM Project_Inventory where Project_name = ?", (inventory_project_name, )).fetchall()
        count = 0
        for material in materials:
            self.materials_list.insert(count, str(material[2]))
            count += 1

        # ADD BUTTON

        self.add_a_material_btn = ttk.Button(self.bottom, text="Add Material", width=18, command = self.add_material_pressed)
        self.add_a_material_btn.place(x=360, y=30)

        # DELETE BUTTON

        self.delete_material_btn = ttk.Button(self.bottom, text="Delete Material", width=18, command = self.delete_material_pressed)
        self.delete_material_btn.place(x=500, y=30)

        # UPDATE BUTTON

        self.update_material_btn = ttk.Button(self.bottom, text="Update Material", width=18, command = self.update_material_pressed)
        self.update_material_btn.place(x=360, y=60)

        # VIEW BUTTON

        self.show_material_btn = ttk.Button(self.bottom, text="View Material", width=18, command = self.view_material_pressed)
        self.show_material_btn.place(x=500, y=60)


    def add_material_pressed(self):

        global inventory_project_name
        add_material = Add_material()

    def view_material_pressed(self):

        global material_name_view
        selected_material_name = self.materials_list.curselection()
        material_name_view = self.materials_list.get(selected_material_name)

        view_material = View_material()

    def update_material_pressed(self):

        global material_name_update
        global inventory_project_name
        selected_material_name = self.materials_list.curselection()
        material_name_update = self.materials_list.get(selected_material_name)

        update_material = Update_material()



    def delete_material_pressed(self):


        selected_material = self.materials_list.curselection()
        material_name_to_delete = self.materials_list.get(selected_material)

        mbox = messagebox.askquestion("Warning", "Are you sure you want to delete this member ?", icon="warning")

        if mbox == "yes":
                try:
                    crsr.execute("DELETE FROM Project_Team where Material_name = ?", (material_name_to_delete, ))
                    connection.commit()
                    messagebox.showinfo("Success", "Successfully deleted from database", icon="info")


                except:
                    messagebox.showerror("Error", "Can't delete from database", icon="warning")


class Add_material(Toplevel):


    def __init__(self):
        Toplevel.__init__(self)
        self.title("COMPANY")
        self.geometry("650x650+680+20")
        self.iconbitmap()
        self.resizable(False, False)

        global inventory_project_name

        # FRAMES
        self.top = Frame(self, height=150, bg="#FFF3F3")
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg="#FFD28E")
        self.bottom.pack(fill=X)

        # TITLE
        self.title_lbl = Label(self.top, text="ADD MATERIAL", font="Broadway 60 bold", fg="#BD2312", bg="#FFF3F3")
        self.title_lbl.place(x=40, y=20)

        # Name of the Material
        self.material_name_lbl = Label(self.bottom, text="Name of the Material : ", bg="#FFD28E")
        self.material_name_lbl.place(x=10, y=10)

        self.material_name_ety = ttk.Entry(self.bottom, width=40)
        self.material_name_ety.insert(0, 'Please enter the name of the Material')
        self.material_name_ety.place(x=170, y=10)

        # Quantity of the material
        self.material_qty_lbl = Label(self.bottom, text="Quantity of Material : ", bg="#FFD28E")
        self.material_qty_lbl.place(x=10, y=50)

        self.material_qty_ety = ttk.Entry(self.bottom, width=40)
        self.material_qty_ety.insert(0, 'Please enter the Quantity of Material')
        self.material_qty_ety.place(x=170, y=50)

        # COST PRICE of the material
        self.material_cp_lbl = Label(self.bottom, text="Cost Price of Material : ", bg="#FFD28E")
        self.material_cp_lbl.place(x=10, y=90)

        self.material_cp_ety = ttk.Entry(self.bottom, width=40)
        self.material_cp_ety.insert(0, 'Please enter the Cost Price of Material')
        self.material_cp_ety.place(x=170, y=90)


        # SELL PRICE of the material
        self.material_sp_lbl = Label(self.bottom, text="Sell Price of Material : ", bg="#FFD28E")
        self.material_sp_lbl.place(x=10, y=130)

        self.material_sp_ety = ttk.Entry(self.bottom, width=40)
        self.material_sp_ety.insert(0, 'Please enter the Sell Price of Material')
        self.material_sp_ety.place(x=170, y=130)

        # Button to finally add
        self.add_btn = ttk.Button(self.bottom, text="Add", width =8, command=self.save_material)
        self.add_btn.place(x=350, y=170)


    def save_material(self):
        material_name = self.material_name_ety.get()
        material_qty = self.material_qty_ety.get()
        material_cp = self.material_cp_ety.get()
        material_sp = self.material_sp_ety.get()

        if (inventory_project_name and material_name and material_qty and material_cp and material_sp) != "":
            try:
                query = "INSERT INTO 'Project_Inventory' (Project_name, Material_name, Material_qty, Material_cp, Material_sp) VALUES(?,?,?,?,?)"
                crsr.execute(query, (inventory_project_name, material_name, material_qty, material_cp, material_sp))
                connection.commit()
                messagebox.showinfo("Success", "Successfully added to database", icon="info")

            except:
                messagebox.showerror("Error", "Can't add to database", icon="warning")
        else:
            messagebox.showerror("Error", "Fields can't be empty", icon="warning")

class View_material(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        self.title("COMPANY")
        self.geometry("650x650+680+20")
        self.iconbitmap()
        self.resizable(False, False)

        global material_name_view

        # FRAMES
        self.top = Frame(self, height=150, bg="#FFF3F3")
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg="#FFD28E")
        self.bottom.pack(fill=X)

        # TITLE
        self.title_lbl = Label(self.top, text="VIEW MATERIAL", font="Broadway 60 bold", fg="#BD2312", bg="#FFF3F3")
        self.title_lbl.place(x=40, y=20)

        material = crsr.execute("SELECT * from Project_Inventory where Material_name = ?", (material_name_view, )).fetchall()
        material_name = material[0][2]
        material_qty = material[0][3]
        material_cp = material[0][4]
        material_sp = material[0][5]


        # Name of the Material
        self.material_name_lbl = Label(self.bottom, text="Name of the Material : ", bg="#FFD28E")
        self.material_name_lbl.place(x=10, y=10)

        self.material_name_ety = ttk.Entry(self.bottom, width=40)
        self.material_name_ety.insert(0, material_name)
        self.material_name_ety.config(state = "disabled")
        self.material_name_ety.place(x=170, y=10)

        # Quantity of the material
        self.material_qty_lbl = Label(self.bottom, text="Quantity of Material : ", bg="#FFD28E")
        self.material_qty_lbl.place(x=10, y=50)

        self.material_qty_ety = ttk.Entry(self.bottom, width=40)
        self.material_qty_ety.insert(0, material_qty)
        self.material_qty_ety.config(state = "disabled")
        self.material_qty_ety.place(x=170, y=50)

        # COST PRICE of the material
        self.material_cp_lbl = Label(self.bottom, text="Cost Price of Material : ", bg="#FFD28E")
        self.material_cp_lbl.place(x=10, y=90)

        self.material_cp_ety = ttk.Entry(self.bottom, width=40)
        self.material_cp_ety.insert(0, material_cp)
        self.material_cp_ety.config(state = "disabled")
        self.material_cp_ety.place(x=170, y=90)


        # SELL PRICE of the material
        self.material_sp_lbl = Label(self.bottom, text="Sell Price of Material : ", bg="#FFD28E")
        self.material_sp_lbl.place(x=10, y=130)

        self.material_sp_ety = ttk.Entry(self.bottom, width=40)
        self.material_sp_ety.insert(0, material_sp)
        self.material_sp_ety.config(state = "disabled")
        self.material_sp_ety.place(x=170, y=130)

class Update_material(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        self.title("COMPANY")
        self.geometry("650x650+680+20")
        self.iconbitmap()
        self.resizable(False, False)

        global material_name_update
        global inventory_project_name
        global material_id

        # FRAMES
        self.top = Frame(self, height=150, bg="#FFF3F3")
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg="#FFD28E")
        self.bottom.pack(fill=X)

        # TITLE
        self.title_lbl = Label(self.top, text="UPDATE MATERIAL", font="Broadway 60 bold", fg="#BD2312", bg="#FFF3F3")
        self.title_lbl.place(x=40, y=20)

        material = crsr.execute("SELECT * from Project_Inventory where Material_name = ?", (material_name_update, )).fetchall()
        material_id = material[0][0]
        material_name = material[0][2]
        material_qty = material[0][3]
        material_cp = material[0][4]
        material_sp = material[0][5]


        # Name of the Material
        self.material_name_lbl = Label(self.bottom, text="Name of the Material : ", bg="#FFD28E")
        self.material_name_lbl.place(x=10, y=10)

        self.material_name_ety = ttk.Entry(self.bottom, width=40)
        self.material_name_ety.insert(0, material_name)
        self.material_name_ety.place(x=170, y=10)

        # Quantity of the material
        self.material_qty_lbl = Label(self.bottom, text="Quantity of Material : ", bg="#FFD28E")
        self.material_qty_lbl.place(x=10, y=50)

        self.material_qty_ety = ttk.Entry(self.bottom, width=40)
        self.material_qty_ety.insert(0, material_qty)
        self.material_qty_ety.place(x=170, y=50)

        # COST PRICE of the material
        self.material_cp_lbl = Label(self.bottom, text="Cost Price of Material : ", bg="#FFD28E")
        self.material_cp_lbl.place(x=10, y=90)

        self.material_cp_ety = ttk.Entry(self.bottom, width=40)
        self.material_cp_ety.insert(0, material_cp)
        self.material_cp_ety.place(x=170, y=90)

        # SELL PRICE of the material
        self.material_sp_lbl = Label(self.bottom, text="Sell Price of Material : ", bg="#FFD28E")
        self.material_sp_lbl.place(x=10, y=130)

        self.material_sp_ety = ttk.Entry(self.bottom, width=40)
        self.material_sp_ety.insert(0, material_sp)
        self.material_sp_ety.place(x=170, y=130)

        # Button to finally update
        self.add_btn = ttk.Button(self.bottom, text="Update Member", width=14, command=self.update_material)
        self.add_btn.place(x=200, y=370)

    def update_material(self):

        global inventory_project_name
        global material_id
        material_name = self.material_name_ety.get()
        material_qty = self.material_qty_ety.get()
        material_cp = self.material_cp_ety.get()
        material_sp = self.material_sp_ety.get()

        try:

            crsr.execute("UPDATE Project_Inventory SET Material_name=? , Material_qty=? , Material_cp=? , Material_sp=? WHERE ID=? ", (material_name, material_qty, material_cp, material_sp, material_id, ))
            messagebox.showinfo("Success", "Material has been successfully updated.")

            connection.commit()

        except:

            messagebox.showinfo("Warning", "Material has not been updated.", icon = "warning")





