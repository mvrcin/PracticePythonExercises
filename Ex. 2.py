# Marcin Piskuła
# Practicepython.org Ex. 2 - Odd or Even

digit = int(input("Wprowadz dowolna liczbe:"))
ooe = digit % 2 # ooe = odd or even

if ooe > 0:
    print("Liczba jest nieparzysta")
else:
    print("Liczba jest parzysta")
input("\nAby zakonczyc nacisnij klawisz Enter.")
