valor1 = float(input("digite o valor 1 "))
valor2 = float(input("digite o valor 2 "))
valor3 = float(input("digite o valor 3 "))
valor4 = float(input("digite o valor 4 "))
valor5 = float(input("digite o valor 5 "))
dinheiro_recebido = float(input("digite o valor do dinheiro recebido"))
soma = valor1+valor2+valor3+valor4+valor5
print("o total da compra e ", soma )
troco = dinheiro_recebido - soma
if troco > 0:
     print ("o valor do troco e ", troco)