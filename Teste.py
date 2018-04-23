#!/usr/bin/env python3

from movimento import *

from ev3dev.ev3 import *
from time import sleep

#Testando os parametros que serão lidos no servidor web
dire = 1
steps = 1

#Instanciado um objeto da classe movimento
mov = movimento(dire,steps)

if dire == 2:
  mov.oeste()
elif dire == 3:
  mov.leste()
elif dire == 1:
  mov.norte()
else: mov.sul()    

mov.alinhar()

