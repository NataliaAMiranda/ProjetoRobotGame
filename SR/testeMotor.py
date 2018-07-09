import operator
from automatico import  *
from ev3dev.ev3 import * 
from time import sleep

gy = GyroSensor()
#calibrando giroscopio
gy.mode = 'GYRO-CAL'
sleep(5)

def getKey(item):
	return item[0]

def ordenacaca(caca):
	caca.sort(key = operator.itemgetter(0))
	return caca
 
def ordenacaca2(caca):
    lista = []
    for i in range(len(cacas)):
        lista.append([sum(cacas[i]),i]) 
    return lista
  
def atualizalista(cacas, cacasencontradas):
    for i in range(len(cacasencontradas)):
        cacas.remove(cacasencontradas[i])
    return  
    
def reordena(cacas,novalistaordenada):
    lista = []
    for i in range(len(cacas)):
        lista.insert(i,cacas[novalistaordenada[i][1]])
    return  lista

def proxima_caca_amarelo(novalistareord):
    del novalistareord[0]
    if len(novalistareord) != 0:      
        return  novalistareord[0]
    else:
        return -1

def proxima_caca_azul(novalistareord):
    del novalistareord[-1]
    if len(novalistareord) != 0:      
        return  novalistareord[-1]
    else:
        return -1

#cacas = [[2, 3], [1, 7], [3, 4], [0, 1], [7, 2]]
cacas = [[1, 1], [1, 0]]
print('Original: ' + str(cacas))
#cacasencontradas = [[3, 4], [0, 1]]
#atualizalista(cacas, cacasencontradas)
novalista = ordenacaca2(cacas)
print('Lista SOMAS, INDEX: ' + str(novalista))
novalistaordenada = ordenacaca(novalista)
print('Lista SOMA ORDENADA, INDEX: ' + str(novalistaordenada))
print('Lista ORDENADA: ' + str(novalistaordenada))
novalistareord = reordena(cacas,novalistaordenada)
print('Lista RE-ORDENADA: ' + str(novalistareord))
 
# cor 6 - azul
# cor 4 - amarelo

cor_inicial = 4

jogada3 = automatico()
jogada = automatico()

if cor_inicial == 4:
    pos_inicial = [0,0]
    pos_atual = pos_inicial
    cacas_encontradas = 0
    cacas_disp = len(cacas)
    m = 0;
    prox_caca = novalistareord[m]
    jogada.recebeParametros(pos_atual,prox_caca)
    print(pos_atual)
    print(prox_caca)

    jogada.interseccao()
    pos_atual = jogada.info_posicao_atual()

    while(m < len(cacas)):
        jogada3.recebeParametros(pos_atual,prox_caca)
        jogada3.interseccao()
        if (pos_atual == prox_caca):
            print("************** ENCONTROU A CACA:" + str(pos_atual))
            print('Posicao atual: ' + str(pos_atual))
            prox_caca = proxima_caca_amarelo(novalistareord)
            m = m +1
            print("Quantidade de cacas encontradas: " + str(m))
        cacas_disp = len(cacas)

else:
    pos_inicial = [7,7]
    pos_atual = pos_inicial
    cacas_encontradas = 0
    cacas_disp = len(cacas)
    m = 0;
    prox_caca = novalistareord[-1]
    jogada.recebeParametros(pos_atual,prox_caca)
    print(pos_atual)
    print(prox_caca)

    jogada.interseccao()
    pos_atual = jogada.info_posicao_atual()
    while(m < len(cacas)):
        jogada3.recebeParametros(pos_atual, prox_caca)
        jogada3.interseccao()
        if (pos_atual == prox_caca):
            print("************** ENCONTROU A CACA:" + str(pos_atual))
            prox_caca = proxima_caca_azul(novalistareord)
            m = m +1
            print("Quantidade de cacas encontradas: " + str(m))
        cacas_disp = len(cacas)
        print("Cacas disponiveis: " + str(cacas_disp))
    print("Finaliza partida ")
