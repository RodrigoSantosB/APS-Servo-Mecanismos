# Routh-Hurwitz Algorithm

Este projeto implementa o **Critério de Routh-Hurwitz** em Python para determinar a estabilidade de sistemas dinâmicos.

## Sobre o Método de Routh-Hurwitz
O critério de Routh-Hurwitz é usado para verificar a estabilidade de um sistema dinâmico analisando o polinômio característico do denominador da função de transferência:

$P(s) = a_n s^n + a_{n-1} s^{n-1} + \dots + a_1 s + a_0$


O sistema é **estável** se e somente se todos os polos tiverem parte real negativa, o que acontece quando todos os elementos da primeira coluna da Tabela de Routh têm o mesmo sinal.

### Construção da Tabela de Routh
1. A primeira linha contém os coeficientes do polinômio característico, alternando entre os termos de maior e menor grau.
2. A segunda linha contém os coeficientes restantes.
3. As linhas subsequentes são preenchidas utilizando a equação:


$R_{i,j} = \frac{(R_{i-2,1} \cdot R_{i-1,j+1}) - (R_{i-1,1} \cdot R_{i-2,j+1})}{R_{i-1,1}}$

onde \( R_{i,j} \) representa os elementos da Tabela de Routh.

### Determinação da Estabilidade
Após construir a tabela, observamos a **primeira coluna**:
- Se todos os elementos forem **positivos ou negativos**, o sistema é estável.
- Se houver **mudança de sinal**, o sistema é instável, e o número de mudanças indica quantos polos têm parte real positiva.

### Tratamento de Casos Especiais
1. **Se o primeiro elemento da linha for zero:**
   - Inverte-se os coeficientes do polinômio.
   - Se o problema persistir, o código retorna uma mensagem de erro.
2. **Se uma linha inteira for zero:**
   - Indica a presença de polos imaginários puros.

---

## Como Executar o Código

### Requisitos
- Python 3
- Biblioteca NumPy

### Passos
1. Clone este repositório `https://github.com/RodrigoSantosB/APS-Servo-Mecanismos.git`.
2. Execute o código com o seguinte comando:
   ```bash
   python3 main.py
   ```
3. O programa exibirá um menu interativo:
   - **Opção 1:** Permite inserir os coeficientes do polinômio.
   - **Opção 2:** Encerra a execução.

### Exemplo de Uso
Ao rodar o programa e inserir os coeficientes `3 9 6 4 7 8 2 6`, a saída pode ser:
```
Matriz de entrada:
[3. 9. 6. 4. 7. 8. 2. 6.]

Tabela de Routh-Hurwitz:
| 3.         | 6.          |7.          |2.        |
| 9.         | 4.          |8.          |6.        |
| 4.66666667 | 4.33333333  |0.          |0.        |
|-4.35714286 | 8.          |6.          |0.        |
|12.90163934 | 6.42622951  |0.          |0.        |
|10.17026684 | 6.          |0.          |0.        |
|-1.18515742 | 0.          |0.          |0.        |
| 6.         | 0.          |0.          |0.        |

Resultado:
Sistema Instável com 4 polos no semiplano direito.
```
