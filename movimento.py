#/usr/bin/python3

from ev3dev.ev3 import *
from time import sleep

class movimento(object):

  def __init__(self, direcao, passos):
    self.dir = direcao
    self.steps = passos
    self.gy= GyroSensor()
    self.ts = TouchSensor()
    self.mA = LargeMotor('outA')
    self.mD = LargeMotor('outD')
    assert self.gy.connected
    self.gy.mode = 'GYRO-ANG'
    self.units = self.gy.units  
  
  def norte(self):
    self.andar()
    
  def oeste(self):
    while not self.ts.value():
      angle = self.gy.value()
      print(str(angle) + " " + self.units)
      self.mA.run_timed(time_sp = 500, speed_sp = 80)
      #self.mA.run-to-abs-pos(posicion_sp = 90)
      if angle >= 85:
        self.mA.stop(stop_action = "brake")
        break
      sleep(0.25)
      self.andar()
      self.alinhar(2)
    
  def sul(self):
    while not self.ts.value():
      angle = self.gy.value()
      print(str(angle) + " " + self.units)
      self.mA.run_timed(time_sp = 500, speed_sp = 80)
      #self.mA.run-to-abs-pos(posicion_sp = 180)
      if angle >= 174:
        self.mA.stop(stop_action = "brake")
        break
      sleep(0.25)
      self.andar()
      self.alinhar(3)
    
  def leste(self):
    while not self.ts.value():
      print("Virou para o leste")
      angle = self.gy.value()
      print(str(angle) + " " + self.units)
      self.mD.run_timed(time_sp = 500, speed_sp = 80)
      #self.mD.run-to-abs-pos(posicion_sp = 90)
      if angle <= -85:
        self.mD.stop(stop_action = "brake")
        break
      self.andar()
      self.alinhar(4)
         
  def andar(self):
    for x in range(0, self.steps):
      print ("1 passo")
      self.mA.run_timed(time_sp = 2000, speed_sp = 200)
      self.mD.run_timed(time_sp = 2000, speed_sp = 200)
      sleep(2)
    
  def alinhar(self):
    if self.dir == 2:
      while not self.ts.value():
        print("Virou para o leste")
        angle = self.gy.value()
        print(str(angle) + " " + self.units)
        #self.mD.run-to-abs-pos(posicion_sp = 90)
        self.mD.run_timed(time_sp = 500, speed_sp = 80)
        if angle <= 1:
          self.mD.stop(stop_action = "brake")
          break
    elif self.dir == 4:
      while not self.ts.value():
        angle = self.gy.value()
        print(str(angle) + " " + self.units)
        #self.mA.run-to-abs-pos(posicion_sp = 90)
        self.mA.run_timed(time_sp = 500, speed_sp = 80)
        if angle >= 360:
          self.mA.stop(stop_action = "brake")
          break
    elif self.dir ==3:
      while not self.ts.value():
        angle = self.gy.value()
        print(str(angle) + " " + self.units)
        #self.mA.run-to-abs-pos(posicion_sp = 180)
        self.mA.run_timed(time_sp = 500, speed_sp = 80)
        if angle >= -1:
          self.mA.stop(stop_action = "brake")
          break
    else: 
        pass
