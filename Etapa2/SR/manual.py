#from ev3dev.ev3 import *
from time import sleep

class manual(object):

  def __init__(self, direcao, passos):
    self.dire = direcao
    self.steps = passos
    self.gy= GyroSensor()
    self.ts = TouchSensor()
    self.mA = LargeMotor('outA')
    self.mD = LargeMotor('outD')
    assert self.gy.connected
    self.gy.mode = 'GYRO-ANG'
    self.units = self.gy.units

  def movimento(self):
    if self.dire == 2:
     self.oeste()
     self.andar()
     self.alinhar()
    elif self.dire == 6:
     self.mA.run_timed(time_sp = 200, speed_sp = 100)
    elif self.dire == 7:
     self.mD.run_timed(time_sp = 200, speed_sp = 100)
    elif self.dire == 3:
     self.leste()
     self.andar()
     self.alinhar()
    elif self.dire == 1:
     self.andar()
     self.alinhar()
    else: 
     self.sul()

  def oeste(self):
    while not self.ts.value():
      angle = self.gy.value()
      print(str(angle) + " " + self.units)
      self.mA.run_timed(time_sp = 300, speed_sp = 100)
      if angle >= 90:
        self.mA.stop(stop_action = "brake")
        break

  def leste(self):
    while not self.ts.value():
      angle = self.gy.value()
      print(str(angle) + " " + self.units)
      self.mA.run_timed(time_sp = 300, speed_sp = -120)
      if angle <= -90:
        self.mA.stop(stop_action = "brake")
        break

  def sul(self):
    for x in range(0, self.steps):
      print ("1 passo")
      self.mA.run_timed(time_sp = 1000, speed_sp = -400)
      self.mD.run_timed(time_sp = 1000, speed_sp = -400)
      sleep(1)

  def andar(self):
    for x in range(0, self.steps):
      print ("1 passo")
      self.mA.run_timed(time_sp = 1000, speed_sp = 400)
      self.mD.run_timed(time_sp = 1000, speed_sp = 400)
      sleep(1)

  def alinhar(self):
    print("alinhando")
    if self.dire == 2:
      while not self.ts.value():
        angle = self.gy.value()
        print(str(angle) + " " + self.units)
        self.mD.run_timed(time_sp = 500, speed_sp = 120)
        if angle <= 1:
          self.mD.stop(stop_action = "brake")
          break
    elif self.dire == 3:
      while not self.ts.value():
        angle = self.gy.value()
        print(str(angle) + " " + self.units)
        self.mA.run_timed(time_sp = 500, speed_sp = 120)
        if angle >= -1:
          self.mA.stop(stop_action = "brake")
          break
    else:
      pass
