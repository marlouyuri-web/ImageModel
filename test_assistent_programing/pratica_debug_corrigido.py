def calcular_media(notas):
    if len(notas) == 0:
        return 0
    
    soma = 0
    for nota in notas:
        soma += nota
    
    media = soma / len(notas)
    return media

# Entrada do usuário com validação de erro
try:
    entrada = input("Digite as notas separadas por vírgula: ")
    notas = [int(x.strip()) for x in entrada.split(',')]
    
    resultado = calcular_media(notas)
    print(f"A média das notas é: {resultado}")
    
except ValueError:
    print("Erro: Digite apenas números separados por vírgula!")
except Exception as e:
    print(f"Erro inesperado: {e}")
