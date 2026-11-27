gasolina = float(input("Informe o valor da gasolina: "))
etanol = float(input("Informe o valor do etanol: "))
if etanol <= 0.75 * gasolina:
    print("Abasteça com etanol")
else:
    print("Abateça com gasolina")