import customtkinter as ctk
from tkinter import *
from subprocess import call

bg = "#483D8B"

def ACHATS():
    root.destroy()

    call(["python", "Achats.py"])


def VENTES():
    root.destroy()
    
    call(["python", "Ventes.py"])

root = ctk.CTk()
root.title("GESTIONNAIRE")
root.geometry("600x200+400+200")
root.config(bg="#808080")
root.resizable(False, False)

titre = ctk.CTkLabel(root,
                     text="GESTIONNAIRES DES ACHATS ET VENTES",
                     font=("sans serif", 25, 'bold'), 
                     bg_color=bg
)
titre.place(x=45, y=20)

btn_achat = ctk.CTkButton(root,
                          text="ACHATS",
                          font=("sans serif", 23, 'bold'),
                          bg_color=bg,
                          corner_radius=20,
                          width=200,
                          command=ACHATS
)
btn_achat.place(x=80, y=100)

btn_vente = ctk.CTkButton(root,
                          text="VENTES",
                          font=("sans serif", 23, 'bold'),
                          bg_color=bg,
                          corner_radius=20,
                          width=200,
                          command=VENTES
)
btn_vente.place(x=330, y=100)

root.mainloop()