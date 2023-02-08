#! /usr/bin/python3
# -*- coding: utf-8 -*-
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# OBJETIVO:
#   Gráfico de velocidade de rotação de uma galáxia espiral para a componente do 
#  Halo de Matéria Escura com perfil isotérmico.
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
from lib05 import vh


  
  
r = np.linspace(0.01,1000,10000)

plt.plot( r, vh( r,  20.0, 200 ), "b-" , label="$a_h =  20 kpc, v_h = 200 km/s$" )
plt.plot( r, vh( r, 100.0, 200 ), "r-" , label="$a_h = 100 kpc, v_h = 200 km/s$" )
plt.plot( r, vh( r,  20.0, 300 ), "b--", label="$a_h =  20 kpc, v_h = 300 km/s$" )
plt.plot( r, vh( r, 100.0, 300 ), "r--", label="$a_h = 100 kpc, v_h = 300 km/s$" )



plt.xlabel(u"Raio (kpc)")
plt.ylabel(u"Velocidade (km/s)")

plt.legend(loc="lower right")
plt.grid()
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.96, top=0.95)
plt.show()










