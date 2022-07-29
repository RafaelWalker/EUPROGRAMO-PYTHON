while True:
 print("----------------------------------------------------")
 print("CALCULADORA V5.0")
 print("----------------------------------------------------")
 num1 = float(input("Digite o Primeiro valor: "))
 num2 = float(input("Digite o Segundo valor: "))
 print("DIGITE A OPÇÃO DE CALCULO ")
 print("1 PARA ADIÇÃO")
 print("2 PARA SUBTRAÇÃO")
 print("3 PARA MULTIPLICAÇÃO")
 print("4 PARA DIVISAO")
 print("")
 op = int(input("DIGITE A OPÇÃO: ")) 
 soma = num1 + num2
 sub = num1 - num2
 div = num1 / num2
 mult = num1 * num2 
 if op == 9:
  print("ATÉ A PRÓXIMA! OBRIGADO!!")
  break
 elif op == 1:
     print("O valor de {} + {} é = {:.2f}".format(num1,num2,soma))
 elif op == 2:
     print("O valor de {} - {} é = {:.2f}".format(num1,num2,sub)) 
 elif op == 3:
     print("O valor de {} X {} é = {:.2f}".format(num1,num2,mult))     
 elif op == 4:
     print("O valor de {} / {} é = {:.2f}".format(num1,num2,div))  
 else:
     print("")
     print("OPÇÃO INVÁLIDA")