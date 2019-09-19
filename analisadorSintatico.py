# -*- coding: utf-8 -*-
import analisadorLexico as lxc
import csv

#Estados
P = 50
LDE = 51
DE = 52
DF = 53
DT = 54
T = 55
DC = 56
LI = 57
LP = 58
B = 59
LDV = 60
LS = 61
DV = 62
S = 63
E = 64
LV = 65
L = 66
R = 67
Y = 68
F = 69
LE = 70
ID = 71
TRUE = 72
FALSE = 73
CHR = 74
STR = 75
NUM = 76
PLINHA = 77
M = 78
U = 79

#Regras armazenadas na forma Left -> Right
RIGHT = [1,2,1,1,1,1,1,1,1,1,9,7,4,5,3,8,5,3,4,2,1,2,1,5,3,1,1,1,5,7,7,5,7,1,4,2,2,3,3,1,3,3,3,3,3,3,1,3,3,1,3,3,1,1,2,2,2,2,3,4,2,2,1,1,1,1,1,3,1,3,4,1,1,1,1,1,1,1]
LEFT = [P,LDE,LDE,DE,DE,T,T,T,T,T,DT,DT,DT,DC,DC,DF,LP,LP,B,LDV,LDV,LS,LS,DV,LI,LI,S,S,U,U,M,M,M,M,M,M,M,E,E,E,L,L,L,L,L,L,L,R,R,R,Y,Y,Y,F,F,F,F,F,F,F,F,F,F,F,F,F,F,LE,LE,LV,LV,LV,ID,TRUE,FALSE,CHR,STR,NUM]

TAB_ACTION_GOTO = list(csv.reader(open("TabelaActionGoTo.csv","r"),delimiter="\t"))

#ordem dos tokens na tabela
TOKEN_TAB_ACTION=[lxc.INTEGER,lxc.CHAR,lxc.BOOLEAN,lxc.STRING,lxc.TYPE,lxc.EQUALS,lxc.ARRAY,lxc.LEFT_SQUARE,lxc.RIGHT_SQUARE,lxc.OF,lxc.STRUCT,lxc.LEFT_BRACES,lxc.RIGHT_BRACES,lxc.SEMI_COLON,lxc.COLON,lxc.FUNCTION,lxc.LEFT_PARENTHESIS,lxc.RIGHT_PARENTHESIS,lxc.COMMA,lxc.VAR,lxc.IF,lxc.ELSE,lxc.WHILE,lxc.DO,lxc.BREAK,lxc.CONTINUE,lxc.AND,lxc.OR,lxc.LESS_THAN,lxc.GREATER_THAN,lxc.LESS_OR_EQUAL,lxc.GREATER_OR_EQUAL,lxc.EQUAL_EQUAL,lxc.NOT_EQUAL,lxc.PLUS,lxc.MINUS,lxc.TIMES,lxc.DIVIDE,lxc.PLUS_PLUS,lxc.MINUS_MINUS,lxc.NOT,lxc.DOT,lxc.ID,lxc.TRUE,lxc.FALSE,lxc.CHARACTER,lxc.STRINGVAL,lxc.NUMERAL,lxc.EOF,PLINHA,P,LDE,DE,T,DT,DC,DF,LP,B,LDV,LS,DV,LI,S,U,M,E,L,R,Y,F,LE,LV,ID,TRUE,FALSE,CHR,STR,NUM]

#contador token do código
proximo=-1

def tokenTAB(a):
    """Retorna a coluna na tabela ACTION"""
    return TOKEN_TAB_ACTION.index(a)+1

def nextToken():
    """Retorna token da pilha TOKENS do analisador léxico"""
    global proximo
    proximo+=1
    try:
        return lxc.TOKENS[proximo]
    except:
        return lxc.EOF


Erro = False
def parse():
    """Analisador Sintático"""
    global Erro
    PILHA = [] #armazena os estados
    state = 0 #linha da tabela ACTION
    PILHA.append(state)
    tokenLido = nextToken()
    action = TAB_ACTION_GOTO[state+1][tokenTAB(tokenLido)]
    
    cont=0
    while (action!="acc"):
        #print("TESTE DO TOKENLIDO no passo "+str(cont))
        #print(tokenLido)
        #print("TESTE DA TABELA")
        #print(action)
        #print("TESTE DA PILHA")
        #print(PILHA)
        if (action[0]=="s"):
            """shift to state"""
            state=int(action[1:])
            PILHA.append(state)
            tokenLido=nextToken()
            action = TAB_ACTION_GOTO[state+1][tokenTAB(tokenLido)]
            cont+=1
        elif (action[0]=="r"):
            """reduce rule"""
            rule=int(action[1:])
            for x in range(RIGHT[rule-1]):
                PILHA.pop()
            try:
                state=int(TAB_ACTION_GOTO[PILHA[-1]+1][tokenTAB(LEFT[rule-1])])
            except:
                print("Erro de sintaxe.")
                Erro = True
                break
            PILHA.append(state)
            action=TAB_ACTION_GOTO[state+1][tokenTAB(tokenLido)]
            cont+=1
        else:
            """erro de sintaxe"""
            Erro = True
            print("Erro de sintaxe no token "+str(proximo))
            break
    if (not Erro):
        print("Sem erro de sintaxe.")

def analisarSintaticamente():
    if (not lxc.Erro):
        parse()

            

