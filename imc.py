peso = float(input("Informe o Peso em KG: "))
altura = float(input("Informe o Altura em m: "))
imc = peso / (altura * altura)
if (imc < 18.5):
    print("Abaixo do peso")
if (imc >= 18.5 and imc < 24.9):
    print("Normal")
if (imc >= 24.9 and imc <= 30):
    print("Sobrepeso")
if (imc > 30):
    print("Obesidade")