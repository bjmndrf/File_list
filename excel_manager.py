import xlsxwriter as xw

class Liste_Excel:

    def Createur_liste_excel(self, liste_fichier,adresse):

        classeur_1 = xw.Workbook(f"{adresse}/liste_des_fichiers.xlsx")
        liste_1 = classeur_1.add_worksheet("Dossier 1")
        liste_1.set_column("A:A",60)
        liste_1.set_column("B:D",45)
        row = 1
        liste_1.write("A1", "Nom du document")
        # liste_1.write("B1", "Type de modifications")
        # liste_1.write("C1","Quantité de modifications")
        # liste_1.write("D1", "Process / Utilitées")

        for item in range(0, len(liste_fichier)):
            liste_1.write(row, 0, f"{liste_fichier[item]}")
            row +=1
        classeur_1.close()