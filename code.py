historico = []

while True:
    item = input("É despesa ou compra? ")

    if item == "compra":
        nome = input("O que comprou? ")
    elif item == "despesa":
        nome = input("Qual conta pagou? ")
    else:
        print("Opção inválida, tente novamente.")
        continue

    valor = float(input("Quanto custou? "))

    ficha = {"categoria": item, "nome": nome, "preco": valor}

    confirmar = input("Os dados acima estão corretos? (s/n) ")
    if confirmar == "n":
        print("Vamos recomeçar!")
        continue

    historico.append(ficha)

    continuar = input("Deseja adicionar mais algo? (s/n) ")
    if continuar == "n":
        break

total_compra = 0
total_despesa = 0

for ficha in historico:
    if ficha["categoria"] == "compra":
        total_compra += ficha["preco"]
    else:
        total_despesa += ficha["preco"]

print(f"Total de despesa: R$ {total_despesa:.2f}")
print(f"Total de compra: R$ {total_compra:.2f}")