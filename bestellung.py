import random

customers=["Jimmy","Kim","John","Staice"]
winner=random.choice(customers)
flavour="vanille";
print ("Congratulations "+winner+" you have won an ice cream sundae!")
prompt="Would you like a cherry on top?"
wants_cherry=input(prompt)
order=flavour+" sundae"
if(wants_cherry=='yes'):
    order=order + " with cherry on top"
    print("aktuelle Bestellung:", order)
print("One "+order+" for "+winner+" coming right up!")
