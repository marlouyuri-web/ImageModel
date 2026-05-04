def calcular_estatisticas(valores):
    """
    Calcula estatísticas básicas de uma lista de valores numéricos.

    Esta função recebe uma lista de números e calcula o total de elementos,
    a média aritmética, o maior e o menor valor.

    Args:
        valores (list[float] or list[int]): Lista de valores numéricos para calcular as estatísticas.

    Returns:
        tuple: Uma tupla contendo (total, media, maior, menor), onde:
            - total (int): Número total de elementos na lista.
            - media (float): Média aritmética dos valores.
            - maior (float or int): O maior valor na lista.
            - menor (float or int): O menor valor na lista.

    Raises:
        ValueError: Se a lista de valores estiver vazia.

    Example:
        >>> calcular_estatisticas([1, 2, 3, 4, 5])
        (5, 3.0, 5, 1)
    """
    if not valores:
        raise ValueError("A lista de valores não pode estar vazia.")

    total = len(valores)
    media = total / len(valores)
    maior = max(valores)
    menor = min(valores)

    return total, media, maior, menor


def main() -> None:
    numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, media, maior, menor = calcular_estatisticas(numeros)

    print("Total:", total)
    print("Média:", media)
    print("Maior:", maior)
    print("Menor:", menor)


if __name__ == "__main__":
    main()