# -*- coding: utf-8 -*-
import analisadorLexico as lxc
import analisadorSintatico as stt

arq = open("codigoGerado.txt","w")

NO_KIND_DEF_=-1
VAR_=0
PARAM_=1
FUNCTION_=2
FIELD_=3
ARRAY_TYPE_=4
STRUCT_TYPE_=5
ALIAS_TYPE_=6
SCALAR_TYPE_=7
UNIVERSAL_=8

def IS_TYPE_KIND(eKind):
    return (eKind==ARRAY_TYPE_ or eKind==STRUCT_TYPE_ or eKind==ALIAS_TYPE_ or eKind==SCALAR_TYPE_)

ERR_REDCL=9
ERR_NO_DECL=10
ERR_TYPE_EXPECTED=11
ERR_BOOL_TYPE_EXPECTED=12
ERR_TYPE_MISMATCH=13
ERR_INVALID_TYPE=14
ERR_KIND_NOT_STRUCT=15
ERR_FIELD_NOT_DECL=16
ERR_KIND_NOT_ARRAY=17
ERR_INVALID_INDEX_TYPE=18
ERR_KIND_NOT_VAR=19
ERR_KIND_NOT_FUNCTION=20
ERR_TOO_MANY_ARG=21
ERR_PARAM_TYPE=22
ERR_TOO_FEW_ARGS=23
ERR_RETURN_TYPE_MISMATCH=24

#Regras
PLINE_P_RULE = 0
P_LDE_RULE = 1
LDE_LDE_RULE = 2
LDE_DE_RULE = 3
DE_DF_RULE = 4
DE_DT_RULE = 5
T_INTEGER_RULE = 6
T_CHAR_RULE  = 7
T_BOOL_RULE = 8
T_STRING_RULE = 9
T_IDU_RULE = 10
DT_ARRAY_RULE = 11
DT_STRUCT_RULE = 12
DT_ALIAS_RULE = 12
DC_DC_RULE = 14
DC_LI_RULE = 15
DF_RULE = 16
LP_LP_RULE = 17
LP_IDD_RULE = 18
#LP_EPSILON_RULE = 
B_LS_RULE = 19
LDV_LDV_RULE = 20
LDV_DV_RULE = 21
LS_LS_RULE = 22
LS_S_RULE = 23
DV_VAR_RULE = 24
LI_COMMA_RULE = 25
LI_IDD_RULE = 26
S_M_RULE = 27
S_U_RULE = 28
#S_RETURN_RULE = 
U_IF_RULE = 29
U_IF_ELSE_U_RULE = 30
M_IF_ELSE_M_RULE = 31
M_WHILE_RULE = 32
M_DO_WHILE_RULE = 33
M_BLOCK_RULE = 34
M_E_SEMICOLON = 35
M_BREAK_RULE = 36
M_CONTINUE_RULE = 37
E_AND_RULE = 38
E_OR_RULE = 39
E_L_RULE = 40
#E_LV_EQUAL_RULE = 
L_LESS_THAN_RULE = 41
L_GREATER_THAN_RULE = 42
L_LESS_EQUAL_RULE = 43
L_GREATER_EQUAL_RULE = 44
L_EQUAL_EQUAL_RULE = 45
L_NOT_EQUAL_RULE = 46
L_R_RULE = 47
R_PLUS_RULE = 48
R_MINUS_RULE = 49
R_Y_RULE = 50
Y_TIMES_RULE = 51
Y_DIVIDE_RULE = 52
Y_F_RULE = 53
F_LV_RULE = 54
F_LEFT_PLUS_PLUS_RULE = 55
F_LEFT_MINUS_MINUS_RULE = 56
F_RIGHT_PLUS_PLUS_RULE = 57
F_RIGHT_MINUS_MINUS_RULE = 58
F_PARENTHESIS_E_RULE = 59
F_IDU_MC_RULE = 60
F_MINUS_F_RULE = 61
F_NOT_F_RULE = 62
F_TRUE_RULE = 63
F_FALSE_RULE = 64
F_CHR_RULE = 65
F_STR_RULE = 66
F_NUM_RULE = 67
LE_LE_RULE = 68
LE_E_RULE = 69
#LE_EPSILON_RULE = 
LV_DOT_RULE = 70
LV_SQUARE_RULE = 71
LV_IDU_RULE = 72
IDD_RULE = 73
IDU_RULE = 74
ID_RULE = 75
TRUE_RULE = 76
FALSE_RULE = 77
CHR_RULE = 78
STR_RULE = 79
NUM_RULE = 80
NB_RULE = 81
MF_RULE = 82
MC_RULE = 83
NF_RULE = 84
MT_RULE = 85
ME_RULE = 86
MW_RULE = 87
#MA_RULE = 

class Var:
    def __init__(self,tipo=None,nIndex=None, nSize=None):
        self.tipo=tipo
        self.nIndex=nIndex
        self.nSize=nSize
class Param:
    def __init__(self,tipo=None,nIndex=None, nSize=None):
        self.tipo=tipo
        self.nIndex=nIndex
        self.nSize=nSize
class Field:
    def __init__(self,tipo=None,nIndex=None, nSize=None):
        self.tipo=tipo
        self.nIndex=nIndex
        self.nSize=nSize
class Function:
    def __init__(self,pRetType=None,pParams=None, nIndex=None, nParams=None,nVars=None):
        self.pRetType=pRetType
        self.pParams=nParams
        self.nIndex=nIndex
        self.nParams=nParams
        self.nVars=nVars       
class Array:
    def __init__(self,tipoElemento=None,nNumElems=None, nSize=None):
        self.tipoElemento=tipoElemento
        self.nNumElems=nNumElems
        self.nSize=nSize
class Struct:
    def __init__(self,campos=None, nSize=None):
        self.campos=campos
        self.nSize=nSize
class Alias:
    def __init__(self,tipoBase=None, nSize=None):
        self.tipoBase=tipoBase
        self.nSize=nSize
class Type:
    def __init__(self,tipoBase=None, nSize=None):
        self.tipoBase=tipoBase
        self.nSize=None

class object:

    def __init__(self, nName=None, pNext=None,eKind=None,_=None):
        self.nName=nName
        self.pNext=pNext
        self.eKind=eKind
        self._=None

class ID:
    def __init__(self, objeto=None,name=None):
        self.objeto=objeto
        self.name=name
class T:
    def __init__(self, type=None):
        self.type=type
class E:
    def __init__(self, type=None):
        self.type=type
class L:
    def __init__(self, type=None):
        self.type=type
class R:
    def __init__(self, type=None):
        self.type=type
class Y:
    def __init__(self, type=None):
        self.type=type
class F:
    def __init__(self, type=None):
        self.type=type
class LV:
    def __init__(self, type=None):
        self.type=type
class MC:
    def __init__(self,type=None,param=None,err=None):
        self.type=type
        self.param=param
        self.err=err
class MT:
    def __init__(self,label=None):
        self.label=label   
class ME:
    def __init__(self,label=None):
        self.label=label  
class MW:
    def __init__(self,label=None):
        self.label=label  
class MA:
    def __init__(self,label=None):
        self.label=label  
class LE:
    def __init__(self, type=None,param=None,err=None,n=None):
        self.type=type
        self.param=param
        self.err=err
        self.n=n
class LI:
    def __init__(self, list=None):
        self.list=list
class DC:
    def __init__(self, list=None):
        self.list=list
class LP:
    def __init__(self, list=None):
        self.list=list
class TRU:
    def __init__(self, type=None,val=None):
        self.type=type
        self.val=val
class FALS:
    def __init__(self, type=None,val=None):
        self.type=type
        self.val=val
class CHR:
    def __init__(self, type=None,pos=None,val=None):
        self.type=type
        self.pos=pos
        self.val=val    
class STR:
    def __init__(self, type=None,val=None,pos=None):
        self.type=type
        self.val=val
        self.pos=pos
class NUM:
    def __init__(self, type=None,val=None,pos=None):
        self.type=type
        self.val=val
        self.pos=pos
class t_attrib:
    def __init__(self, t_nont=None, nSize=None,_=None):
        self.t_nont=t_nont
        self.nSize=nSize
        self._=_

global SymbolTable
SymbolTable = []
global SymbolTableLast
SymbolTableLast = []
global nCurrentLevel
nCurrentLevel = -1

global labelNo
labelNo =0
global nFuncs
nFuncs = 0
global constPool
constPool = 0
global curFunction
curFunction = object()

def newLabel():
    global labelNo
    labelNo+=1
    return labelNo-1

def NewBlock():
    global nCurrentLevel
    global SymbolTable
    global SymbolTableLast
    nCurrentLevel+=1
    SymbolTable[nCurrentLevel]=None
    SymbolTableLast[nCurrentLevel]=None
    return nCurrentLevel

def EndBlock():
    global nCurrentLevel
    nCurrentLevel=nCurrentLevel-1
    return nCurrentLevel

def Define(aName):
    obj = object('aName,None')
    if (SymbolTable[nCurrentLevel]==None):
        SymbolTable[nCurrentLevel]=obj
        SymbolTableLast[nCurrentLevel]=obj
    else:
        SymbolTable[nCurrentLevel].pNext = obj
        SymbolTableLast[nCurrentLevel]=obj
    return obj

def Search (aName):
    obj = SymbolTable[nCurrentLevel]
    while (obj!= None):
        if (obj.nName == aName):
            break
        else:
            obj=obj.pNext
    return obj

def Find(aName):
    obj = None
    for i in nCurrentLevel:
        obj = SymbolTable[i]
        while (obj!=None):
            if (obj.nName==aName):
                break
            else:
                obj = obj.pNext
        if (obj!=None):
            break
        return obj

hasErr = False
StackSem = []
int_ = object(-1,None,SCALAR_TYPE_)
char_ = object(-1,None,SCALAR_TYPE_)
bool_ = object(-1,None,SCALAR_TYPE_)
string_ = object(-1,None,SCALAR_TYPE_)
universal_ = object(-1,None,SCALAR_TYPE_)

def Error(code):
    hasErr = True
    print("Linha: "+str(lxc.linha)+" - ")
    if (code==ERR_NO_DECL):
        print("Variável não previamente declarada")
    elif (code==ERR_REDCL):
        print("Variável já declarada")
    elif (code==ERR_TYPE_EXPECTED):
        print("Tipo não declarado previamente")
    elif (code==ERR_BOOL_TYPE_EXPECTED):
        print("Tipo boolean é esperado")
    elif (code==ERR_INVALID_TYPE):
        print("Tipo é invalido para a operação realizada")
    elif (code==ERR_TYPE_MISMATCH):
        print("Tipo é invalido para a operação realizada")
    elif (code==ERR_KIND_NOT_STRUCT):
        print("A operação pode ser realizada somente em tipos Struct")
    elif (code==ERR_FIELD_NOT_DECL):
        print("Campo não foi declarado")
    elif (code==ERR_KIND_NOT_ARRAY):
        print("A operação é destinada somente para Array")
    elif (code==ERR_INVALID_INDEX_TYPE):
        print("O índice é inválido para o Array")
    elif(code==ERR_KIND_NOT_VAR):
        print("A operação somente válida para tipo Var")
    elif(code==ERR_KIND_NOT_FUNCTION):
        print("A operação somente válida para tipo Function")
    elif (code==ERR_TOO_FEW_ARGS):
        print("O número de parâmetros é menor do que o especificado")
    elif (code==ERR_TOO_MANY_ARG):
        print("O número de parametros é maior do que o especificado")
    elif (code==ERR_PARAM_TYPE):
        print("O tipo especificado não é válido")
    elif (code==ERR_RETURN_TYPE_MISMATCH):
        print("O tipo de retorno não é compatível com o tipo especificado na função")

def CheckTypes(t1,t2):
    if (t1==t2):
        return True
    elif (t1==universal_ or t2==universal_):
        return True
    elif (t1.eKind==UNIVERSAL_ or t2.eKind==UNIVERSAL_):
        return True
    elif (t1.eKind==ALIAS_TYPE_ and t2.eKind!=ALIAS_TYPE_):
        return CheckTypes(t1._.tipoBase,t2)
    elif(t1.eKind!=ALIAS_TYPE_ and t2.eKind==ALIAS_TYPE_):
        return CheckTypes(t1,t2._.tipoBase)
    elif (t1.eKind==t2.eKind):
        if (t1.eKind==ALIAS_TYPE_):
            return CheckTypes(t1._.tipoBase,t2._.tipoBase)
        elif (t1.eKind==ARRAY_TYPE_):
            if(t1._.nNumElems==t2._.nNumElems):
                return CheckTypes(t1._.tipoElemento,t2._.tipoElemento)
        elif (t1.eKind==STRUCT_TYPE_):
            f1 = t1._.campos
            f2 = t2._.campos
            while (f1 != None and f2 != None):
                if (not CheckTypes(f1._.tipo,f2._.tipo)):
                    return False
            return (f1==None and f2==None)
    else:
        return False

global name,n,rLabel,rLabel1,rLabel2 #tirar labels?
name,n,rLabel,rLabel1,rLabel2=None
global p,t,f
p,t,f= object()
global IDD_,IDU_,ID_,T_,LI_,LI0_,LI1_,TRU_,FALS_,STR_,CHR_,NUM_,DC_,DC0_,DC1_,LP_,LP0_,LP1_,E_,E0_,E1_,L_,L0_,L1_,R_,R0_,R1_,Y_,Y0_,Y1_,F_,F0_,F1_,LV_,LV0_,LV1_,MC_,LE_,LE0_,LE1_,MT_,ME_,MW_
IDD_,IDU_,ID_,T_,LI_,LI0_,LI1_,TRU_,FALS_,STR_,CHR_,NUM_,DC_,DC0_,DC1_,LP_,LP0_,LP1_,E_,E0_,E1_,L_,L0_,L1_,R_,R0_,R1_,Y_,Y0_,Y1_,F_,F0_,F1_,LV_,LV0_,LV1_,MC_,LE_,LE0_,LE1_,MT_,ME_,MW_=t_attrib()

def Semantics(rule):
    global name,n,rLabel
    global p,t,f
    global IDD_,IDU_,ID_,T_,LI_,LI0_,LI1_,TRU_,FALS_,STR_,CHR_,NUM_,DC_,DC0_,DC1_,LP_,LP0_,LP1_,E_,E0_,E1_,L_,L0_,L1_,R_,R0_,R1_,Y_,Y0_,Y1_,F_,F0_,F1_,LV_,LV0_,LV1_,MC_,LE_,LE0_,LE1_,MT_,ME_,MW_
    global curFunction

    if (rule == IDD_RULE):
        name = lxc.tokenSecundario
        p=Search(name)
        if (p!=None):
            Error(ERR_REDCL)
        else:
            p=Define(name)
        p.eKind=NO_KIND_DEF_
        IDD_.t_nont=stt.IDD
        IDD_._=ID(p,name)
        StackSem.append(IDD_)

    elif(rule == IDU_RULE):
        name=lxc.tokenSecundario
        p=Find(name)
        if (p==None):
            Error(ERR_NO_DECL)
            p=Define(name)
        IDU_.t_nont=stt.IDU
        IDU_._=ID(p,name)
        StackSem.append(IDU_)

    elif(rule == ID_RULE):
        name=lxc.tokenSecundario
        ID_.t_nont=stt.ID
        ID_._=ID(None,name)
        StackSem.push(ID_)

    elif(rule == T_IDU_RULE):
        IDU_=StackSem.pop()
        p=IDU_._.objeto
        if(IS_TYPE_KIND(p.eKind) or p.eKind==UNIVERSAL_):
            T_=t_attrib(stt.T,p._.nSize,T(p))
        else:
            T_=t_attrib(stt.T,0,T(universal_))
            Error(ERR_TYPE_EXPECTED)
        StackSem.append(T_)

    elif(rule == T_INTEGER_RULE):
        T_=t_attrib(stt.T,1,T(int_))
        StackSem.append(T_)

    elif(rule == T_CHAR_RULE):
        T_=t_attrib(stt.T,1,T(char_))
        StackSem.append(T_)

    elif(rule==T_BOOL_RULE):
        T_=t_attrib(stt.T,1,T(bool_))
        StackSem.append(T_)

    elif(rule==T_STRING_RULE):
        T_=t_attrib(T,1,T(string_))
        StackSem.append(T_)

    elif (rule==LI_IDD_RULE):
        IDD_=StackSem.pop()
        LI_=t_attrib(stt.LI,None,LI(IDD_._.objeto))
        StackSem.append(LI_)
    elif (rule==LI_COMMA_RULE):
        IDD_=StackSem.pop()
        LI1_=StackSem.pop()
        LI0_=t_attrib(stt.LI,None,LI(LI1_._.list))
        StackSem.append(LI0_)
    elif(rule==DV_VAR_RULE):
        T_=StackSem.pop()
        t=T_._.type
        LI_=StackSem.pop()
        p=LI_._.list
        n=curFunction._.nVars
        while(p!=None and p.eKind==NO_KIND_DEF_):
            p.eKind=VAR_
            p._=Var(t,n,T_.nSize)
            n+=T_.nSize
            p=p.pNext
        curFunction._.nVars=n

    elif(rule==TRUE_RULE):
        TRU_=t_attrib(stt.TRU,None,TRU(bool_,True)) #tem problema ter o None?
        StackSem.append(TRU_)
    elif(rule==FALSE_RULE):
        FALS_=t_attrib(stt.FALS,None,FALS(bool_,False))
        StackSem.append(FALS_)
    elif(rule==CHR_RULE):
        CHR_=t_attrib(stt.CHR,None,CHR(char_,lxc.tokenSecundario,lxc.getConst(lxc.tokenSecundario)))
        StackSem.append(CHR_)
    elif(rule==STR_RULE):
        STR_=t_attrib(stt.STR,None,STR(string_,lxc.getConst(lxc.tokenSecundario),lxc.tokenSecundario))
        StackSem.append(STR_)
    elif(rule==NUM_RULE):
        NUM_=t_attrib(stt.NUM,None,NUM(int_,lxc.getConst(lxc.tokenSecundario),lxc.tokenSecundario))
        StackSem.append(NUM_)

    elif(rule==DT_ARRAY_RULE):
        T_=StackSem.pop()
        NUM_=StackSem.pop()
        IDD_=StackSem.pop()
        p=IDD_._.objeto
        n=NUM_._.val
        t=T_._.type
        p.eKind=ARRAY_TYPE_
        p._=Array(t,n,n*T_.nSize)

    elif(rule==DT_ALIAS_RULE):
        T_=StackSem.pop()
        IDD_=StackSem.pop()
        p=IDD_._.objeto
        t=T_._.type
        p.eKind=ALIAS_TYPE_
        p._=Alias(t,T_.nSize)

    elif(rule==DC_LI_RULE):
        T_=StackSem.pop()
        LI_=StackSem.pop()
        p=LI_._.list
        t=T_._.type
        n=0
        while(p!=None and p.eKind==NO_KIND_DEF_):
            p.eKind=FIELD_
            p._=Field(t,n,T_.nSize)
            n=n+T_.nSize
            p=p.pNext
        DC_=t_attrib(stt.DC,n,DC(LI_._.list))
        StackSem(DC_)
    elif(rule==DC_DC_RULE):
        T_=StackSem.pop()
        LI_=StackSem.pop()
        DC1_=StackSem.pop()
        p=LI_._.list
        t=T_._.type
        n=DC1_.nSize
        while(p!=None and p.eKind==NO_KIND_DEF_):
            p.eKind=FIELD_
            p._=Field(t,n,T_.nSize)
            n=n+T_.nSize
            p=p.pNext
        DC0_=t_attrib(stt.DC,n,DC(DC1_._.list))
        StackSem.append(DC0_)
    elif(rule==NB_RULE):
        NewBlock()

    elif(rule==DT_STRUCT_RULE):
        DC_=StackSem.pop()
        IDD_=StackSem.pop()
        p=IDD_._.objeto
        p.eKind=STRUCT_TYPE_
        p._=Struct(DC_._.list,DC_.nSize)
        EndBlock()

    elif (rule==LP_IDD_RULE):
        T_=StackSem.pop()
        IDD_=StackSem.pop()
        p=IDD_._.objeto
        p.eKind=PARAM_
        p._=Param(t,0,T_.nSize)
        LP_=t_attrib(stt.LP,T_.nSize,LP(p))
        StackSem.append(LP_)
    elif(rule==LP_LP_RULE):
        T_=StackSem.pop()
        IDD_=StackSem.pop()
        LP1_=StackSem.pop()
        p=IDD_._.objeto
        t=T_._.type
        n=LP1_.nSize
        p.eKind=PARAM_
        p._=Param(t,n,T_.nSize)
        LP0_=t_attrib(stt.LP,n+T_.nSize,LP(LP1_._.list))
    elif (rule==NF_RULE):
        IDD_=StackSem.pop()
        f=IDD_._.objeto
        f.eKind=FUNCTION_
        f._=Function(f._.pRetType,f._.pParams,nFuncs,0,0)
        nFuncs+=1
        #f._=Function(None,None,None,0,0) #E SE F JÁ TIVER VALORES NOS 3 PRIMEIROS CAMPOS?
        NewBlock()

    elif(rule==MF_RULE):
        T_=StackSem.pop()
        LP_=StackSem.pop()
        IDD_=StackSem.pop()
        f=IDD_._.objeto
        f.eKind=FUNCTION_
        f._=Function(T_._.type,LP_._.list,f._.nIndex,LP_.nSize,LP_.nSize) #E se F n for function
        curFunction=f
        file.write("BEGIN_FUNC "+str(f._.nIndex)+" "+str(f._.nParams))

    elif(rule==DF_RULE):
        EndBlock()
        file.write("END_FUNC")

    elif (rule == U_IF_RULE):
		MT_ = StackSem.pop()
		E_ = StackSem.pop()
		t = E_._.type
		if (not CheckTypes(t,bool_)):
			Error(ERR_BOOL_TYPE_EXPECTED)
		file.write("L"+str(MT_._.label))
        
    elif (rule == U_IF_ELSE_U_RULE):
		ME_ = StackSem.pop()
		MT_ = StackSem.pop()
		E_ = StackSem.pop()
		t = E_._.type
		if (not CheckTypes(t,bool_)):
			Error(ERR_BOOL_TYPE_EXPECTED)
		file.write("L"+str(ME_._.label))

    elif (rule == M_IF_ELSE_M_RULE):
		ME_ = StackSem.pop()
		MT_ = StackSem.pop()
		E_ = StackSem.pop()
		t = E_._.type
		if not CheckTypes(t,bool_):
			Error(ERR_BOOL_TYPE_EXPECTED)
		file.write("L"+str(ME_._.label))

    elif (rule == M_WHILE_RULE):
		MT_ = StackSem.pop()
		E_ = StackSem.pop()
		MW_ = StackSem.pop()
		t = E_._.type
		if (not CheckTypes(t,bool_)):
			Error(ERR_BOOL_TYPE_EXPECTED)
		file.write("\tJMP_BW L"+str(MW_._.label)+"\nL"+str(MT_._.label))        

    elif (rule == M_DO_WHILE_RULE):
		E_ = StackSem.pop()
		MW_ = StackSem.pop()
		t = E_._.type
		if (not CheckTypes(t,bool_)):
			Error(ERR_BOOL_TYPE_EXPECTED)
		file.write("\tNOT\n\tTJMP_BW L"+str(MW_._.label))  

    elif(rule == E_AND_RULE):
        L_=StackSem.pop()
        E1_=StackSem.pop()
        if(not CheckTypes(E1_._.type,bool_)):
            Error(ERR_BOOL_TYPE_EXPECTED)
        if(not CheckTypes(L_._.type,bool_)):
            Error(ERR_BOOL_TYPE_EXPECTED)
        E0_=t_attrib(stt.E,None,E(bool_)) #Pode usar None nos campos não declarados?
        StackSem.append(E0_)
        file.write("\tAND")
    
    elif(rule == E_OR_RULE):
        L_=StackSem.pop()
        E1_=StackSem.pop()
        if(not CheckTypes(E1_._.type,bool_)):
            Error(ERR_BOOL_TYPE_EXPECTED)
        if(not CheckTypes(L_._.type,bool_)):
            Error(ERR_BOOL_TYPE_EXPECTED)
        E0_=t_attrib(stt.E,None,E(bool_))
        StackSem.push(E0_)
        file.write("\tOR")

    elif(rule == E_L_RULE):
        L_=StackSem.pop()
        E_=t_attrib(stt.E,None,E(L_._.type))
        StackSem.append(E_)
    elif(rule == L_LESS_THAN_RULE):
        R_=StackSem.pop()
        L1_=StackSem.pop()
        if(not CheckTypes(L1_._.type,R_._.type)):
            Error(ERR_TYPE_MISMATCH)
        L0_=t_attrib(stt.L,None,L(bool_))
        StackSem.append(L0_)
        file.write("\tLT")

    elif(rule == L_GREATER_THAN_RULE):
        R_=StackSem.pop()
        L1_=StackSem.pop()
        if(not CheckTypes(L1_._.type,R_._.type)):
            Error(ERR_TYPE_MISMATCH)
        L0_=t_attrib(stt.L,None,bool_)
        StackSem.append(L0_)
        file.write("\tGT")

    elif(rule == L_LESS_EQUAL_RULE):
        R_=StackSem.pop()
        L1=StackSem.pop()
        if(not CheckTypes(L1_._.type,R_._.type)):
            Error(ERR_TYPE_MISMATCH)
        L0_=t_attrib(stt.L,None,bool_)
        StackSem.append(L0_)
        file.write("\tLE")

    elif (rule == L_GREATER_EQUAL_RULE):
        R_=StackSem.pop()
        L1=StackSem.pop()
        if(not CheckTypes(L1_._.type,R_._.type)):
            Error(ERR_TYPE_MISMATCH)
        L0_=t_attrib(stt.L,None,bool_)
        StackSem.append(L0_)
        file.write("\tGE")

    elif(rule == L_EQUAL_EQUAL_RULE):
        R_=StackSem.pop()
        L1=StackSem.pop()
        if(not CheckTypes(L1_._.type,R_._.type)):
            Error(ERR_TYPE_MISMATCH)
        L0_=t_attrib(stt.L,None,bool_)
        StackSem.append(L0_)
        file.write("\tEQ")

    elif(rule == L_NOT_EQUAL_RULE):
        R_=StackSem.pop()
        L1=StackSem.pop()
        if(not CheckTypes(L1_._.type,R_._.type)):
            Error(ERR_TYPE_MISMATCH)
        L0_=t_attrib(stt.L,None,bool_)
        StackSem.append(L0_)
        file.write("\tNE")

    elif(rule == L_R_RULE):
        R_=StackSem.pop()
        L_=t_attrib(stt.L,None,L(R_._.type))
        StackSem.append(L_)
    elif(rule == R_PLUS_RULE):
        Y_=StackSem.pop()
        R1_=StackSem.pop()
        if(not CheckTypes(R1_._.type,Y_._.type)):
            Error(ERR_TYPE_MISMATCH)
        if((not CheckTypes(R1_._.type,int_)) and (not CheckTypes(R1_._.type,string_))):
            Error(ERR_INVALID_TYPE)
        R0_=t_attrib(stt.R,None,R(R1_._.type))
        StackSem.append(R0_)
        file.write("\tADD")

    elif(rule == R_MINUS_RULE):
        Y_=StackSem.pop()
        R1_=StackSem.pop()
        if(not CheckTypes(R1_._.type,Y_._.type)):
            Error(ERR_TYPE_MISMATCH)
        if(not CheckTypes(R1_._.type,int_)):
            Error(ERR_INVALID_TYPE)
        R0_=t_attrib(stt.R,None,R(R1_._.type))
        StackSem.append(R0_)
        file.write("\tSUB")

    elif(rule==R_Y_RULE):
        Y_=StackSem.top()
        StackSem.pop()
        R_=t_attrib(stt.R,None,R(Y_._.type))
        StackSem.append(R_)
    elif(rule==Y_TIMES_RULE):
        F_=StackSem.pop()
        Y1_=StackSem.pop()
        if(not CheckTypes(Y1_._.type,F_._.type)):
            Error(ERR_TYPE_MISMATCH)
        if(not CheckTypes(Y1_._.type,int_)):
            Error(ERR_INVALID_TYPE)
        Y0_=t_attrib(stt.Y,None,Y(Y1_._.type))
        StackSem(Y0_)
        file.write("\tMUL")

    elif(rule==Y_DIVIDE_RULE):
        F_=StackSem.pop()
        Y1_=StackSem.pop()
        if(not CheckTypes(Y1_._.type,F_._.type)):
            Error(ERR_TYPE_MISMATCH)
        if(not CheckTypes(Y1_._.type,int_)):
            Error(ERR_INVALID_TYPE)
        Y0_=t_attrib(stt.Y,None,Y(Y1_._.type))
        StackSem(Y0_)
        file.write("\tDIV")

    elif(rule==Y_F_RULE):
        F_=StackSem.pop()
        Y_=t_attrib(stt.Y,None,Y(F_._.type))
        StackSem.append(Y_)
    elif(rule==F_LV_RULE):
        LV_=StackSem.pop()
        n=LV_._.type._.nSize 
        F_=t_attrib(stt.F,None,F(LV_._.type))
        StackSem.append(F_)
        file.write("\tDE_REF "+str(n))
    elif(rule==F_LEFT_PLUS_PLUS_RULE):
        LV_=StackSem.pop()
        t=LV_._.type
        if(not CheckTypes(t,int_)):
            Error(ERR_INVALID_TYPE)
        F_=t_attrib(stt.F,None,F(int_))
        file.write("\tDUP\n\tDUP\n\tDE_REF 1")
        file.write("\tINC\n\tSTORE REF 1\n\tDE_REF 1")


    elif(rule==F_LEFT_MINUS_MINUS_RULE):
        LV_=StackSem.pop()
        t=LV_._.type
        if(not CheckTypes(t,int_)):
            Error(ERR_INVALID_TYPE)
        F_=t_attrib(stt.F,None,F(LV_._.type))
        StackSem.append(F_)
        file.write("\tDUP\n\tDUP\n\tDE_REF 1")
        file.write("\tDEC\n\tSTORE_REF 1\n\tDE_REF 1")

    elif(rule==F_RIGHT_PLUS_PLUS_RULE):
        LV_=StackSem.pop()
        t=LV_._.type
        if(not CheckTypes(t,int_)):
            Error(ERR_INVALID_TYPE)
        F_=t_attrib(stt.F,None,F(LV_._.type))
        StackSem.append(F_)
        file.write("\tDUP\n\tDUP\n\tDE_REF 1")
        file.write("\tINC\n\tSTORE_REF 1\n\tDE_REF 1")
        file.write("\tDEC")

    elif(rule==F_RIGHT_MINUS_MINUS_RULE):
        LV_=StackSem.pop()
        t=LV_._.type
        if(not CheckTypes(t,int_)):
            Error(ERR_INVALID_TYPE)
        F_=t_attrib(stt.F,None,F(t))
        StackSem.append(F_)
        file.write("\tDUP\n\tDUP\n\tDE_REF 1")
        file.write("\tDEC\n\tSTORE_REF 1\n\tDE_REF 1")
        file.write("\tINC")

    elif(rule==F_PARENTHESIS_E_RULE):
        E_=StackSem.pop()
        F_=t_attrib(stt.F,None,F(E_._.type))
        StackSem.append(F_)
    elif(rule==F_MINUS_F_RULE):
        F1_=StackSem.pop()
        t=F1_._.type
        if(not CheckTypes(t,int_)):
            Error(ERR_INVALID_TYPE)
        F0_=t_attrib(stt.F,None,F(t))
        StackSem.append(F0_)
        file.write("\tNEG")

    elif(rule==F_NOT_F_RULE):
        F1_=StackSem.pop()
        t=F1_._.type
        if(not CheckTypes(t,bool_)):
            Error(ERR_INVALID_TYPE)
        F0_=t_attrib(stt.F,None,F(t))
        StackSem.append(F0_)
        file.write("\tNOT")

    elif(rule==F_TRUE_RULE):
        TRU_=StackSem.pop()
        F_=t_attrib(stt.F,None,F(bool_))
        StackSem.append(F_)
        file.write("\tLOAD_TRUE")

    elif(rule==F_FALSE_RULE):
        FALS_=StackSem.pop()
        F_=t_attrib(stt.F,None,F(bool_))
        StackSem.append(F_)
        file.write("\tLOAD_FALSE")

    elif(rule==F_CHR_RULE):
        CHR_=StackSem.pop()
        F_=t_attrib(stt.F,None,F(char_))
        StackSem.append(F_)
        n=lxc.tokenSecundario
        file.write("\tLOAD_CONST "+str(constPool))
        constPool+=1

    elif(rule==F_STR_RULE):
        STR_=StackSem.pop()
        F_=t_attrib(stt.F,None,F(string_))
        StackSem.append(F_)
        n=lxc.tokenSecundario
        file.write("\tLOAD_CONST "+str(constPool))
        constPool+=1

    elif(rule==F_NUM_RULE):
        NUM_=StackSem.pop()
        F_=t_attrib(stt.F,None,F(int_)) # os int_ etc são ponteiros no voltan, o que isso muda? Eles apontem pro ultimo que é o tipo?
        StackSem.append(F_)
        n=lxc.tokenSecundario
        file.write("\tLOAD_CONST "+str(constPool))
        constPool+=1

    elif(rule == LV_DOT_RULE):
        ID_=StackSem.pop()
        LV1_=StackSem.pop()
        t=LV1_._.type
        if(t.eKind!=STRUCT_TYPE_):
            if(t.eKind!=UNIVERSAL_):
                Error(ERR_KIND_NOT_STRUCT)
            LV0_=t_attrib(stt.LV,None,LV(universal_))
        else:
            p=t._.campos
            while(p!=None):
                if(p.aName==ID_._.name):
                    break
                p=p.pNext
            if(p==None):
                Error(ERR_FIELD_NOT_DECL)
                LV0_=t_attrib(stt.LV,None,LV(universal_))
            else:
                LV0_=t_attrib(stt.LV,None,LV(p._.tipo))
                LV0._.type._=Type(None,p._.nSize)
        StackSem.append(LV0_)
        file.write("\tADD "+str(p._.nIndex))

    elif(rule == LV_SQUARE_RULE):
        E_=StackSem.pop()
        LV1=StackSem.pop()
        t=LV1_._.type
        if(CheckTypes(t,string_)):
            LV0_=t_attrib(stt.LV,None,LV(char_))
        elif(t.eKind!=ARRAY_TYPE_):
            if(t.eKind!=UNIVERSAL_):
                Error(ERR_KIND_NOT_ARRAY)
            LV0_=t_attrib(stt.LV,None,LV(universal_))
        else:
            LV0_=t_attrib(stt.LV,None,LV(t._.tipoElemento))
            n=t._tipoElemento._.nSize
            file.write("\tMUL "+str(n))
            file.write("\tADD")
        if(not CheckTypes(E_._.type,int_)):
            Error(ERR_INVALID_INDEX_TYPE)
        StackSem.append(LV0_)


    elif(rule == LV_IDU_RULE):
        IDU_=StackSem.pop()
        p=IDU_._.objeto
        if(p.eKind!=VAR_ and p.eKind!=PARAM_):
            if(p.eKind!=UNIVERSAL_):
                Error(ERR_KIND_NOT_VAR)
            LV_=t_attrib(stt.LV,None,LV(universal_))
        else:
            LV_=t_attrib(stt.LV,None,LV(p._tipo))
            LV_._.type._=Type(None,p._.nSize)
        StackSem.append(LV_)
        file.write("\tLOAD_REF "+str(p._.nIndex))

    #colocar regras E

    elif(rule==MC_RULE):
        IDU_=StackSem.pop()
        f=IDU_._.objeto
        if(f.eKind!=FUNCTION_):
            MC_=t_attrib(stt.MC,None,MC(universal_,None,True))
        else:
            MC_=t_attrib(stt.MC,None,MC(f._.pRetType,f._.pParams,False))
        StackSem.append(MC_)
    elif(rule==LE_E_RULE):
        E_=StackSem.pop()
        MC_=StackSem.pop()
        LE_=t_attrib(stt.LE,None,LE(None,None,MC_._.err,1))
        if(not MC_._.err):
            p=MC_._.param 
            if(p==None):
                Error(ERR_TOO_MANY_ARG)
                LE_._.err=True
            else:
                if(not CheckTypes(p._.tipo,E_._.type)):
                    Error(ERR_PARAM_TYPE)
                LE_._.param=p.pNext
                LE_._.n=n+1
        StackSem.append(LE_)
    elif(rule==LE_LE_RULE):
        E_=StackSem.pop()
        LE1_=StackSem.pop()
        LE0_=t_attrib(stt.LE,None,LE(None,None,L1_._.err,LE1_._.n))
        if(not LE1_._.err):
            p=LE1_._.param
            if(p==None):
                Error(ERR_TOO_MANY_ARG)
                LE0_._.err=True
            else:
                if(not CheckTypes(p._.tipo,E_._.type)):
                    Error(ERR_PARAM_TYPE)
                LE0._.param=p.pNext
                LE0._.n=n+1
        StackSem.append(LE0_)
    elif(rule==F_IDU_MC_RULE):
        LE_=StackSem.pop()
        MC_=StackSem.pop()
        IDU_=StackSem.pop()
        f=IDU_._.objeto
        F_=t_attrib(stt.F,None,F(MC_._.type))
        if(not LE_._.err):
            if(LE_._.n-1 < f._nParams and LE_._.n != 0):
                Error(ERR_TOO_FEW_ARGS)
            elif (LE_._.n-1 > f._.nParams):
                Error(ERR_TOO_MANY_ARG)
        StackSem.append(F_)
        file.write("\tCALL "+str(f._.nIndex))

    elif(rule==MT_RULE):
        rLabel=newLabel()
        MT_=t_attrib(stt.MT,None,MT(rLabel))
        StackSem.append(MT_)
        file.write("\tTJMP_FW L"+str(rLabel))

    elif(rule==ME_RULE):
        MT_=StackSem.pop()
        rLabel=newLabel()
        ME._.label=rLabel
        ME_.t_nont=stt.ME
        StackSem.append(ME_)
        file.write("\tTJMP_FW L"+str(rLabel))
        file.write("L"+str(MT_._.label))

    elif(rule==MW_RULE):
        rLabel=newLabel()
        MW_._.label=rLabel
        StackSem.append(MW_)
        file.write("L"+str(rLabel))



                
