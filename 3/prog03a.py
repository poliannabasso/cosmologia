#! /usr/bin/python3
# -*- coding: utf-8 -*-
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# OBJETIVO:
#   Fazer o gráfico da força gravitacional gerada por um anel de matéria sobre uma
#  partícula no eixo do anel.
#_________________________________________________________
# MODO DE USAR:
#   ./prog001.py
#_________________________________________________________
# Universidade Federal de Santa Catarina
# Programa Astrofísica para Todos!
# Curso de Cosmologia
# Prof. Alexandre Zabot
# https://astrofisica.ufsc.br
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
import numpy as np
import matplotlib.pyplot as plt



u = np.linspace( 0.1, 10, 1000 )

fanel    = 2*np.sqrt(2) * u / np.power( u*u + 1, 1.5 )
fpontual = 1.0 / ( u*u )


plt.plot( u, fanel   , "-" , label="Anel")
plt.plot( u, fpontual, "--", label="Ponto")

plt.axvline(1,color="black",linestyle="--")


plt.legend(loc="best")
plt.ylim(0,1.2)
plt.grid()
plt.show()




