import sys

def MudaLetras(str):
    vowels = ['a','e','i','o','u']
    listStr = list(str)
    count = 0
    for character in listStr:
        # passo 1 - verifica se i é um caráter do alfabeto
        if character.isalpha():
            # se for 'Z' ou z é necessário "dar a volta" ao alfabeto
            if character == 'Z' or character == 'z':
                listStr[count] = chr(ord(character)-25)
            else:
                listStr[count] = chr(ord(character)+1)
            # passo 2 - verifica se o caráter é uma vogal minúscula
            if listStr[count] in vowels:
                listStr[count] = chr(ord(listStr[count])-32)
        count += 1
    res  = ''.join(listStr)
    return res

if __name__ == '__main__':
    if len(sys.argv) >1:
        listaArgs= list()
        for i in range (1,len(sys.argv)):
            listaArgs.append(sys.argv[i])
        res = " ".join(listaArgs)
        try:
            number = int(res)
            print(number)
        except ValueError:
            print(MudaLetras(" ".join(listaArgs)))
    else:
        print("run python3 MudaLetras.py str")
