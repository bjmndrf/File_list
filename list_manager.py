from os import listdir
from os.path import isfile, join

class ListeFichier:

    def __init__(self):
        self.liste_fichier = []

    def Createur_liste(self,adresse):

        liste_fichier = [f for f in listdir(adresse) if isfile(join(adresse, f))]

        return liste_fichier
