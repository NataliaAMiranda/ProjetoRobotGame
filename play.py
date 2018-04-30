from movimento import *
from ev3dev.ev3 import *
from time import sleep
import json
import requests


response = requests.get("http://localhost:5000/oper").text
response = json.loads(response)
dire = response['oper'][0]['dir']
steps = response ['oper'][0]['steps']
novajogada = response['oper'][0]['novajogada']
novojogo = response['oper'][0]['novojogo']

while (novojogo == True):
 response = requests.get("http://localhost:5000/oper").text
 response = json.loads(response)
 dire = response['oper'][0]['dir']
 steps = response ['oper'][0]['steps']
 novajogada = response['oper'][0]['novajogada']
 novojogo = response['oper'][0]['novojogo']
 if novajogada == True:
  mov = movimento(dire,steps)
  if dire == 2:
   mov.oeste()
   mov.andar()
  elif dire == 3:
   mov.leste()
   mov.andar()
  elif dire == 1:
   mov.norte()
  else:
   mov.sul()
   mov.andar()
  mov.alinhar()
  response = requests.get("http://localhost:5000/finalizajogada").text
 else:
  pass

