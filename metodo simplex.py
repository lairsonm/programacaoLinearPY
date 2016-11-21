#programa para a matéria matemática aplicada
#feito por Lairson Melo Filho

def funcaoDeCalculo():
    indexMaximo = 1
    indexDivisor = 0
    maximo = 0
    while indexMaximo < tamanhoDaMatriz:
        if matriz[0][indexMaximo] < maximo:
            maximo = matriz[0][indexMaximo]
            indexDivisor = indexMaximo
        indexMaximo += 1
    print('A coluna pivot é:', indexDivisor)
    print('O valor utilizado é:', maximo)


    iterationDivisor = 0
    menorPositivo = 0
    teste =0
    linhaMenorPositivo = 0
    while iterationDivisor < numeroRestricoes:
        iterationDivisor += 1
        teste = matriz[iterationDivisor][tamanhoDaMatriz]/matriz[iterationDivisor][indexDivisor]
        if (teste>0):
            if menorPositivo == 0:
                menorPositivo = teste
                linhaMenorPositivo = iterationDivisor
            elif teste < menorPositivo:
                menorPositivo = teste
                linhaMenorPositivo = iterationDivisor

    print('O menor positivo é', menorPositivo)
    print('A linha do menor positivo é', linhaMenorPositivo)

    matriz[linhaMenorPositivo] = [x/matriz[linhaMenorPositivo][indexDivisor] for x in matriz[linhaMenorPositivo]]
    print('A linha para fazer a conta é', matriz[linhaMenorPositivo])

    iterationMultiplicador = 0
    while iterationMultiplicador <= numeroRestricoes:
        if iterationMultiplicador != linhaMenorPositivo:
            linhaMultiplicada = [y*(-matriz[iterationMultiplicador][indexDivisor]) for y in matriz[linhaMenorPositivo]]
            print('Linha multiplicada', linhaMultiplicada)
            matriz[iterationMultiplicador] = [a + b for a, b in zip(matriz[iterationMultiplicador], linhaMultiplicada)]
            print('Linha substituida', matriz[iterationMultiplicador])
            iterationMultiplicador += 1
        else:
            matriz[iterationMultiplicador] = matriz[iterationMultiplicador]
            iterationMultiplicador += 1
    print('A matriz atual é:', matriz)
    return matriz


def MostrarVariaveisBasicasENaoBasicas(matriz):
    iterationColuna = 1
    while iterationColuna <= (numeroRestricoes*2):
        coluna = [row[iterationColuna] for row in matriz]
        soma = sum(coluna)
        if soma == 1:
            print('O valor ótimo para a variável de número ', iterationColuna, 'é:', matriz[iterationColuna][tamanhoDaMatriz])
        else:
            print('A variável de número', iterationColuna, 'é não básica, logo igual a: 0')
        iterationColuna += 1

         #   matriz[iterationLinha][iterationColuna]


def MostrarValorDeZ(matriz):
    print('O valor de Z é:', matriz[0][tamanhoDaMatriz])


#ITERAÇÃO DE CHECAGEM
def ChecarSeOtima(matriz):
    otima = 0
    for a in matriz[0]:
        if a >= 0:
            otima += 0
        else:
            otima += 1
            print('A solução não é ótima por causa do número:', a,'\n')
    if otima > 0:
        funcaoDeCalculo()
        ChecarSeOtima(matriz)
    else:
        print('Foi encontrada a solução ótima \n')
        MostrarVariaveisBasicasENaoBasicas(matriz)
        MostrarValorDeZ(matriz)






#CORPO DO PROGRAMA
print ('Bem vindo ao programa de método Simplex')
numeroVariaveis = int(input('Quantas são as variáveis de decisão?'))
#print (numeroVariaveis)
numeroRestricoes = int(input('Quantas são as restrições?'))
#print (numeroRestricoes)
matrizPrimeira = [[1.0]]
iterationVariaveis = 0
iterationRestricoes = 0
matriz = [[1]]
novaLinha = [0]
tamanhoDaMatriz = 0
print('Agora você vai inserir os coeficientes da função objetivo')

#inserção dos coeficientes da função objetivo
while iterationVariaveis < numeroVariaveis:
    iterationVariaveis += 1
    item = float(input('Insira o coeficiente'))
    matriz[0].insert(iterationVariaveis, item)
    tamanhoDaMatriz += 1
    print(matriz)
iterationVariaveis = 0

#inserção dos coeficientes do que falta e o b
while iterationRestricoes <= numeroRestricoes:
    iterationRestricoes += 1
    matriz[0].insert(numeroVariaveis+1, 0)
    tamanhoDaMatriz += 1
    print(matriz)
iterationRestricoes = 0

#inserção dos coeficientes das restrições e dos resultados
while iterationRestricoes < numeroRestricoes:
    iterationRestricoes += 1
    while iterationVariaveis < numeroVariaveis:
        iterationVariaveis += 1
        item = float(input('Insira o coeficiente'))
        novaLinha.append(item)
        print(novaLinha)
    indexDaFalta = iterationVariaveis + iterationRestricoes

    while iterationVariaveis < tamanhoDaMatriz-1:
        iterationVariaveis += 1
        if iterationVariaveis == indexDaFalta:
            novaLinha.insert(iterationVariaveis, 1)
        else:
            novaLinha.insert(iterationVariaveis, 0)

    item = float(input('Insira o resultado'))
    novaLinha.append(item)

    matriz.append(novaLinha)
    novaLinha = [0]
    print('A matriz construida é:', matriz)
    iterationVariaveis = 0
iterationRestricoes = 0
funcaoDeCalculo()
ChecarSeOtima(matriz)
input()










