vetA = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Ç','À','Á','Ã','Â','É','Ê','Í','Ó','Õ','Ô','Ú',' ','ç','à','á','ã','â','a','b','c','d','e','é','ê','f','g','h','i','í','ì','j','k','l','m','n','o','ó','õ','ô','ò','p','q','r','s','t','u','ú','v','w','x','y','z','!','?','.','@','#','$','%','-',',']
vetC = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,132,134,136,138,140,142,144,146,148,150,152,154,156,158,160,162,164,166,168,170,172,174,176,178]
ind = []
cripto = []
decripto = []
opcao = 0

#funcoes
#criptografar em binario
def bin_to_str(palavra):
    binario = str(palavra)
    caractere = ''
    string = ''
    tamanho = len(palavra)
    k = 1
    for j in binario:
        if j != ' ':
            caractere += j
            if k == tamanho:
                string += chr(int(caractere, 2))
        else:
            string += chr(int(caractere, 2))
            caractere = ''  ## 0x101100110
        k += 1
    return string

#descriptografar de binario
def str_to_bin(string):
    binario = ''
    for i in string:
        binario += bin(ord(i))[2::] + ' '
    return binario

#apresentação
print('~'*40)
print('Lukas Gabriel Burda Ferreira Longo')
print('Matrícula 1918704')
print('~'*40)

#menu
while (opcao != 3):
    print('\nDentre as opções a seguir,\n'
            '  [ 1 ] Encriptar uma frase\n'
            '  [ 2 ] Desencriptar uma frase\n'
            '  [ 3 ] Sair do programa')
    opcao = int(input('Escolha uma opção: '))

    #para encriptar
    if (opcao == 1):
        print('~'*40)
        palavra = str(input('\nInsira uma frase para encriptar: '))
        indice = len(palavra)
        
        #para encriptar
        for pos in range(indice):
            ind.append(vetA.index(palavra[pos]))
            cripto.append(vetC[ind[pos]])
        print('~'*40)
        print('Sua frase é:',palavra)
        print('~'*40)
        print('As letras criptografadas são: ',cripto) #posição no vetor cripto das palavras
        print('~'*40)

        #chamando a função binária
        resp = str(input('\nDeseja transformar a frase em binário? <s/n> '))
        if (resp == 's'):
            binary = str_to_bin(palavra)
            print('~'*40)
            print('O código binário da sua frase é: ',binary)
            print('<Zeros à esquerda são desconsierados>')
            print('~'*40)
            print('\nRetornando ao menu...')
        else:
            print('~'*40)
            print('\nRetornando ao menu...')
            
    #chamando a função de desencriptar
    elif (opcao == 2):
        binary = str(input('\nInsira uma sequência binária para desencriptar: '))
        text = bin_to_str(binary)
        indice = len(text)
        print('~'*40)        
        #chamando pergunta para binário > cripto
        resp = str(input('Deseja transformar o código binário em cripto? <s/n> '))
        if (resp == 's'):
            for pos in range(indice):
                ind.append(vetA.index(text[pos]))
                decripto.append(vetC[ind[pos]])
                
            print('As letras em cripto são: ',decripto)
            print('~'*40)
            print('\nSua frase desencriptada é: ',text)
            print('\nRetornando ao menu...')
        if (resp == 'n'):
            print('~'*40)
            print('\nRetornando ao menu...')
            
    elif (opcao == 3):
        print('\nFinalizando...')
        print('~'*40)
        
    else:
        print('Opção inválida, tente novamente.')
        print('~'*40)
        print('\nRetornando ao menu...')

print('###########  Volte sempre que precisar.  ###########')
input()
