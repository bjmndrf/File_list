from list_manager import ListeFichier
from excel_manager import Liste_Excel
from tkinter import *
from tkinter import messagebox


BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Créateur de liste de fichier")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



#adresse = r"C:\Users\bdurif\Desktop\hdf"

def creation():
    try:
        adresse =  adresse_entry.get()
        adresse = adresse.replace(r"\"","/")
        liste_de_fichier = ListeFichier()
        liste_de_fichier = liste_de_fichier.Createur_liste(adresse=adresse)
        liste_format_excel = Liste_Excel()
        liste_format_excel = liste_format_excel.Createur_liste_excel(liste_fichier=liste_de_fichier, adresse=adresse)
        print(liste_de_fichier)
        messagebox.showinfo(title="C'est fait", message=f"La liste des fichiers a été créé à l'adresse suivante {adresse}")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="L'adresse du dossier n'est pas correct")


adresse_label = Label(text="Addresse du dossier")
adresse_label.grid(row=0, column=0)
adresse_entry = Entry(width=35)
adresse_entry.grid(row=0, column=1)
adresse_entry.focus()
texte = adresse_entry.get()
print(texte)
creation_button = Button(text="Créer la liste de fichier", width=20,command=creation)
creation_button.grid(row=1, column=1 )






window.mainloop()