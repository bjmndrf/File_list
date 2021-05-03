# File_list
Creating the file list of a folder using python.

The main.py contains the GUI via Tkinter, and the "creation" function.

The GUI is very basic, only the 3 following items:
  1 label "Addresse du dossier" (which is the french for "Folder location")
  2 An entry, where the user copy past the folder (the one he want to have the file list)
  3 A button labelled "Créer la liste de fichier" (File list creation), this button once you clicked on it triggered the "creation function"
  
 The "creation function" creates in the folder location (the one the user want to have the file list) an excel list, if the address does not exist a popup feedback is given.
 
 list_manager.py create the file list form a given folder location.
 
 Excel_manager.py put the list from list manager into an excel sheet (one cells by items)
