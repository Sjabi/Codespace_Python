"""
Welkom bij Python Programmeren!

Dit is een voorbeeldbestand om je te helpen beginnen met Python.
"""

# Voorbeeld 1: Een eenvoudig "Hallo Wereld" programma
print("Hallo, Wereld!")

# Voorbeeld 2: Variabelen gebruiken
naam = "Student"
leeftijd = 15
print(f"Hallo {naam}, je bent {leeftijd} jaar oud!")

# Voorbeeld 3: Rekenen met Python
a = 10
b = 5
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")

# Voorbeeld 4: Een eenvoudige functie
def begroet(naam):
    """Begroet een persoon met hun naam."""
    return f"Hallo, {naam}! Leuk je te ontmoeten."

print(begroet("Python Student"))

# Voorbeeld 5: Een lijst gebruiken
favoriete_kleuren = ["rood", "blauw", "groen", "geel"]
print("Mijn favoriete kleuren zijn:")
for kleur in favoriete_kleuren:
    print(f"  - {kleur}")

# Voorbeeld 6: Input van de gebruiker
# Uncomment de volgende regels om input te vragen:
# jouw_naam = input("Wat is jouw naam? ")
# print(f"Welkom, {jouw_naam}!")
