import numpy as np
from RouthHurwitzAlgorithm import routh_hurwitz


def main():
    while True:
        print("\n=== Menu ===")
        print("1. Calcular estabilidade de um sistema")
        print("2. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "2":
            print("Encerrando o programa...")
            break
        elif opcao == "1":
            try:
                entrada = input("Digite os coeficientes do polinômio separados por espaço: ")
                coefficients = list(map(float, entrada.split()))
                resultado, tabela = routh_hurwitz(coefficients)
                
                print("\nMatriz de entrada:")
                print(np.array(coefficients))
                print("\nTabela de Routh-Hurwitz:")
                print(tabela)
                print("\nResultado:")
                print(resultado)
            except Exception as e:
                print("Erro ao processar a entrada. Certifique-se de inserir coeficientes válidos.", e)
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
