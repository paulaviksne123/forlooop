#UZDEVUMS 1
# Kino ieejas biļete maksā 10 eiro parasti
# ja tev ir mazāk vai vienāds par 12 vai 
# vairāk vai vienāds par 60
# tad maksā ar 50 % atlaidi
# uzstaisi programmu
# programma prasa ievadīt vecumu
# tad painformē kāda ir kino biļetes cena



ordinary_price = 14
discount = 0.5
discounted_price = ordinary_price * discount

name = input("Ievadi vārdu: ")

age = int(input("Ievadi savu vecumu: "))

if age <= 12 or age >= 60:
    print(f"Kino biļetes cena ir {discounted_price} eiro")
else:
    print(f"Kino biļetes cena ir {ordinary_price} eiro")
