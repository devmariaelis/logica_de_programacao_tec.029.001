nome = input("Informe seu nome: ")
nota1 = int(input("Informe sua primeira nota: "))
nota2 = int(input("Informe sua segunda nota: "))
media = (nota1 + nota2)/2
print(f"Media: {media}")
if media >= 7:
    print(f"{nome} está aprovado")
elif media >= 5:
    print(f"{nome} está de recuperação")
else:
    print(f"{nome} reprovado")