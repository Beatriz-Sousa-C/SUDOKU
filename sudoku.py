#Beatriz Sousa da Cruz, Isabella Lelis Moreno, Iuri Castro Bessa.

import sys

### Declaração de variáveis 

#começa declarando um sudoku vazio
sudoku = [
    list("    A   B   C    D   E   F    G   H   I"),
    list(" ++---+---+---++---+---+---++---+---+---++"),
    list("1||   |   |   ||   |   |   ||   |   |   ||1"),
    list(" ++---+---+---++---+---+---++---+---+---++"),
    list("2||   |   |   ||   |   |   ||   |   |   ||2"),
    list(" ++---+---+---++---+---+---++---+---+---++"),
    list("3||   |   |   ||   |   |   ||   |   |   ||3"),
    list(" ++===+===+===++===+===+===++===+===+===++"),
    list("4||   |   |   ||   |   |   ||   |   |   ||4"),
    list(" ++---+---+---++---+---+---++---+---+---++"),
    list("5||   |   |   ||   |   |   ||   |   |   ||5"),
    list(" ++---+---+---++---+---+---++---+---+---++"),
    list("6||   |   |   ||   |   |   ||   |   |   ||6"),
    list(" ++===+===+===++===+===+===++===+===+===++"),
    list("7||   |   |   ||   |   |   ||   |   |   ||7"),
    list(" ++---+---+---++---+---+---++---+---+---++"),
    list("8||   |   |   ||   |   |   ||   |   |   ||8"),
    list(" ++---+---+---++---+---+---++---+---+---++"),
    list("9||   |   |   ||   |   |   ||   |   |   ||9"),
    list(" ++---+---+---++---+---+---++---+---+---++"),
    list("    A   B   C    D   E   F    G   H   I")
]

#Dicionário com as colunas pra ser mais fácil de adicionar as entradas
coluna_matriz = {"A" : 4, "B" : 8, "C" : 12, "D" : 17, "E" : 21, "F" :25, "G" : 30, "H" : 34, "I": 38} 

#Dicionario com o espaco correspondente as linhas da entrada
linha_matriz = {"1": 2 ,"2" : 4, "3" : 6, "4" : 8, "5":10, "6": 12, "7": 14, "8": 16, "9" : 18} 


### Declaração de funções

#Fazendo uma funcao para pintar as entradas que forem dadas
def pintar(valor, cor="\033[31m"):
    return f"{cor}{valor}\033[0m"

# Função para imprimir a matriz de forma visual no terminal
def imprimir_matriz(sudoku):
    for linha in sudoku:
        # Junta os caracteres da linha e imprime
        print("".join(linha))  


### Principal

#Criando uma lista dos parametos de entrada
parametros = sys.argv
#Pegando a quantidade de arquivos de entrada, tirando o nome do programa
quantidade_arquivos = len(parametros) -1

#Verificando se o usuario entrou com um arquivo
if (quantidade_arquivos == 1):
    #Pegando o nome do arquivo das pistas
    pistas_arqv1= sys.argv[1]
    quantidade_pistas = 0
 
    #Lendo o arquivo
    with open (pistas_arqv1, 'r') as arquivo:
        for pistas in arquivo:
            pista = pistas.split(',')
            pista_linha_valor = pista[1].split(":")
            
            coluna = pista[0].strip()
            linha = pista_linha_valor[0].strip()
            valor = pista_linha_valor[1].strip()

            sudoku[linha_matriz[linha]][coluna_matriz[coluna.upper()]] = pintar(valor)
            quantidade_pistas += 1

    imprimir_matriz(sudoku)

    if (quantidade_pistas<1 or quantidade_pistas>80):
        print("Quantidade de pistas inválidas. Precisa haver uma quantidade de 1 até 80")
        sys.exit(1)
