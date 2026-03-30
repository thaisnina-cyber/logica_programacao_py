
# AND para ser TRUE tudo tem que ser true
# or para ser true, apenas uma da operações precisa ser verdadeira

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

saldo <= saque and saque <=limite or conta_especial and saldo >= saque

(saldo <= saque and saque <=limite)  or  (conta_especial and saldo >= saque)
