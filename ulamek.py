import math
class Ułamek:
    def __init__(self, licznik, mianownik):
        assert(mianownik != 0)
        if licznik == 0:
            self.licznik = 0
            self.mianownik = 1
        else:
            gcd = math.gcd(licznik, mianownik)
            if mianownik < 0:
                gcd = -gcd
            self.licznik = licznik//gcd
            self.mianownik = mianownik//gcd

    def __str__(self):
        return f"{self.licznik}/{self.mianownik}"

    def __repr__(self):
        return f"{self.licznik}/{self.mianownik}"
    
    def __mul__(self, y):
        if self.licznik == 0 or y.licznik == 0:
            return Ułamek(0,1)
        nlicznik = self.licznik * y.licznik
        nmianownik = self.mianownik * y.mianownik
        return Ułamek(nlicznik, nmianownik)

    def __truediv__(self, y):
        assert(y.licznik != 0)
        if(self.licznik == 0):
            return Ułamek(0,1)
        nlicznik = self.licznik * y.mianownik
        nmianownik = self.mianownik * y.licznik
        return Ułamek(nlicznik, nmianownik)

    def __add__(self, y):
        nlicznik = self.licznik * y.mianownik + self.mianownik * y.licznik
        nmianownik = self.mianownik * y.mianownik
        return Ułamek(nlicznik, nmianownik)

    def __sub__(self, y):
        nlicznik = self.licznik * y.mianownik - self.mianownik * y.licznik
        nmianownik = self.mianownik * y.mianownik
        return Ułamek(nlicznik, nmianownik)

    def __le__(self, y):
        if self.licznik * y.mianownik <= self.mianownik * y.licznik:
            return True
        return False

    def __ge__(self, y):
        if self.licznik * y.mianownik >= self.mianownik * y.licznik:
            return True
        return False

    def __lt__(self, y):
        if self.licznik * y.mianownik < self.mianownik * y.licznik:
            return True
        return False
    
    def __gt__(self, y):
        if self.licznik * y.mianownik > self.mianownik * y.licznik:
            return True
        return False
    
    def __eq__(self, y):
        if self.licznik * y.mianownik == self.mianownik * y.licznik:
            return True
        return False

    def __ne__(self, y):
        if self.licznik * y.mianownik != self.mianownik * y.licznik:
            return True
        return False


if __name__ == "__main__":
    a = Ułamek(2, -15)
    b = Ułamek(5, 6)

    print("a =", a)
    print("b =", b)
    print("a * b =", a * b)
    print("a / b =", a / b)
    print("a + b =", a + b)
    print("a - b =", a - b)

    assert str(a * b) == "-1/9"
    assert str(a / b) == "-4/25"
    assert str(a + b) == "7/10"
    assert str(a - b) == "-29/30"

    print("a <= b:", a <= b)
    print("a >= b:", a >= b)
    print("a < b:", a < b)
    print("a > b:", a > b)
    print("a == b:", a == b)
    print("a != b:", a != b)

    assert a <= b
    assert not (a >= b)
    assert a < b
    assert not (a > b)
    assert not (a == b)
    assert a != b

    print("str(a) =", str(a))
    print("repr(a) =", repr(a))

    assert str(a) == "-2/15"
    assert repr(a) == "-2/15"
    assert (a.licznik, a.mianownik) == (-2, 15)
    assert (b.licznik, b.mianownik) == (5, 6)

    print("Wszystkie testy przeszly.")

