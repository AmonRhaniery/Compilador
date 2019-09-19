# -*- coding: utf-8 -*-
import analisadorLexico as lxc
import analisadorSintatico as stt

arq = open('codigo2.ssl', 'r')

lxc.analisarLexicamente(arq)
stt.analisarSintaticamente()

arq.close()