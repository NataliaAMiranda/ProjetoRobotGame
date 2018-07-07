# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 17:20:02 2018

@author: vitor
"""

#from motor import *

class automatico(object):

    def __init__(self, pos,caca):
        self.pos_atual = pos
        self.next_pos= caca


    def norte(self):
  #       mov = motor(1,1)
  #     mov.movimento()
        print('NORTE')

    def sul(self):
  #      mov = motor(4,1)
  #      mov.movimento()
        print('SUL')

    def leste(self):
  #      mov = motor(2,1)
  #     mov.movimento()
        print('LESTE')

    def oeste(self):
  #     mov = motor(2,1)
  #     mov.movimento()
        print('OESTE')

    def anda(self):
        print('PASSO')

    def info_posicao_atual(self):
        return self.pos_atual

    def andarvertical(self, vert):
        if vert > 0:
            self.norte()
            self.anda()
            self.pos_atual[0] =  self.pos_atual[0]+1
            #print('incrementou')
        else:	
            self.sul()
            self.anda()
            self.pos_atual[0] =  self.pos_atual[0]-1
            #print('incrementou')

    def andarhorizontal(self, hori):
        if  hori < 0:
            self.oeste()
            self.anda()
            self.pos_atual[1] =  self.pos_atual[1]-1
            #print('incrementou')
        else:	
            self.leste()
            self.anda()
            self.pos_atual[1] =  self.pos_atual[1]+1
            #print('incrementou')


    def interseccao(self):
        print('--------INTERSECCAO----------')

        vert = self.next_pos[0] - self.pos_atual[0] 
        hori = self.next_pos[1] - self.pos_atual[1]

        if vert != 0:
            self.andarvertical(vert)
        elif hori != 0:
            self.andarhorizontal(hori)

        #print('Posicao: ' + str(self.pos_atual[0]) +','+ str(self.pos_atual[1]))
