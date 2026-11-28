gasolina = float(input("Informe o valor da gasolina: ").replace(",","."))
etanol = float(input("Informe o valor do etanol: ").replace(",","."))
if etanol <= 0.75 * gasolina:
    print("Abasteça com etanol")
else:
    print("Abateça com gasolina")