import customtkinter as ctk
from tkinter import *
from cProfile import label
from tkinter import ttk, Tk, messagebox
from subprocess import call
import mysql.connector


def Return():
    root.destroy()
    call("python", "Acceuil.py")


def Ajouter():

    num_achat = num_enter.get()
    fournisseur = fournisseur_enter.get()
    telephone = telephone_enter.get()
    produit = produit_combo.get()
    prix_achat = prix_enter.get()
    quantite = quantite_enter.get()

    mabase = mysql.connector.connect(host="localhost", user="root", password="1234", database="gestionnaire")
    moncursor = mabase.cursor()

    print("La connection a la base des donnees a ete etablie !!!")

    try:
        sql = "INSERT INTO achats (num_achat, fournisseur, telephone, produit, prix_achat, quantite) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (num_achat, fournisseur, telephone, produit, prix_achat, quantite)
        moncursor.execute(sql, val)
        mabase.commit()
        dernierId = moncursor.lastrowid
        messagebox.showinfo("Felicitation", "L'achat a ete ajoute")

        num_enter.delete(0, END)
        fournisseur_enter.delete(0, END)
        telephone_enter.delete(0, END)
        produit_combo.delete(0, END)
        prix_enter.delete(0, END)
        quantite_enter.delete(0, END)
        
    except Exception as e:
       print(e)
       #retour de la base
       mabase.rollback()
       mabase.close()


def Edition():
    num_achat = num_enter.get()
    fournisseur = fournisseur_enter.get()
    telephone = telephone_enter.get()
    produit = produit_combo.get()
    prix_achat = prix_enter.get()
    quantite = quantite_enter.get()
    
    mabase = mysql.connector.connect(host="localhost", user="root", password="1234", database="gestionnaire")
    moncursor = mabase.cursor()

    try:
       sql = "UPDATE achats SET fournisseur=%s, telephone=%s, produit=%s, prix_achat=%s, quantite=%s WHERE num_achat=%s"
       val = (fournisseur, telephone, produit, prix_achat, quantite, num_achat)

       moncursor.execute(sql, val)
       mabase.commit()
       dernierId = moncursor.lastrowid
       messagebox.showinfo("information", "Les modifications apportees ont ete effectuees !")


       num_enter.delete(0, END)
       fournisseur_enter.delete(0, END)
       telephone_enter.delete(0, END)
       produit_combo.delete(0, END)
       prix_enter.delete(0, END)
       quantite_enter.delete(0, END)

    except Exception as e:
        print(e)
        mabase.rollback()
        mabase.close()


def Effacer():
    num_achats = num_enter.get()

    mabase = mysql.connector.connect(host="localhost", user="root", password="1234", database="gestionnaire")
    moncursor = mabase.cursor()

    try:
        sql = "DELETE FROM achats WHERE (num_achat = %s)"
        val = num_achats
       
        moncursor.execute(sql, val)
        mabase.commit()
        dernierId = moncursor.lastrowid
        messagebox.showinfo("Attention", "Voullez-vous supprimer ? cette action est irreversible")

    except Exception as e:
        print(e)
        mabase.rollback()
        mabase.close()


bg = "#483D8B"
bg_conf = "#808080"

root = ctk.CTk()
root.title("Gestion des achats")
root.geometry("1350x650+0+10")
root.resizable(False, False)
root.config(bg=bg_conf)


titre = ctk.CTkLabel(root,
                     text="GESTIONNAIRES DES ACHATS",
                     font=("sans serif", 30, 'bold'),
                     bg_color=bg,
                     width=1350, 
                     height=100
)
titre.place(x=0, y=0)

num_lbl = ctk.CTkLabel(root,
                       text="Identifiant",
                       font=("Arial", 18, 'bold'),
                       bg_color=bg_conf,
                       width=150
)
num_lbl.place(x=70, y=150)

num_enter = ctk.CTkEntry(root,
                         border_width=3,
                         font=("Arial", 14),
                         width=150,
                         fg_color="#fff",
                         text_color="#000"
)
num_enter.place(x=200, y=150)


fournisseur_lbl = ctk.CTkLabel(root,
                       text="Fournisseur",
                       font=("Arial", 18, 'bold'),
                       bg_color=bg_conf,
                       width=150
)
fournisseur_lbl.place(x=70, y=200)

fournisseur_enter = ctk.CTkEntry(root,
                         border_width=3,
                         font=("Arial", 14),
                         width=150,
                         fg_color="#fff",
                         text_color="#000"
)
fournisseur_enter.place(x=200, y=200)


telephone_lbl = ctk.CTkLabel(root,
                       text="Telephone",
                       font=("Arial", 18, 'bold'),
                       bg_color=bg_conf,
                       width=150
)
telephone_lbl.place(x=70, y=250)

telephone_enter = ctk.CTkEntry(root,
                         border_width=3,
                         font=("Arial", 14),
                         width=150,
                         fg_color="#fff",
                         text_color="#000"
)
telephone_enter.place(x=200, y=250)


produit_lbl = ctk.CTkLabel(root,
                       text="Produit",
                       font=("Arial", 18, 'bold'),
                       bg_color=bg_conf,
                       width=150
)
produit_lbl.place(x=450, y=150)

produit_combo = ttk.Combobox(root,
                            font=("Arial", 12),
                            width=15
)
produit_combo['values'] = ['Iphone 12', 'Iphone 12 pro', 'Iphone 13', 'Iphone 13 pro', 'Iphone 14', 'Iphone 14 pro', 'Iphone 15', 'Iphone 15 pro']
produit_combo.place(x=600, y=150)


prix_lbl = ctk.CTkLabel(root,
                       text="Prix",
                       font=("Arial", 18, 'bold'),
                       bg_color=bg_conf,
                       width=150
)
prix_lbl.place(x=450, y=200)

prix_enter = ctk.CTkEntry(root,
                         border_width=3,
                         font=("Arial", 14),
                         width=150,
                         fg_color="#fff",
                         text_color="#000"
)
prix_enter.place(x=600, y=200)


quantite_lbl = ctk.CTkLabel(root,
                       text="Quantite",
                       font=("Arial", 18, 'bold'),
                       bg_color=bg_conf,
                       width=150
)
quantite_lbl.place(x=450, y=250)

quantite_enter = ctk.CTkEntry(root,
                         border_width=3,
                         font=("Arial", 14),
                         width=150,
                         fg_color="#fff",
                         text_color="#000"
)
quantite_enter.place(x=600, y=250)

btn_save = ctk.CTkButton(root,
                         text="Enregister",
                         font=("Arial", 16, 'bold'),
                         fg_color=bg,
                         width=200,
                         command=Ajouter
)
btn_save.place(x=850, y=150)

btn_edite = ctk.CTkButton(root,
                         text="Modifier",
                         font=("Arial", 16, 'bold'),
                         fg_color=bg,
                         width=200,
)
btn_edite.place(x=850, y=200)

btn_delete = ctk.CTkButton(root,
                         text="Supprimer",
                         font=("Arial", 16, 'bold'),
                         fg_color=bg,
                         width=200,
                         command=Effacer
)
btn_delete.place(x=850, y=250)

def Come_back():
    root.destroy()

    call(["python", "Achats.py"])

btn_comeback = ctk.CTkButton(root,
                         text="Actualiser",
                         font=("Arial", 16, 'bold'),
                         fg_color=bg,
                         width=200,
                         command=Come_back
)
btn_comeback.place(x=1100, y=250)

def Return():
    root.destroy()

    call(["python", "Acceuil.py"])

btn_retour = ctk.CTkButton(root,
                            text="Retour",
                            font=("Arial", 16, 'bold'),
                            fg_color=bg,
                            width=200,
                            command=Return
)
btn_retour.place(x=1100, y=200)


table = ttk.Treeview(root,
                     columns=(1, 2, 3, 4, 5, 6),
                     height=10, show="headings"
)
table.place(x=0,y=290, width=1350, height=360)

#definir le nom de l'entete de la table des donnees
table.heading(1, text="Identifiant")
table.heading(2, text="Fournisseur")
table.heading(3, text="Telephone")
table.heading(4, text="Produit")
table.heading(5, text="Prix")
table.heading(6, text="Quantite")

#definir une dimension\taille pour chaque colones de text
table.column(1, width=50)
table.column(2, width=150)
table.column(3, width=150)
table.column(4, width=150)
table.column(5, width=50)
table.column(6, width=50)

mabase = mysql.connector.connect(host="localhost", user="root", password="1234", database="gestionnaire")
moncursor = mabase.cursor()
moncursor.execute("SELECT * FROM achats")

for row in moncursor:
    table.insert('', END, value=row)

mabase.close()

root.mainloop()