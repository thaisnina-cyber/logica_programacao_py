historico = []
while True:
    item = input("é despesa ou compra? ") 
    if item == "compra": 
        nome = input("o que comprou? ")
    elif item == "despesa":    
        nome = input("qual conta pagou? ")
    else:  
        print("opção invalida, tente novamente")
        continue

    valor = float(input("quanto custou? ")) 

    ficha = {"categoria": item, "preco": valor, "nome": nome}

    confirmar = input("os dados acima estão corretos? (s/n) ")
    if confirmar =="n":
          print("vamos recomecar!")
          continue
       
    historico.append(ficha)
    continuar = input("deseja adicionar mais algo?(s/n) ")
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