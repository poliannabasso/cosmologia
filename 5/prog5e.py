#! /usr/bin/python3
# -*- coding: utf-8 -*-
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# OBJETIVO:
#   Gráfico da curva de Rotação de Andrômeda, com componentes, incluindo o Halo de Matéria
#  escura com perfil isotérmico.
#_________________________________________________________
# MODO DE USAR:
#   ./prog005.py
#_________________________________________________________
# Universidade Federal de Santa Catarina
# Programa Astrofísica para Todos!
# Curso de Cosmologia
# Prof. Alexandre Zabot
# https://astrofisica.ufsc.br
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
import numpy as np
import matplotlib.pyplot as plt
from lib05 import vb,vd,vh








D = np.loadtxt( "dados/m31.dat" , dtype=float ).transpose()
plt.errorbar( D[0], D[1], yerr=D[3], fmt="o", label="Observado")



rmax=1350

r = np.linspace(0.1,rmax,30000)



# Conjunto possível de valores
Vb = vb( r, 0.1, 0.6e10 )
Vd = vd( r, 8.0, 4.0e11 )
Vh = vh( r, 200.0, 250    )





V  = np.sqrt(Vb*Vb + Vd*Vd + Vh*Vh)



plt.plot( r, Vb   , "--", label="Bojo" )
plt.plot( r, Vd   , "--", label="Disco" )
plt.plot( r, Vh   , "--", label=u"Matéria Escura" )
plt.plot( r, V, "-", lw=2, label="Bojo + Disco + ME" )




plt.margins(0.1)
plt.xlim(0,rmax)
plt.ylim(0,300)
plt.title(u"Curva de rotação de M31")
plt.xlabel(u"Raio (kpc)")
plt.ylabel(u"Velocidade (km/s)")
plt.legend(loc="lower right")
plt.grid()
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.96, top=0.9)
plt.show()
