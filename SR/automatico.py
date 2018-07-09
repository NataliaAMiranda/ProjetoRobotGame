from motor import *

class automatico(object):

    def __init__(self):
        self.mov = motor()

    def recebeParametros(self, pos, caca):
        self.pos_atual = pos
        self.next_pos = caca
        
    def norte(self):
        self.mov.movimento(1,1)
        print('NORTE')

    def sul(self):
        self.mov.movimento(4,1)
        print('SUL')

    def leste(self):
        self.mov.movimento(2,1)
        print('LESTE')

    def oeste(self):
        self.mov.movimento(3,1)
        print('OESTE')

    def info_posicao_atual(self):
        return self.pos_atual

    def andarvertical(self, vert):
        if vert > 0:
            self.leste()
            self.pos_atual[0] =  self.pos_atual[0]+1
            #print('incrementou')
        else:	
            self.oeste()
            self.pos_atual[0] =  self.pos_atual[0]-1
            #print('incrementou')

    def andarhorizontal(self, hori):
        if  hori < 0:
            self.sul()
            self.pos_atual[1] =  self.pos_atual[1]-1            
            #print('incrementou')
        else:	
            self.norte()
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

        print('Posicao: ' + str(self.pos_atual[0]) +','+ str(self.pos_atual[1]))
