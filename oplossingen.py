# Oplossingen voor Python Oefeningen

"""
Dit bestand bevat de oplossingen voor de oefeningen in oefeningen.py
Dit is bedoeld voor docenten.
"""

# Oefening 1: Maak een functie die twee getallen optelt
def tel_op(getal1, getal2):
    """
    Tel twee getallen op en geef het resultaat terug.
    
    Args:
        getal1: Het eerste getal
        getal2: Het tweede getal
        
    Returns:
        De som van getal1 en getal2
    """
    return getal1 + getal2


# Oefening 2: Maak een functie die controleert of een getal even is
def is_even(getal):
    """
    Controleer of een getal even is.
    
    Args:
        getal: Het getal om te controleren
        
    Returns:
        True als het getal even is, anders False
    """
    return getal % 2 == 0


# Oefening 3: Maak een functie die het grootste getal uit een lijst vindt
def vind_grootste(getallen):
    """
    Vind het grootste getal in een lijst.
    
    Args:
        getallen: Een lijst met getallen
        
    Returns:
        Het grootste getal uit de lijst
    """
    return max(getallen)
    # Alternatief zonder max():
    # grootste = getallen[0]
    # for getal in getallen:
    #     if getal > grootste:
    #         grootste = getal
    # return grootste


# Oefening 4: Maak een functie die een woord omkeert
def keer_om(woord):
    """
    Keer een woord om.
    
    Args:
        woord: Het woord om te keren
        
    Returns:
        Het omgekeerde woord
    """
    return woord[::-1]
    # Alternatief:
    # return ''.join(reversed(woord))


# Test de functies
if __name__ == "__main__":
    print("Test de oplossingen:")
    print(f"tel_op(5, 3) = {tel_op(5, 3)}")  # Verwacht: 8
    print(f"is_even(4) = {is_even(4)}")      # Verwacht: True
    print(f"is_even(7) = {is_even(7)}")      # Verwacht: False
    print(f"vind_grootste([1, 5, 3, 9, 2]) = {vind_grootste([1, 5, 3, 9, 2])}")  # Verwacht: 9
    print(f"keer_om('hallo') = {keer_om('hallo')}")  # Verwacht: 'ollah'
    
    # Alle tests moeten slagen
    assert tel_op(5, 3) == 8
    assert is_even(4) == True
    assert is_even(7) == False
    assert vind_grootste([1, 5, 3, 9, 2]) == 9
    assert keer_om('hallo') == 'ollah'
    
    print("\n✓ Alle tests geslaagd!")
