#palavras reservadas
ARRAY = 0
BOOLEAN = 1
BREAK = 2
CHAR = 3
CONTINUE = 4
DO = 5
ELSE = 6
FALSE = 7
FUNCTION = 8
IF = 9
INTEGER = 10
OF = 11
STRING = 12
STRUCT = 13 
TRUE = 14
TYPE = 15
VAR = 16
WHILE = 17
#simbolos
COLON = 18
SEMI_COLON = 19
COMMA = 20
EQUALS = 21
LEFT_SQUARE = 22
RIGHT_SQUARE = 23
LEFT_BRACES = 24
RIGHT_BRACES = 25
LEFT_PARENTHESIS = 26
RIGHT_PARENTHESIS = 2
AND = 28
OR = 29
LESS_THAN = 30
GREATER_THAN = 31
LESS_OR_EQUAL = 32
GREATER_OR_EQUAL = 33
NOT_EQUAL = 34
EQUAL_EQUAL = 35
PLUS = 36
PLUS_PLUS = 37
MINUS = 38
MINUS_MINUS = 39
TIMES = 40
DIVIDE = 41
DOT = 42
NOT = 43
#tokens regulares
CHARACTER = 44
NUMERAL = 45
STRINGVAL = 46
ID = 47
#token desconhecido
UNKNOWN = 48

#1a etapa: PALAVRAS RESERVADAS
PalavrasReservadas = [ARRAY, BOOLEAN, BREAK, CHAR, CONTINUE, DO, ELSE, FALSE, FUNCTION, IF, INTEGER, OF, STRING, STRUCT, TRUE, TYPE, VAR, WHILE]

def searchKeyWord(nome): 
    """Retorna token de PALAVRAS RESERVADAS ou ID"""
    esquerda=0
    direita=len(palavrasReservadas) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if palavrasReservadas[meio] == nome:
            return meio #precisa retornar a var?
        elif palavrasReservadas[meio] > nome:
            direita = meio - 1
        else: # A[meio] < item
            esquerda = meio + 1
    return ID #retornar id?

#2a etapa: IDENTIFICADORES
Identificadores = {}
cont = 0
def searchName(nome): 
    """Adiciona os identificadores num formato Hash juntamente com token secundário.
    O token secundário é a ordem do identificador no texto, sendo considerado a primeira aparição apenas."""
    global cont
    if nome not in Identificadores.keys():
        Identificadores[nome] = cont
        cont = cont + 1

#3a etapa: LITERAIS
vConsts = []
def addConst(s):
    """Adiciona os literais do programa, que representam as constantes da linguagem. Estão associados aos tokens CHARACTER, NUMERAL E STRINGVAL.
    O token secundário é a ordem que foram adicionadas."""
    vConsts.append(s)
    return len(vConsts)-1
def getConst(n):
    """Retorna a constante de token secundário n."""
    return vConsts[n]

#LER CARACTER

arq = open('codigo.txt', 'r')
nextChar=arq.read(1)

#AUTOMATO FINITO DO ANALISADOR LEXICO
def ispace(n):
    if n in [chr(10), chr(13)," ", "\t", "\v", "\f"]:
        return True
    return False
def isalpha(n):
    if n in string.ascii_letters:
        return True
    return False
def isdigit(n):
    if n in [0,1,2,3,4,5,6,7,8,9]:
        return True
    return False

def nextToken():
    while(isspace(nextChar)):
        nextChar=arq.read(1)
    if (isalpha(nextChar)):
        textAux=[]
        while(isalnum(nextChar) or nextChar == '_'):
            textAux.append(nextChar)
            nextChar=arq.read(1)
        separador=""
        text=separador.join(textAux)
        token = searchKeyWord(text)
        if(token==ID):
            tokenSecundario=searchName(text)
    elif (isdigit(nextChar)):
        numeralAux=[]
        while(isdigit(nextChar)):
            numeralAux.append(nextChar)
            nextChar=arq.read(1)
        numeral=separador.join(numeralAux)
        token = NUMERAL
        tokenSecundario = addIntConst(numeral)
    elif (nextChar=="\""):
        stringAux=[]
        while(nextChar!="\""):
            stringAux.append(nextChar)
            nextChar=arq.read(1)
        string=separador.join(stringAux)
        token = STRING
        tokenSecundario = addStringConst(string)
    else:
        if(ch=="\""):
            nextChar=arq.read(1)
            token=CHARACTER
            tokenSecundario=addCharConst(nextChar)
            nextChar=arq.read(2) #pular o "
        elif(ch==":"):
            nextChar=arq.read(1)
            token=COLON
        elif(ch=="+"):
            nextChar=arq.read(1)
            if(nextChar=="+"):
                token=PLUS_PLUS
                nextChar=arq.read(1)
            else:
                token=PLUS
        elif():#FAZER O RESTANTE

        else:
            UNKNOWN
    return token
        
        
arq.close()

