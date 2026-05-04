def numprimo(n):
    """
    Verifica se um número é primo.

    Esta função determina se o número fornecido é um número primo, ou seja,
    um número maior que 1 que não tem divisores positivos além de 1 e ele mesmo.

    Args:
        n (int): O número a ser verificado. Deve ser um inteiro não negativo.

    Returns:
        bool: True se o número for primo, False caso contrário.

    Raises:
        Nenhum erro é levantado, mas para n <= 1, retorna False.

    Example:
        >>> numprimo(7)
        True
        >>> numprimo(4)
        False
    """
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