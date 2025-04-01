import numpy as np
from RouthHurwitzAlgorithm import routh_hurwitz


def main():
    # Menu interativo para entrada dos coeficientes
    while True:
        print("\nAnálise de Estabilidade pelo Método de Routh-Hurwitz")
        print("1. Inserir coeficientes do polinômio")
        print("2. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            coef_str = input("Digite os coeficientes do polinômio separados por espaço: ")
            coeffs = list(map(float, coef_str.split()))
            routh_hurwitz(coeffs)
        elif opcao == "2":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
