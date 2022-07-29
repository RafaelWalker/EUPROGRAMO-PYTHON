
print("----------------------------------------------------")
print("CALCULADORA V4.0")
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

match op: # a variável que iremos avaliar

  case 1: # case a variável tenha esse valor executa o código abaixo
    print("O valor de {} + {} é = {:.2f}".format(num1,num2,soma))

  case 2:
   print("O valor de {} - {} é = {:.2f}".format(num1,num2,sub))
 
  case 3:
    print("O valor de {} X {} é = {:.2f}".format(num1,num2,mult))
    
  case 4:
    print("O valor de {} / {} é = {:.2f}".format(num1,num2,div))
  
  case _: 
    print("OPÇÃO INVÁLIDA")
    