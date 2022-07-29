
print("----------------------------------------------------")
print("CALCULADORA V2.0")
print("----------------------------------------------------")
num1 = float(input("Digite o Primeiro valor: "))
num2 = float(input("Digite o Segundo valor: "))
soma = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
print("DIGITE A OPÇÃO DE CALCULO ")
print("1 PARA ADIÇÃO")
print("2 PARA SUBTRAÇÃO")
print("3 PARA MULTIPLICAÇÃO")
print("4 PARA DIVISAO")
op = int(input("Digite a opção: "))
if op == 1:
    print("O valor de {} + {} é = {:.2f}".format(num1,num2,soma))
if op == 2:
    print("O valor de {} - {} é = {:.2f}".format(num1,num2,sub)) 
if op == 3:
    print("O valor de {} X {} é = {:.2f}".format(num1,num2,mult))     
if op == 4:
    print("O valor de {} / {} é = {:.2f}".format(num1,num2,div))  
   
