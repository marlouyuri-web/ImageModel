def calcular_media(notas):
    # Verifica se a lista está vazia para evitar divisão por zero, retornando 0 como média padrão
    if len(notas) == 0:
        return 0
    
    soma = 0
    # Itera sobre cada nota para calcular a soma total, em vez de usar sum() para maior controle
    for nota in notas:
        soma += nota
    
    media = soma / len(notas)
    return media

# Entrada do usuário com validação de erro para lidar com entradas inválidas de forma robusta
try:
    entrada = input("Digite as notas separadas por vírgula: ")
    # Converte a entrada em lista de inteiros, removendo espaços extras para flexibilidade na entrada
    notas = [int(x.strip()) for x in entrada.split(',')]
    
    resultado = calcular_media(notas)
    print(f"A média das notas é: {resultado}")
    
except ValueError:
    # Trata especificamente erros de conversão para números, orientando o usuário
    print("Erro: Digite apenas números separados por vírgula!")
except Exception as e:
    # Captura qualquer outro erro inesperado para depuração
    print(f"Erro inesperado: {e}")
