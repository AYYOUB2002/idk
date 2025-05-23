class Etudiant :
    def __init__(self, nom, age, moyenne):
        self.nom = nom
        self.age = age
        self.moyenne = moyenne
    def afficher_details(self):
        print(f"Etudiant : {self.nom}, age : {self.age}, moyenne : {self.moyenne}")    




mon_Etudiant = Etudiant ("9ayoub", "102", "70")
mon_Etudiant.afficher_details() 