# -*- coding: utf-8 -*-
import analisadorLexico as lxc
import analisadorSintatico as stt

lxc.arq = open('codigo2.ssl', 'r')
stt.analisarSintaticamente()

lxc.arq.close()