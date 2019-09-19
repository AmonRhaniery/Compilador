# -*- coding: utf-8 -*-
import string

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
RIGHT_PARENTHESIS = 27
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
#fim do arquivo
EOF=49

#1a etapa: PALAVRAS RESERVADAS
PalavrasReservadas = ["array", "boolean", "break", "char", "continue", "do", "else", "false", "function", "if", "integer", "of", "string", "struct", "true", "type", "var", "while"]

TOKENS=[] #pilha de tokens do arquivo de entrada

Erro=False #indicador de erro do analisador léxico

nextChar="" #próx char do arquivo
arq = None #variavel responsável por ler o arquivo do código

def searchKeyWord(nome): 
    """Retorna token de PALAVRAS RESERVADAS ou ID"""
    esquerda=0
    direita=len(PalavrasReservadas) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if PalavrasReservadas[meio] == nome:
            return meio #precisa retornar a var?
        elif PalavrasReservadas[meio] > nome:
            direita = meio - 1
        else: # A[meio] < item
            esquerda = meio + 1
    return ID #retornar id?

#2a etapa: IDENTIFICADORES
Identificadores = {}
cont = 0
def searchName(nome): 
    """Adiciona os identificadores num formato Hash juntamente com token secundario.
    O token secundário é a ordem do identificador no texto, sendo considerado a primeira aparição apenas."""
    global cont
    global Identificadores
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

#AUTOMATO FINITO DO ANALISADOR LEXICO
def isspace(n):
    if n in [chr(10), chr(13)," ", "\t", "\v", "\f"]:
        return True
    return False
def isalnum(n):
    if n in string.ascii_letters:
        return True
    return False
def isdigit(n):
    if n in "0123456789":
        return True
    return False

linha = 1
ch=1
def nextToken():
    """Retorna o token lido e suas variáveis token principal e secundário"""
    global nextChar
    global ch
    global linha
    global arq
    separador=""
    while(isspace(nextChar)):
        if (nextChar == "\n") or (nextChar == "\r"):
            linha+=1
        nextChar=arq.read(1)
        ch+=1
    if (nextChar==""):
            token=EOF
    elif (isalnum(nextChar)):
        textAux=[]
        while(isalnum(nextChar) or nextChar == '_'):
            textAux.append(nextChar)
            nextChar=arq.read(1)
            ch+=1
        text=separador.join(textAux)
        token = searchKeyWord(text)
        if(token==ID):
            tokenSecundario=searchName(text)
    elif (isdigit(nextChar)):
        numeralAux=[]
        while(isdigit(nextChar)):
            numeralAux.append(nextChar)
            nextChar=arq.read(1)
            ch+=1
        numeral=separador.join(numeralAux)
        token = NUMERAL
        tokenSecundario = addConst(numeral)
    elif (nextChar=="\""):
        stringAux=[]
        stringAux.append(nextChar)
        nextChar=arq.read(1)
        ch+=1
        if(nextChar!="\""):
            while(nextChar!="\""):
                stringAux.append(nextChar)
                nextChar=arq.read(1)
                ch+=1
        stringAux.append(nextChar)
        nextChar=arq.read(1)
        ch+=1
        string=separador.join(stringAux)
        token = STRING
        tokenSecundario = addConst(string)
    else:
        if(nextChar=="\'"):
            nextChar=arq.read(1)
            ch+=1
            token=CHARACTER
            tokenSecundario=addConst(nextChar)
            nextChar=arq.read(2) 
            ch+=2
        elif(nextChar==":"):
            nextChar=arq.read(1)
            ch+=1
            token=COLON
        elif(nextChar=="+"):
            nextChar=arq.read(1)
            ch+=1
            if(nextChar=="+"):
                token=PLUS_PLUS
                nextChar=arq.read(1)
                ch+=1
            else:
                token=PLUS
        elif(nextChar=="-"):
            nextChar=arq.read(1)
            ch+=1
            if(nextChar=="-"):
                token=MINUS_MINUS
                nextChar=arq.read(1)
                ch+=1
            else:
                token=MINUS
        elif(nextChar==";"):
            nextChar=arq.read(1)
            ch+=1
            token=SEMI_COLON
        elif(nextChar==","):
            nextChar=arq.read(1)
            ch+=1
            token=COMMA
        elif(nextChar=="="):
            nextChar=arq.read(1)
            ch+=1
            if(nextChar=="="):
                token=EQUAL_EQUAL
                nextChar=arq.read(1)
                ch+=1
            else:
                token=EQUALS
        elif(nextChar=="["):
            nextChar=arq.read(1)
            ch+=1
            token=LEFT_SQUARE
        elif(nextChar=="]"):
            nextChar=arq.read(1)
            ch+=1
            token=RIGHT_SQUARE
        elif(nextChar=="{"):
            nextChar=arq.read(1)
            ch+=1
            token=LEFT_BRACES
        elif(nextChar=="}"):
            nextChar=arq.read(1)
            ch+=1
            token=RIGHT_BRACES
        elif(nextChar=="("):
            nextChar=arq.read(1)
            ch+=1
            token=LEFT_PARENTHESIS
        elif(nextChar==")"):
            nextChar=arq.read(1)
            ch+=1
            token=RIGHT_PARENTHESIS
        elif(nextChar=="&"):
            nextChar=arq.read(1)
            ch+=1
            if(nextChar=="&"):
                nextChar=arq.read(1)
                ch+=1
                token=AND
            else:
                token=UNKNOWN
        elif(nextChar=="|"):
            nextChar=arq.read(1)
            ch+=1
            if(nextChar=="|"):
                nextChar=arq.read(1)
                ch+=1
                token=OR
            else:
                token=UNKNOWN
        elif(nextChar=="<"):
            nextChar=arq.read(1)
            ch+=1
            if(nextChar)=="=":
                token=LESS_OR_EQUAL
                nextChar=arq.read(1)
                ch+=1
            else:
                token=LESS_THAN
        elif(nextChar==">"):
            nextChar=arq.read(1)
            ch+=1
            if(nextChar)=="=":
                token=GREATER_OR_EQUAL
                nextChar=arq.read(1)
                ch+=1
            else:
                token=GREATER_THAN
        elif(nextChar=="!"):
            nextChar=arq.read(1)
            ch+=1
            if(nextChar)=="=":
                token=NOT_EQUAL
                nextChar=arq.read(1)
                ch+=1
            else:
                token=NOT 
        elif(nextChar=="*"):
            nextChar=arq.read(1)
            ch+=1
            token=TIMES
        elif(nextChar=="."):
            nextChar=arq.read(1)
            ch+=1
            token=DOT        
        elif(nextChar=="/"):
            nextChar=arq.read(1)
            ch+=1
            token=DIVIDE
        else:
            nextChar=arq.read(1)
            ch+=1
            token=UNKNOWN
    return token

def analisarLexicamente(arquivo):
    """Executar o analisador Léxico."""
    global Erro
    global arq
    global nextChar
    arq=arquivo
    nextChar = arq.read(1)
    tokenAux=nextToken()
    while (tokenAux!=EOF):
        TOKENS.append(tokenAux)
        if(tokenAux==UNKNOWN):
            print("Caracter "+str(ch+1)+" não esperado na linha " + str(linha))
            Erro=True
        tokenAux=nextToken()
    if (not Erro):
        print ("Sem erros léxicos.")
            

