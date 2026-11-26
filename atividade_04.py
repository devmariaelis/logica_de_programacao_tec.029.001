massa = float(input("Informe sua massa: "))
altura = float(input("Informe sua altura: ").replace(",","."))
if massa <= 140 and altura >= 1.15:
   print("Entrada do usuário permitida")
else:
   print("Entrada do usuário negada") 