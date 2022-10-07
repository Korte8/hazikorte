from enum import Enum


class Packaging(Enum):
    PACKAGING = "5 dl"

    def __str__(self):
        return self.value


class Ital:
    name: str
    _packaging: Packaging
    __prize: int
    lst = []

    def __init__(self, name: str, packaging: Packaging, prize: int) -> None:
        self.name = name
        self._packaging = packaging
        self.__prize = prize

    def get_prize(self) -> int:
        return Ital.__prize

    def set_prize(self, value: int) -> None:
        Ital.__prize = value

    def get_packaging(self):
        return Ital._packaging

    prize = property(get_prize, set_prize)
    packaging = property(get_packaging)

    def __repr__(self) -> str:
        return f"Ital({self.name}, {self._packaging}, {self.__prize})"

    def __str__(self) -> str:
        return f"{self.name}, {self._packaging}, {self.__prize} Ft"

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Ital):
            return False
        return self.name == o.name and self._packaging == o._packaging and self.__prize == o.__prize

    def __hash__(self) -> int:
        return self.name.__hash__()

    def ne(self, o: object) -> bool:
        return not self.__eq__(o)

    def lt(self, other: object) -> bool:
        if not isinstance(other, Ital):
            return NotImplemented
        return self.__prize > other.__prize

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Ital):
            return NotImplemented
        return self.name < other.name and self._packaging < other._packaging

    @staticmethod
    def get_italok(ital: list[lst], nev) -> list[lst]:
        ret = []
        for italok in ital:
            if italok.name == nev:
                ret.append(italok._packaging)
        return ret


class Szeszesital(Ital):
    __alk = float

    def set_alk(self, alk: float):
        self.__alk = alk

    def get_alk(self):
        return self.__alk

    alk = property(get_alk, set_alk)

    def __init__(self, name: str, packaging: Packaging, prize: int, alk: float) -> None:
        super().__init__(name, packaging, prize)
        self.alk = alk

    def __repr__(self) -> str:
        return f"{self.alk}" + super().__repr__()

    def __str__(self) -> str:
        return  f"{self.alk}% alkoholtartalmú " + super().__str__()


def main():
    p1 = Ital("Doca-Cola", 4, 20)
    p2 = Ital("Doca-Cola", 6, 21)
    p3 = Ital("Pepsi", 5, 18)
    p4 = Szeszesital("Kékfrankos", "0,75 l", 20, 11.5)



if __name__ == "__main__":
    main()
