# Bsp. if
konto = 100

if konto < 100: 
    print("Wahrnung: Konto unter 100€")
else: 
    print("Information: Konto über 100€ -> investieren möglich")

# Bsp. Schleife
anlageAr = ["(1) Sparbuch", "(2) Aktie", "(3) Fond",
             "(4) Krypto", "(5) Nicht anlegen"]

for a in anlageAr: 
    print(a)


# Bsp. Break
eingabe = ['1', '2', '3', '4']

while True:
    benutzerAu = input("Wählen Sie eine Option aus: ")
    if benutzerAu in eingabe:
        print("Sie haben Option", benutzerAu, "gewählt.")
        break
    print("Fehlerhafte Eingabe -> investieren verpflichtet!")


# Bsp. Pass
x = 5
if x == 5 :
    pass # In Python darf ein Block nicht leer sein 


# Bsp. try-except
sorgen = 100
print("Sie haben", sorgen, "Sorgen")
divisor = input("Durch wie viel möchten Sie ihre Sorgen teilen (0-10)? ")


try: 
    divisor = int(divisor)
    sorgenNeu = sorgen / divisor

except ZeroDivisionError as e:
    print ("Error zu viele Sorgen!", e)

else: 
    print("Neue Sorgen", sorgenNeu)

    
    
    










