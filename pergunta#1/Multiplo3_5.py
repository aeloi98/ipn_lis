import sys
from math import floor

'''
Os múltiplos de um número x até n podem ser descritos como x * (1,2,3...m) sendo m = x/n.
Com esta observação percebemos que é nos possível descrever o problema #1 sem necessidade de percorrer uma array de números até n-1 dado.
Portanto:
1 - Encontrar o número de múltiplos de x até n-1 e guardar em m
2 - Somar todos os números naturais até o resultado obtido (1+2+3...+m) com a expressão do somatório dos números naturais até m: (m*(m+1)/2) 
3 - Executar a distribuição de x sobre esse resultado: x*(m(m+1)/2)

'''

def Multiplo3_5(max):
    #Encontrar o número de múltiplos de 3 até max -1.
    nMulti3 = floor((max-1) / 3)
    #Encontrar o número de múltiplos de 5 até max -1.
    nMulti5 = floor((max-1) / 5)
    
    #A soma dos números naturais até n é dado por (n(n+1)/2)
    sumNMulti3 = nMulti3*(nMulti3+1)/2
    sumNMulti5 = nMulti5*(nMulti5+1)/2
    
    #Agora basta somar os múltiplos de 3 e 5. NOTA: Múltiplos de 15 são múltiplos simultâneos de 3 e 5, pelo que é necessário subtrair o conjunto de múltiplos de 15 que ficariam a ser contabilizados duas vezes.
    
    nMulti15 = floor((max-1) / 15)
    sumNMulti15 = nMulti15*(nMulti15+1)/2

    return floor(3 * sumNMulti3 + 5 * sumNMulti5 - 15 *sumNMulti15)
    
if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(Multiplo3_5(int(sys.argv[1])))
    else:
        print("run python3 Multiplo3_5.py max")
    

'''
Recorri a informações na internet tais como:
    https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
    https://www.geeksforgeeks.org/sum-multiples-number-n/
    https://math.stackexchange.com/questions/9259/find-the-sum-of-all-the-multiples-of-3-or-5-below-1000
'''
