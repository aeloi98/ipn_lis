import sys
from math import floor



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
        try:
            number = int(sys.argv[1])
            if number >= 0:
                print(Multiplo3_5(number))
            else:
                raise ValueError

        except ValueError:
            print("Max should be a Natural Number")
    else:
        print("run python3 Multiplo3_5.py max")
    
