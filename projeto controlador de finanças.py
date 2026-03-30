historico = []
while True:
    item = input("é despesa ou compra? ") 
    if item == "compra": 
        nome = input("o que comprou? ")
    else:
        nome = input("qual conta pagou? ")
    valor = float(input("quanto custou? ")) 
    ficha = {"categoria": item, "preço": valor, "nome": nome}
    confirmar = input("os dados acima estão corretos? (s/n)")
    if confirmar =="n":
          print("vamos recomeçar!")
          continue
    else:     
      historico.append(ficha)
    continuar = input("deseja adicionar mais algo?(s/n)")
    if continuar == "n":
        break
total_compra = 0
total_despesa = 0
for ficha in historico:
    if ficha["categoria"] == "compra":
        total_compra = total_compra + ficha["preço"]
    else:
        total_despesa = total_despesa + ficha["preço"]
print(f"Total de despesa: R$ {total_despesa:.2f}")
print(f"Total de compra: R$ {total_compra:.2f}")
    