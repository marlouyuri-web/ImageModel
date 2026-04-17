def calcular_estatisticas(valores):
    if not valores:
        raise ValueError("A lista de valores não pode estar vazia.")

    total = sum(valores)
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