historico = []

renda = float(input("qual a sua renda esse mes? "))

while True:
    entrada = input("Informe: categoria/nome/valor (ex: comprei/tenis/250,50): ") 
    lista = entrada.split("/")
    categoria = entrada.split("/")[0]
    nome = entrada.split("/")[1]
    valor = entrada.split("/")[2]
    valor = float(valor.replace(",", ".")) 

    ficha = {"categoria": categoria, "nome": nome, "preco": valor}

    confirmar = input("os dados acima estão corretos? (s/n) ")
    if confirmar =="n":
          print("vamos recomecar!")
          continue
       
    historico.append(ficha)
    continuar = input("deseja adicionar mais algo?(s/n) ")
    if continuar == "n":
        break

total_compra_or_comprei = 0
total_pagamento = 0
for ficha in historico:
    if ficha["categoria"] == "compra" or ficha["categoria"] == "comprei":
        total_compra_or_comprei += ficha["preco"]
    else:
        total_pagamento += ficha["preco"]
print(f"Total de compra: R$ {total_compra_or_comprei:.2f}")
print(f"Total de pagamento: R$ {total_pagamento:.2f}")
saldo = renda - (total_compra_or_comprei + total_pagamento)
if saldo >= 0:
    print(f"Você ainda pode gastar R$ {saldo:.2f} sem ficar no vermelho")
else:
    print(f"Atenção: você está no vermelho em R$ {abs(saldo):.2f} por favor pare de gastar!")