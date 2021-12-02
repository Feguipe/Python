Base = float(input('Digite o valor da base '))
Altura = float(input('Digite o valor da altura'))

Area= Base*Altura
if Area < 100:
    print ("Terreno pequeno ")
if Area > 100:
   print("Terreno grande")