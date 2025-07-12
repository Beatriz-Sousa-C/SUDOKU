# Beatriz Sousa da Cruz, Isabella Lelis Moreno, Iuri Castro Bessa.

import sys

### Declaração de variáveis 

# Começa declarando um sudoku vazio
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

# Dicionário com o espaco correspondente as colunas do sudoku para transpor da matriz 9x9
coluna_sudoku = {0 : 4, 1 : 8, 2 : 12, 3 : 17, 4 : 21, 5 : 25, 6 : 30, 7 : 34, 8 : 38} 

# Dicionário com o espaco correspondente as linhas do sudoku para transpor da matriz 9x9
linha_sudoku = {0 : 2, 1 : 4, 2 : 6, 3 : 8, 4 : 10, 5 : 12, 6 : 14, 7 : 16, 8 : 18} 

# Matriz 9x9
matriz = [[' ' for j in range(9)]for i in range(9)]

# Dicionário com as colunas da matriz
coluna_matriz = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7, "I" : 8}

# Dicionário com as linhas da matriz
linha_matriz = {"1" : 0 , "2" : 1, "3" : 2, "4" : 3, "5" : 4, "6" : 5, "7" : 6, "8" : 7, "9" : 8} 


### Declaração de funções

# Função para pintar as pistas que forem dadas
def pintar(valor, cor="\033[31m"):
    return f"{cor}{valor}\033[0m"

# Função para imprimir a matriz de forma visual no terminal
def imprimir_matriz(sudoku):
    for linha in sudoku:
        # Junta os caracteres da linha e imprime
        print("".join(linha))  


# Função para ler arquivo pistas
def ler_arquivo_pistas(pistas_arqv): 
    todas_pistas = []

    # Lendo o arquivo
    with open (pistas_arqv, 'r') as arquivo:
        # Pecorrendo as linhas do arquivo
        for pistas in arquivo:
            # Separando as colunas do resto da pista
            pista = pistas.split(',')
            # Separando a linha e o valor da pista
            pista_linha_valor = pista[1].split(":")
            
            # Pegando a coluna, linha e valor da pista
            coluna = pista[0].strip().upper()
            linha = pista_linha_valor[0].strip()
            valor = pista_linha_valor[1].strip()

            matriz[linha_matriz[linha]][coluna_matriz[coluna]] = int(valor)
            todas_pistas.append((linha, coluna, valor))
           
    return todas_pistas

# Função para ler arquivo jogadas
def ler_arquivo_jogadas(jogadas_arqv): 
    todas_jogadas = []

    # Lendo o arquivo
    with open (jogadas_arqv, 'r') as arquivo:
        # Pecorrendo as linhas do arquivo
        for jogadas in arquivo:
            # Separando as colunas do resto da jogada
            jogada = jogadas.split(',')
            # Separando a linha e o valor da jogada
            jogada_linha_valor = jogada[1].split(":")
            
            # Pegando a coluna, linha e valor da jogada
            coluna = jogada[0].strip().upper()
            linha = jogada_linha_valor[0].strip()
            valor = jogada_linha_valor[1].strip()

            # Verifica se o formato da jogada é válido
            if coluna not in coluna_matriz or linha not in linha_matriz or int(valor) not in range(1, 10):
                print(f"A jogada ({coluna},{linha}) = {valor} é inválida!")
            else:
                todas_jogadas.append((linha, coluna, valor))
           
    return todas_jogadas

# Função que verifica se os quadrantes da matriz está preenchida corretamente
def validar_quadrante(matriz):
    for bloco_linha in range(0, 9, 3):
        for bloco_coluna in range(0, 9, 3):
            numeros = set()
            for i in range(3):
                for j in range(3):
                    valor = matriz[bloco_linha + i][bloco_coluna + j]
                    if valor != ' ':
                        if valor in numeros:
                            # Valor repetido no quadrante
                            return False  
                        numeros.add(valor)
    # Todos os quadrantes estão válidos
    return True

# Verifica se as linhas da matriz estão preenchidas corretamente
def validar_linhas(matriz):
    for linha in matriz:
        numeros = set()
        for valor in linha:
            if valor != ' ':
                if valor in numeros:
                    # Valor repetido nas linhas
                    return False
                numeros.add(valor)
    # Todas as linhas estão válidas
    return True

# Verifica se as colunas da matriz estão preenchidas corretamente
def validar_colunas(matriz):
    for col in range(9):
        numeros = set()
        for linha in range(9):
            valor = matriz[linha][col]
            if valor != ' ':
                if valor in numeros:
                    # Valor repetido nas colunas
                    return False
                numeros.add(valor)
    # Todas as colunas estão válidas
    return True

# Função para validar as pistas
def validar_pistas(matriz, todas_pistas, modo_batch=False):
    
    # Verifica se há repetição de pistas
    # Dicionário para armazenar as células ocupadas
    celulas_ocupadas = {}
    quantidade_pistas = 0
    # Percorrendo todas as pistas
    for linha, coluna, valor in todas_pistas:
        celula = (linha, coluna)
        if celula not in celulas_ocupadas:
            celulas_ocupadas[celula] = int(valor)
            quantidade_pistas += 1
        # Verifica se há sobreposição de pistas e é modo batch
        elif (celulas_ocupadas[celula] != int(valor)) and modo_batch:
            raise Exception("Configuração de dicas inválida!")
        
    # Garante que o número de pistas está dentro do intervalo permitido (1 a 80)
    if quantidade_pistas < 1 or quantidade_pistas > 80:
        raise Exception("Quantidade de pistas inválidas. Precisa haver uma quantidade de 1 até 80.")
    
    # Verificando se os quadrantes estão preenchidos corretamente
    if not validar_quadrante(matriz):
        if modo_batch:
            raise Exception("Configuração de dicas inválida!")
        else:
            raise Exception("Quadrantes inválidos. Há um valor repetido em algum quadrante.")
        
    # Verificando se as linhas estão preenchidas corretamente
    if not validar_linhas(matriz):  
        if modo_batch:
            raise Exception("Configuração de dicas inválida!")
        else:
            raise Exception("Linhas inválidas. Há um valor repetido em alguma linha.")
        
    # Verificando se as colunas estão preenchidas corretamente
    if not validar_colunas(matriz):
        if modo_batch:
            raise Exception("Configuração de dicas inválida!")
        else:
            raise Exception("Colunas inválidas. Há um valor repetido em alguma coluna.")

# Função para validar jogadas em modo batch
def validar_jogada_batch(matriz):
    
    # Verificando se os quadrantes estão preenchidos corretamente
    if not validar_quadrante(matriz):
        return False
        
    # Verificando se as linhas estão preenchidas corretamente
    if not validar_linhas(matriz):  
        return False
        
    # Verificando se as colunas estão preenchidas corretamente
    if not validar_colunas(matriz):
        return False

    return True      

# Função para transpor a matriz de pistas para o sudoku
def matriz_para_sudoku():
    for i in range(9):
        for j in range(9):
            sudoku[linha_sudoku[i]][coluna_sudoku[j]] = matriz[i][j]

# Função para pintar o sudoku com as pistas
def pintar_sudoku():
    for i in range(9):
        for j in range(9):
            if matriz[i][j] != ' ':
                # Pintando as pistas de vermelho
                sudoku[linha_sudoku[i]][coluna_sudoku[j]] = pintar(matriz[i][j])
            else:
                # Mantendo o espaço vazio
                sudoku[linha_sudoku[i]][coluna_sudoku[j]] = ' '

# Função para inicializar o jogo
def inicializar_jogo(pistas_arqv, modo_batch=False):
    todas_pistas = ler_arquivo_pistas(pistas_arqv)
    # Verificando se o modo não é batch
    if not modo_batch: 
        matriz_para_sudoku()
        pintar_sudoku()
        imprimir_matriz(sudoku)
    # Validando as pistas
    validar_pistas(matriz, todas_pistas, modo_batch)
    return todas_pistas

# Função para modo interativo
def modo_interativo(pistas_arqv):
    try:
        inicializar_jogo(pistas_arqv)
    except Exception as e:
        print(e)

# Função para modo solucionador
def modo_solucionador(pistas_arqv):
    try:
        inicializar_jogo(pistas_arqv)
    except Exception as e:
        print(e)

# Função para modo batch
def modo_batch(pistas_arqv, jogadas_arqv):
    try:
        todas_pistas = inicializar_jogo(pistas_arqv, modo_batch=True)
        todas_jogadas = ler_arquivo_jogadas(jogadas_arqv)

        pistas_set = set()
        for linha, coluna, _ in todas_pistas:
            pistas_set.add((linha, coluna))

        for linha, coluna, valor in todas_jogadas:
            # Verifica se a jogada é uma pista
            if (linha, coluna) in pistas_set:
                print(f"A jogada ({coluna},{linha}) = {valor} é inválida!")
            else:
                matriz[linha_matriz[linha]][coluna_matriz[coluna]] = int(valor)
                if not validar_jogada_batch(matriz):
                    print(f"A jogada ({coluna},{linha}) = {valor} é inválida!")
                    matriz[linha_matriz[linha]][coluna_matriz[coluna]] = ' '
        
        celulas_preenchidas = 0
        for i in range(9):
            for j in range(9):
                if matriz[i][j] != ' ':
                    celulas_preenchidas += 1

        if celulas_preenchidas == 81:
            print("A grade foi preenchida com sucesso!")
        else:
            print("A grade não foi preenchida!")

    except Exception as e:
        print(e)

### Principal

def principal():
    # Criando uma lista dos parametos de entrada
    parametros = sys.argv
    # Pegando a quantidade de arquivos de entrada, tirando o nome do programa
    quantidade_arquivos = len(parametros) -1

    # Verificando se o usuario entrou com um arquivo
    if (quantidade_arquivos == 1):
        # Pegando o nome do arquivo das pistas
        pistas_arqv= sys.argv[1]

        # Verificando o modo de jogo
        modo = input("Digite 'i' para o modo Interativo ou 's' para o modo Solucionador: ").strip().lower()
        if modo == 'i':
            modo_interativo(pistas_arqv)
        elif modo == 's':
            modo_solucionador(pistas_arqv)
        else:
            print("Modo inválido!")

    # Verificando se o usuario entrou com dois arquivos
    elif (quantidade_arquivos == 2):
        pistas_arqv= sys.argv[1]
        jogadas_arqv = sys.argv[2]
        modo_batch(pistas_arqv, jogadas_arqv)

# Execução do programa
if __name__ == "__main__":
    principal()