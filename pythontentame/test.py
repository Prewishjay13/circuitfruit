import math
# massa = float(input("Massa: "))
# volume = float(input("volume: "))
# result = massa + volume
# print(str(result))

# num1 = float(input("getal 1: "))
# num2 = float(input("getal 2: "))
# result = num1 * num2
# print(result, type(result))

# Stap a: Vraag de gebruiker om een getal in te vullen en sla het op als integer
# getal = int(input("Voer een getal in voor de tafel: "))
# # Stap b: Bereken en print de tafel per regel
# #print(f"Tafel van {getal}:")
# for i in range(1, 11):  # Loop van 1 tot en met 10
#     print(f"{getal} x {i} = {getal * i}\t")  # Print de berekening en uitkomst



# Stap a: Vraag de gebruiker om de totale hoeveelheid geld en het aantal mensen
# geld = int(input("Voer het totale bedrag in (in euro's): "))
# mensen = int(input("Voer het aantal mensen in: "))
# # Stap b: Bereken hoeveel gehele euro's iedere persoon krijgt en de restwaarde
# gehele_euros_per_persoon = geld // mensen  # Gehele euro's per persoon
# restwaarde = geld % mensen  # Overblijvend bedrag
# # Print het resultaat
# print(f"Ieder persoon krijgt {gehele_euros_per_persoon} euro(s).")
# print(f"Het overblijvende bedrag is {restwaarde} euro(s).")

# massa = float(input('Voer de massa in kg in: '))
# c = 300000000**2
# E = massa * c
# print(f"E = m * c^2 = {massa} * 300000000^2 = {E} J")

# Stap a: Vraag om de straal van de cirkel
# straal = float(input("Voer de straal van de cirkel in (in meters): "))
# # Stap b: Bereken de oppervlakte van de cirkel
# oppervlakte = round((math.pi * straal**2),2)
# print(f"De oppervlakte van de cirkel is: {oppervlakte} m²")



getal = int(input("voer getal in: "))
result = getal % 7 
if result == 0:
    print("deelbaar" + str(result))
else:
    print("niet deelbaar, restant is: " + str(result))

