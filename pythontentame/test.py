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



# getal = int(input("voer getal in: "))
# result = getal % 7 
# if result == 0:
#     print("deelbaar" + str(result))
# else:
#     print("niet deelbaar, restant is: " + str(result))

# materiaal = str(input("voer een materiaal in: (Staal, Plastic, Random)")).casefold()
# if materiaal == "aluminium":
#     print("dichtheid is: 123")
# elif materiaal == "plastic":
#     print("dichtheid is: 330")
# elif materiaal == "random":
#     print("random shit")

# getal1 = input("getal 1: ")
# getal2 = input("getal 2: ")

# aantal_cijfers = len(getal1)
# print(aantal_cijfers, getal2)

# Stap 1: Maak een lijst met waarden
# waarden = ["appel", "banaan", "kers", "druif", "mango"]
# invoer = input("Voer een waarde in om te controleren: ").strip().lower()
# # Stap 3: Controleer of de invoer in de lijst voorkomt
# if invoer in waarden:
#     print(f"De waarde '{invoer}' komt voor in de lijst.")
# else:
#     print(f"De waarde '{invoer}' komt niet voor in de lijst.")

# getal = round(float(input("voer in ")),2)
# if 8 < getal < 10:
#     beoordeling = "A"
# elif 7 < getal < 8:
#     beoordeling = "B" 
# elif 5 < getal < 6:
#     beoordeling = "C"
# else:
#     beoordeling = "ieuw"
# print(beoordeling)

# Stap a: Ken het nummer 3 aan een variabele getal1 toe
# getal1 = int(input("voer getal in "))
# getal2 = int(input("voer getal in "))
# # Stap c: Zoek de maximale waarde uit de twee getallen
# maximaal = max(getal1, getal2)
# # Stap d: Bereken het maximale getal tot de macht 5
# uitkomst = pow(maximaal, 5)
# # Stap e: Print de som, inclusief de variabelen maximaal en uitkomst
# print(f"De maximale waarde is {maximaal} en {maximaal} tot de macht 5 is {uitkomst}.")

print(round((math.pi),2))





