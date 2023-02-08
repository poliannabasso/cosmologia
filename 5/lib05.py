#! /usr/bin/python3
# -*- coding: utf-8 -*-
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# OBJETIVO:
#   Gráfico de velocidade de rotação de uma galáxia espiral para a componente do Bojo
#  seguindo o perfil exponencial
#_________________________________________________________
# MODO DE USAR:
#   ./prog002.py
#_________________________________________________________
# Universidade Federal de Santa Catarina
# Programa Astrofísica para Todos!
# Curso de Cosmologia
# Prof. Alexandre Zabot
# https://astrofisica.ufsc.br
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
import math
import numpy as np
import scipy.constants
import astropy.constants
from scipy.special import i0,i1,k0,k1



def vb(r,a,M):
  """
  Recebe:
    r : Numpy Array de raios, em kpc
    a : Parâmetro de escala do bojo, em kpc
    M : Massa total do Bojo em Massas Solares
  Retorna:
    Numpy array com velocidades causadas pelo bojo em km/s
  """
  G    = scipy.constants.gravitational_constant
  kpc  = 1000*scipy.constants.parsec
  Msol = astropy.constants.M_sun.to_value()
  C    = math.sqrt( G * (M*Msol) / (a*kpc) )
  
  x = r/a
  v = C * np.sqrt( (1-np.exp(-x)*( 1 + x + x*x/2.0 ))/x )
  v /= 1000.0 # m/s -> km/s
  
  return v




def vd(r,a,M):
  """
  Recebe:
    r : Numpy Array de raios, em kpc
    a : Parâmetro de escala do disco, em kpc
    M : Massa total do Disco em Massas Solares
  Retorna:
    Numpy array com velocidades causadas pelo disco em km/s
  """
  G    = scipy.constants.gravitational_constant
  kpc  = 1000*scipy.constants.parsec
  Msol = astropy.constants.M_sun.to_value()
  C    = math.sqrt( 2 * G * (M*Msol) / (a*kpc) )
  
  x = r/(2.0*a)
  v = C * np.sqrt( x*x*( i0(x)*k0(x) - i1(x)*k1(x) ) )
  v /= 1000.0 # m/s -> km/s
  
  return v





def vh(r,a,vc):
  """
  Recebe:
    r  : Numpy Array de raios, em kpc
    a  : Parâmetro de escala do halo, em kpc
    vc : Velocidade terminal, em km/s
  Retorna:
    Numpy array com velocidades causadas pelo bojo em km/s
  """
  
  x = r/a
  v = vc * np.sqrt( 1 - np.arctan(x)/x )
  
  return v
  
  






