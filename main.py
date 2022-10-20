class Zmogus:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde

    def pasisveikinti(self):
        print(f"Sveiki, aš esu {self.vardas} {self.pavarde}")

    def __str__(self):
        return f"Žmogus {self.vardas} {self.pavarde}"


class Darbuotojas(Zmogus):
    def __init__(self, vardas, pavarde, atlyginimas):
        super().__init__(vardas, pavarde)
        self.atlyginimas = atlyginimas

    def pasisveikinti(self):
        super().pasisveikinti()
        print(f"Aš uždirbu {self.atlyginimas}")

    def __str__(self):
        return f"Aš esu darbuotojas {self.vardas} {self.pavarde}, mano atlyginimas - {self.atlyginimas}"


darbuotojas1 = Darbuotojas("Rokas", "Ranmantas", 4000)

darbuotojas1.pasisveikinti()


