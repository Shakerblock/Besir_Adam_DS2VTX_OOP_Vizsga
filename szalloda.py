from datetime import datetime


class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, felszereltseg):
        super().__init__(szobaszam, ar=50000)
        self.felszereltseg = felszereltseg


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, felszereltseg):
        super().__init__(szobaszam, ar=80000)
        self.felszereltseg = felszereltseg


class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def uj_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglal(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                if datum < datetime.now():
                    return "A dátum érvénytelen, csak jövőbeni foglalás lehetséges."

                for foglalas in self.foglalasok:
                    if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                        return "A szoba már foglalt ezen a napon."

                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return f"Foglalás sikeres, az ár: {szoba.ar}."

        return "Nincs ilyen szoba."

    def lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return "Lemondás sikeres."

        return "Nincs ilyen foglalás."

    def foglalasok_listazasa(self):
        for foglalas in self.foglalasok:
            print(f"Szobaszám: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")


szallo = Szalloda("Nagyon jó szálloda!")
szallo.uj_szoba(EgyagyasSzoba(szobaszam=101, felszereltseg="Széffel rendelkezik."))
szallo.uj_szoba(KetagyasSzoba(szobaszam=201, felszereltseg="Hűtött pezsgővel."))
szallo.uj_szoba(EgyagyasSzoba(szobaszam=102, felszereltseg="Széffel rendelkezik."))

szallo.foglal(szobaszam=101, datum=datetime(2023, 12, 1))
szallo.foglal(szobaszam=201, datum=datetime(2023, 12, 2))
szallo.foglal(szobaszam=101, datum=datetime(2023, 12, 3))
szallo.foglal(szobaszam=102, datum=datetime(2023, 12, 4))
szallo.foglal(szobaszam=201, datum=datetime(2023, 12, 5))


while True:
    print("\n1. Foglalás")
    print("2. Lemondás")
    print("3. Foglalások listázása")
    print("4. Kilépés")

    valasztas = input("Válassz egy műveletet (1-4): ")

    if valasztas == "1":
        szobaszam = int(input("Add meg a szobaszámot: "))
        szobaszam = szobaszam
        datum_str = input("Add meg a foglalás dátumát (ÉÉÉÉ-HH-NN): ")
        datum = datetime.strptime(datum_str, "%Y-%m-%d")

        if datum < datetime.now():
            print("A dátum érvénytelen, csak jövőbeni foglalás lehetséges.")
        else:
            print(szallo.foglal(szobaszam, datum))

    elif valasztas == "2":
        szobaszam = int(input("Add meg a szobaszámot: "))
        szobaszam = szobaszam
        datum_str = input("Add meg a foglalás dátumát (ÉÉÉÉ-HH-NN): ")
        datum = datetime.strptime(datum_str, "%Y-%m-%d")

        print(szallo.lemondas(szobaszam, datum))

    elif valasztas == "3":
        szallo.foglalasok_listazasa()

    elif valasztas == "4":
        break

    else:
        print("Érvénytelen választás. Kérlek, válassz újra.")
