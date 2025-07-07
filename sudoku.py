#Beatriz Sousa da Cruz, Isabella Lelis Moreno, Iuri Castro Bessa.

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

#Lembrar de colocar aqui a variavel que na entrada corresponde a coluna
j = "D" 
#Lembrar de colocar aqui a variavel que na entrada corresponde a linha
i = "7"
#numero que vai ser adicionado no sudoku 
k = 5 

#Dicionário com as colunas pra ser mais fácil de adicionar as entradas
Coluna = {"A" : 4, "B" : 8, "C" : 12, "D" : 17, "E" : 21, "F" :25, "G" : 30, "H" : 34, "I": 38} 

#Dicionario com o espaco correspondente as linhas da entrada
Linha = {"1": 2 ,"2" : 4, "3" : 6, "4" : 8, "5":10, "6": 12, "7": 14, "8": 16, "9" : 18} 

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

sudoku[Linha[i]][Coluna[j]]= pintar(k)

imprimir_matriz(sudoku)

