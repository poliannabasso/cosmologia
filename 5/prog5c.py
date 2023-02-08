#! /usr/bin/python3
# -*- coding: utf-8 -*-
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# OBJETIVO:
#   Gráfico da curva de Rotação de Andrômeda, com componentes.
#_________________________________________________________
# MODO DE USAR:
#   ./prog004.py
#_________________________________________________________
# Universidade Federal de Santa Catarina
# Programa Astrofísica para Todos!
# Curso de Cosmologia
# Prof. Alexandre Zabot
# https://astrofisica.ufsc.br
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
import numpy as np
import matplotlib.pyplot as plt
from lib05 import vb,vd








D = np.loadtxt( "dados/m31.dat" , dtype=float ).transpose()
plt.errorbar( D[0], D[1], yerr=D[3], fmt="o", label="Observado")



rmax=1000  # kpc

r = np.linspace(0.1,rmax,10000)


# Valores possíveis
Vb = vb( r, 0.1, 0.6e10 )
Vd = vd( r, 8.0, 4.0e11 )

# Valores da Tab 6 de Sofue 2016
# Vb = vb( r, 0.12, 0.92e10 )
# Vd = vd( r, 4.9, 0.9e11 )



V  = np.sqrt(Vb*Vb + Vd*Vd)

plt.plot( r, Vb, "--", label="Bojo" )
plt.plot( r, Vd, "--", label="Disco" )
plt.plot( r, V , "-", lw=2, label="Bojo + Disco" )




plt.margins(0.1)
plt.xlim(0,rmax)
plt.ylim(0,300)
plt.title(u"Curva de rotação de M31")
plt.xlabel(u"Raio (kpc)")
plt.ylabel(u"Velocidade (km/s)")
plt.legend(loc="upper right")
plt.grid()
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.96, top=0.9)
plt.show()
