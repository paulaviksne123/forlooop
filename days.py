#UZDEVUMS 2
#Pirmdiena vai Svētdiena
#Mūzikas skaļums var būt maksimāli 40 no 100
#Izveido Python progammu
#Kas prasa ievadīt Dienu
#Mūzikas skaļumu no 0 līdz 100
#tad informē vai ievadūts mūzikas skaļums ir atļauts

day = input("Ievadi dienu: ")
loudness = int(input("Ievadi skaļumu no 0 līdz 100: "))

silent_season = True 
if not silent_season : True

if day == "pirmdiena" or day == "svētdiena" and loudness > 40:
    print("Ļoti skaļi, vajag klusāk!")
else:
    print("Chill!")