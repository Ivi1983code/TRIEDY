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
        print("Cicavce")


class Vtak(Zvierata):
    def lietat(self):
        print("Lietam vo vzduchu.")


class DomaciPes(Cicavec):
    def __init__(self, hmotnost, vek, plemeno, farba_srst):
        super().__init__(hmotnost, vek)
        self.plemeno = plemeno
        self.farba_srst = farba_srst

    def stekat(self):
        print("Štekám.")

    def priniest(self):
        print("Prinášam predmet.")

    def zobraz_info(self):
        super().zobraz_info()
        print(f"Plemeno: {self.plemeno}, Farba srsti: {self.farba_srst}")



ryba = Ryba(1.5, 2)
cicavec = Cicavec(35, 10)
vtak = Vtak(0.5, 2)
pes = DomaciPes(30, 6, "ŠPIC", "biela")

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

print("Domáci pes:")
pes.zobraz_info()
pes.pozorovat()
pes.dychat()
pes.behat()
pes.stekat()
pes.priniest()