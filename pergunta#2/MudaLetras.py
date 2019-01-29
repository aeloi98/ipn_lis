import sys

'''
A única melhoria que achei correto implementar é a junção do passo 1 ao passo 2 já que podem ser feitos um após outro no mesmo caráter.
'''
def MudaLetras(str):
    vogais = ['a','e','i','o','u']
    listStr = list(str)
    count = 0
    for i in listStr:
        # passo 1 - verifica se i é um caráter do alfabeto
        if i.isalpha():
            # se for 'Z' ou z é necessário "dar a volta" ao alfabeto
            if i == 'Z' or i == 'z':
                listStr[count] = chr(ord(i)-25)
            else:
                listStr[count] = chr(ord(i)+1)
            # passo 2 - verifica se o caráter é uma vogal minúscula
            if listStr[count] in vogais:
                listStr[count] = chr(ord(listStr[count])-32)
        count += 1
    res  = ''.join(listStr)
    return res

if __name__ == '__main__':
    if len(sys.argv) >1:
        listaArgs= list()
        for i in range (1,len(sys.argv)):
            listaArgs.append(sys.argv[i])
        print(MudaLetras(" ".join(listaArgs)))
    else:
        print("run python3 MudaLetras.py str")
