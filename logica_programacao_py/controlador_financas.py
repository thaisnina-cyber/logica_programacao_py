historico = []

renda = float(input("qual a sua renda esse mes? "))


while True: 
    categoria = input("fixo ou variavel? ").lower()
    if categoria.lower() == "sair":
        break
    nome = input("informe o nome: ")
    valor = input("digite o valor: ")
   
    valor = float(valor.replace(",", ".")) 
    
    ficha = {"categoria": categoria, "nome": nome, "preco": valor}
    
    historico.append(ficha)
    for indice, item in enumerate(historico, 1):
        print(f"{indice} - Categoria: {item['categoria']} | Nome: {item['nome']} | Valor: R$ {item['preco']:.2f}")
    

total_fixo = 0
total_variavel = 0
for ficha in historico:
    if ficha["categoria"] == "fixo" :
        total_fixo += ficha["preco"]
    else:
        total_variavel += ficha["preco"]
print(f"Total fixo: R$ {total_fixo:.2f}")
print(f"Total variavel: R$ {total_variavel:.2f}")
saldo = renda - (total_fixo + total_variavel)
if saldo >= 0:
    print(f"Você ainda pode gastar R$ {saldo:.2f} sem ficar no vermelho")
else:
    print(f"Atenção: você está no vermelho em R$ {abs(saldo):.2f} por favor pare de gastar!")