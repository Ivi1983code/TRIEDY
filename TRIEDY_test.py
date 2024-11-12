class Zvierata:
    def __init__(self, hmotnost, vek):
        self.hmotnost = hmotnost
        self.vek = vek

    def pozorovat(self):
        print("Pozorujem svoje okolie.")

    def dychat(self):
        print("Dýcham.")

    def zobraz_info(self):
        print(f"Hmotnosť: {self.hmotnost} kg, Vek: {self.vek} rokov")


class Ryba(Zvierata):
    def plavat(self):
        print("Plávam vo vode.")


class Cicavec(Zvierata):
    def behat(self):
        print("Bežím po zemi.")

    @staticmethod
    def info_o_cicavcoch():
        print("Cicavce sú teplokrvné zvieratá.")


class Vtak(Zvierata):
    def lietat(self):
        print("Lietam vo vzduchu.")



class prva_metoda_pokus:
    def zobraz_info(self):
        print("prva_metoda_pokus.")



class druha_metoda_pokus:
    def zobraz_info(self):
        print("druha_metoda_pokus.")



class DomaciMazlicek(prva_metoda_pokus, druha_metoda_pokus):
    pass



ryba = Ryba(1.5, 2)
cicavec = Cicavec(35, 10)
vtak = Vtak(0.5, 2)
pes = DomaciMazlicek()

print("Ryba:")
ryba.zobraz_info()
ryba.pozorovat()
ryba.dychat()
ryba.plavat()

print("Cicavec:")
cicavec.zobraz_info()
cicavec.pozorovat()
cicavec.dychat()
cicavec.behat()

print("Vták:")
vtak.zobraz_info()
vtak.pozorovat()
vtak.dychat()
vtak.lietat()

print("Domáci mazlíček:")
pes.zobraz_info()