#!/usr/bin/env python3
import sys
sys.path.append('../')
from movimento import *
from ev3dev.ev3 import *
from time import sleep
import json
import requests


response = requests.get("http://192.168.0.7:5000/oper").text
response = json.loads(response)
print (response)
dire = response['oper'][0]['dir']
steps = response ['oper'][0]['steps']
print (dire)
print(steps)
#novajogada = True
#novojogo = True

mov = movimento(dire,steps)
if dire == 2:
  mov.oeste()
elif dire == 3:
	mov.leste()
elif dire == 1:
  mov.norte()
else: mov.sul()    
mov.alinhar()

