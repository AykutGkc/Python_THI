import math

name = input("Wie heißt der Hund: ")
dog_age = int(input("Wie alt ist der Hund: "))

#berechnung des Hundealters in Menschenjahren

"""
Die neue Formel der Forscher lautet daher:
Menschenalter = 16 x ln(Hundealter) + 31.
Dabei haben sie den natürlichen Logarithmus der
Hundejahre mit 16 multipliziert und dann 31 addiert.
"""

 #human_age = dog_age *7

human_age=16* math.log(dog_age) + 31
print("Dann ist der Hund", human_age,"Menschenjahre alt")
