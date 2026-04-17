def numprimo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

input_num = int(input("Ingrese um número: "))
if numprimo(input_num):
    print(f"{input_num} e um número primo.")
else:    
    print(f"{input_num} não é um número primo.")