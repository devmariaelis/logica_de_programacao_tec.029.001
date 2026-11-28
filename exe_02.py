peso = float(input("Informe seu peso: ").replace(",","."))
massa = float(input("Informe sua massa: ").replace(",","."))
altura = float(input("Informe sua altura: ").replace(",","."))
imc = massa/(altura**2)
if imc <18.5:
    print("Usuário está abaixo do peso.")
elif imc <25:
    print("Usuário está no peso ideal.")
elif imc <30:
    print("Usuário está acima do peso.")
elif imc <35:
    print("Usuário está obeso.")
elif imc <40:
    print("Usuário está com obesidade nível 2.")
else:
    print("Usuário está com obesidade mórbida.")
