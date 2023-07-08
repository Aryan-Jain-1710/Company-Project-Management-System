from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from ttkthemes import themed_tk as tk
from tkinter import ttk


connection = sqlite3.connect("Company.db")
crsr = connection.cursor()


class Add_inventory(Toplevel):

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
        self.title_lbl = Label(self.top, text="ADD MATERIAL", font="Broadway 60 bold", fg="#BD2312", bg="white")
        self.title_lbl.place(x=40, y=20)

        # Name of the Material
        self.material_name_lbl = Label(self.bottom, text="Name of the Material : ", bg="#FABC5F")
        self.material_name_lbl.place(x=10, y=10)

        self.material_name_ety = Entry(self.bottom, width=40)
        self.material_name_ety.insert(0, 'Please enter the name of the Material')
        self.material_name_ety.place(x=170, y=10)

        # Quantity of the material
        self.material_qty_lbl = Label(self.bottom, text="Quantity of Material : ", bg="#FABC5F")
        self.material_qty_lbl.place(x=10, y=50)

        self.material_qty_ety = ttk.Entry(self.bottom, width=40)
        self.material_qty_ety.insert(0, 'Please enter the Quantity of Material')
        self.material_qty_ety.place(x=170, y=50)

        # COST PRICE of the material
        self.material_cp_lbl = Label(self.bottom, text="Cost Price of Material : ", bg="#FABC5F")
        self.material_cp_lbl.place(x=10, y=90)

        self.material_cp_ety = ttk.Entry(self.bottom, width=40)
        self.material_cp_ety.insert(0, 'Please enter the Cost Price of Material')
        self.material_cp_ety.place(x=170, y=90)


        # SELL PRICE of the material
        self.material_sp_lbl = Label(self.bottom, text="Sell Price of Material : ", bg="#FABC5F")
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

        if (material_name and material_qty and material_cp and material_sp) != "":
            try:
                query = "INSERT INTO 'Project_Inventory' (Material_name, Material_qty, Material_cp, Material_sp) VALUES(?,?,?,?)"
                crsr.execute(query, (material_name, material_qty, material_cp, material_sp))
                connection.commit()
                messagebox.showinfo("Success", "Successfully added to database", icon="info")

            except:
                messagebox.showerror("Error", "Can't add to database", icon="warning")
        else:
            messagebox.showerror("Error", "Fields can't be empty", icon="warning")