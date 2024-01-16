
class Uzivatel ():
    def __init__(self,jmeno, prijmeni, vek, telefon ):
        self.jmeno=jmeno
        self.prijmeni=prijmeni
        self.vek=vek
        self.telefon=telefon

    def zpracuj_prikaz(self,prikaz):
        if prikaz.startswith("1"):
