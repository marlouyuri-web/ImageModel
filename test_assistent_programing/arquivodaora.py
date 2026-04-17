def Imc(peso,altura):
    imc = peso / (altura * 2)
    return print(f"Seu IMC é: {imc:.2f}")

input_peso = float(input("Digite seu peso em kg: "))
input_altura = float(input("Digite sua altura em metros: "))
Imc(input_peso, input_altura)