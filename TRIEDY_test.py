from abc import ABC, abstractmethod

class Zvierata(ABC):
    celkova_vaha = 0
    zvierata_pribrali = []

    def __init__(self, hmotnost, vek):
        self.hmotnost = hmotnost
        self.vek = vek
        Zvierata.celkova_vaha += self.hmotnost
        Zvierata.zvierata_pribrali.append(self)

    def pozorovat(self):
        print("Pozorujem svoje okolie.")

    def dychat(self):
        print("Dýcham.")

    def zobraz_info(self):
        print(f"Hmotnosť: {self.hmotnost} kg, Vek: {self.vek} rokov")

    @abstractmethod
    def nastavit_hmotnost(self,nova_hmotnost):
        pass

    @classmethod
    def pribrali(cls):
        for zviera in cls.zvierata_pribrali:
            zviera.hmotnost += 2
            cls.celkova_vaha += 2


class Ryba(Zvierata):
    def plavat(self):
        print("Plávam vo vode.")


class Cicavec(Zvierata):
    def behat(self):
        print("Bežím .")

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


print(f"Celkova vaha vsetkych zvierat pred pribratim: {Zvierata.celkova_vaha} kg")

Zvierata.pribrali()

print(f"Celkova vaha vsetkych zvierat po pribrati: {Zvierata.celkova_vaha} kg")


print("Aktualizovaná hmotnosť každého zvieraťa:")
ryba.zobraz_info()
cicavec.zobraz_info()
vtak.zobraz_info()

