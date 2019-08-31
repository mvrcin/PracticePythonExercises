# Marcin Piskuła
# Practicepython.org Ex. 2 - Odd or Even

digit = int(input("Wprowadz dowolna liczbe:"))
# Use more readable variable names without comments. Something like 'result' instead of 'ooe'.
ooe = digit % 2 # ooe = odd or even

# The much more readable solution is:
if ooe == 1:
    print("Liczba jest nieparzysta")
elif ooe == 0:
    print("Liczba jest parzysta")
input("\nAby zakonczyc nacisnij klawisz Enter.")

# Try to make a new solution using Boolean Data Types. That would be professional way to solve this problem.
