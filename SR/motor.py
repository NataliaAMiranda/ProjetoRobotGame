from ev3dev.ev3 import * 
from time import sleep

class motor(object):

  def __init__(self):
    self.gy= GyroSensor()
    self.cor = ColorSensor()
    self.cs = ColorSensor()
    self.ts = TouchSensor()
    self.mA = LargeMotor('outA')
    self.mC = LargeMotor('outC')
    assert self.gy.connected
    assert self.cor.connected
    assert self.cs.connected
    assert self.ts.connected
    assert self.ts.connected
    assert self.mA.connected
    assert self.mC.connected
    self.cor.mode='COL-COLOR'
    self.anguloRef = 0
    self.gy.mode = 'GYRO-ANG'
    self.units = self.gy.units    
    self.angleL = 0
    
  def movimento(self, direcao, passos):
    self.dire = direcao
    self.steps = passos
    if self.dire == 3:
     print("virando oeste..........")
     self.oeste()
     self.andar()
     self.alinhar()
    elif self.dire == 6:
     self.mA.run_timed(time_sp = 200, speed_sp = 100) 
    elif self.dire == 7:
     self.mC.run_timed(time_sp = 200, speed_sp = 100)
    elif self.dire == 2:
     print("virando leste..........")
     self.leste()
     self.andar()
     self.alinhar()
    elif self.dire == 1:
     print("andando norte..........")
     self.andar()
    else: 
     print("virando sul..........")
     self.sul()
     self.andar()
     self.alinhar()
    
  def oeste(self):
    while not self.ts.value():
      angle = self.gy.value()
      self.mA.run_timed(time_sp = 100, speed_sp = -100)
      n = self.cor.value()
      if angle < -1: 
        if n == 1:
          self.mA.stop()
          self.mC.stop()
          print("Preto " + str(n))
          sleep(0.5)
          break

  def leste(self):
    while not self.ts.value():
      self.angleL = self.gy.value()
      self.mA.run_timed(time_sp = 100, speed_sp = 100)
      n = self.cor.value()
      if self.angleL > 30:
        if n == 1:
          self.mA.stop()
          self.mC.stop()
          print("Preto " + str(n))
          sleep(0.5)
          break
        
        
  def sul(self):
    while not self.ts.value():
      self.mC.run_timed(time_sp = 500, speed_sp = -100)
      self.mA.run_timed(time_sp = 500, speed_sp = -100)
      n = self.cor.value()
      if n == 1:
        self.mA.stop()
        self.mC.stop()
        print("Preto " + str(n))
        sleep(0.5)
        break
        
         
  def andar(self):
    n = self.cor.value()
    if n == 3 or n == 4:
      self.mC.run_timed(time_sp = 500, speed_sp = 250)
      self.mA.run_timed(time_sp = 500, speed_sp = 250)
    sleep(2)
    x = 0
    while not self.ts.value() or (x != self.steps):
      n = self.cor.value()
      angle = self.gy.value()
      if self.dire == 4:  
        self.mA.run_timed(time_sp = 100, speed_sp = 100)
        self.mC.run_timed(time_sp = 100, speed_sp = 100)
        if n == 3:
          print("Verde anda " + str(n))
          x = 1
          print("1 passo")
          break
        elif n == 4:
          print("Amarelo anda " + str(n))
          x = 1
          posi = (1,1)
          print("1 passo")
          break
        elif n == 2:
          print("Azul anda " + str(n))
          x = 1
          posi = (7,7)
          print("1 passo")
          break
        elif n == 6:
          if angle >= 100:
            self.viraEsquerda()
          else:
            self.viraDireita()          
      else:
          self.mA.run_timed(time_sp = 100, speed_sp = 100)
          self.mC.run_timed(time_sp = 100, speed_sp = 100)
          if n == 3:
            x = 1
            print("1 passo")
            break
          elif n == 4:
            x = 1
            posi = (1,1)
            print("1 passo")
            break
          elif n == 2:
            x = 1
            posi = (7,7)
            print("1 passo")
            break
          elif n == 6:
            if self.dire == 1 and angle != 0:
              if angle > self.anguloRef:
                self.viraEsquerda()
              else:
                self.viraDireita()
            elif self.dire == 3 and angle != 0:
              if angle <= -1:
                self.viraEsquerda()
              else:
                self.viraDireita()
            elif self.dire == 2 and angle != 0:
              if angle >= 1:
                self.viraEsquerda()
              else:
               self.viraDireita()
    self.mC.stop()
    self.mA.stop()
    sleep(2)

  def viraEsquerda(self):
    aux = 0
    n = self.cor.value()
    while n != 1:
      self.mA.stop(stop_action = "brake")
      self.mC.run_timed(time_sp = 100, speed_sp = 150)
      n = self.cor.value()
      sleep(0.5)
      if n == 3:
        self.mC.run_timed(time_sp = 200, speed_sp = 100)
        self.mA.run_timed(time_sp = 200, speed_sp = 100)
        sleep(0.5)
        break
            
  def viraDireita(self):
    aux = 0
    n = self.cor.value()
    while n != 1:
      self.mC.stop(stop_action = "brake")
      self.mA.run_timed(time_sp = 100, speed_sp = 150)
      n = self.cor.value()
      print(n)
      sleep(0.5)
      if n == 3:
        self.mC.run_timed(time_sp = 200, speed_sp = 100)
        self.mA.run_timed(time_sp = 200, speed_sp = 100)
        sleep(0.5)
        break
  
  def alinhar(self):
    print("alinhando")
    if self.dire == 4:
      sleep(2)
      while not self.ts.value():
        angle = self.gy.value()
        self.mC.run_timed(time_sp = 500, speed_sp = 120)
        if angle == 0:
          self.mC.stop(stop_action = "brake")
          break
    elif self.dire == 2:
      while not self.ts.value():
        angle = self.gy.value()
        self.mC.run_timed(time_sp = 500, speed_sp = 120)
        if angle == 0:
          self.mC.stop(stop_action = "brake")
          break
    elif self.dire == 3:
      while not self.ts.value():
        angle = self.gy.value()
        self.mC.run_timed(time_sp = 500, speed_sp = -120)
        if angle == 0:
          self.mA.stop(stop_action = "brake")
          break
    else: 
      pass
