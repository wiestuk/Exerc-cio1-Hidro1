# -*- coding: utf-8 -*-
"""
@author: wiest
"""

import numpy as np
import matplotlib.pyplot as plt
"""
Apenas a proa, o ombro à vante e a popa geram um sistema de ondas e que o formato da onda é senoidal.
A distância entre os pontos de pressão da proa e do ombro à vante é de 50m 
e a distância entre os pontos de pressão da proa e da popa é de 300m.

a) Para a velocidade de projeto, faça o gráfico (utilizando software) de cada um dos
sistemas de ondas gerados e do sistema resultante. Assuma que a amplitude do
sistema de ondas do ombro à vante é metade da amplitude do sistema da proa e
que a amplitude do sistema de ondas da popa é equivalente a 3/4 da amplitude
do sistema de ondas da proa. Os quatro sistemas de ondas (considerando
também o resultante) devem ser mostrados no mesmo gráfico.

b) Repita a questão a) para uma das possíveis velocidades onde a interferência
entre os sistemas de ondas da proa e popa é destrutiva. Indique a velocidade em
nós e o número de Froude utilizados e verifique se esta velocidade é plausível
para uma embarcação deste porte.
"""

Lpp = 320

LWL = 325.5

Lwl1 = LWL + 200 #Usei para facilitar a visualização dos gráficos
Lwl = LWL + 450



S = 27194 # Área molhada

Desloc = 312622 # m³

Vs = 20 * 0.5144  # m/s <---- nós

"""
proa = a
ombro à vante = b
popa = c
"""
Lab = 50 
Lac = 300

A1 = 1
A2 = A1/2
A3 = A1*3/4

""" Com isso podemos calcular o número de Froude (Fr) e o comprimento de onda (lambda), 
considerando grandes profundidades, dado o tamanho da embarcação.
"""
g = 9.807

Fr  = Vs/np.sqrt(g*LWL)

Lambda  = (Vs**2)*2*np.pi/g

k = 2*np.pi/Lambda


"""
Em seguida defineremos as funções senoidais para a a proa, ombro a vante e popa. 

Proa: Início em CRISTA (+kx +pi/2)
Ombro à vante: Início em CAVA (-k(x-Lab)-pi/2)
Popa: Início em CAVA (-k(x-Lac)-pi/2)

Sistema referencial iniciado na proa
"""

x = np.linspace(0,Lwl1, 500)
xab = np.linspace(Lab,Lwl1,500)
xac = np.linspace(Lac,Lwl1,500)

def OndaProa(x):
    if 0<=x<=Lwl1:
        y = A1*np.sin(k*x+np.pi/2)
        return y
    else:
        return 0

y = [OndaProa(xi) for xi in x]


def OndaOmbro(x):
    if Lab<=x<=Lwl1:
        y = A2*np.sin(-k*(x-Lab)-np.pi/2)
        return y
    else:
        return 0
    
yo = [OndaOmbro(xi) for xi in xab]    
    
def OndaPopa(x):
    if Lac<=x<=Lwl1:
        y = A3*np.sin(-k*(x-Lac)-np.pi/2)
        return y
    else:
        return 0

yp = [OndaPopa(xi) for xi in xac] 

def Resultante(x):
    return OndaProa(x) + OndaOmbro(x) + OndaPopa(x)

yr = [Resultante(xi) for xi in x]

    
plt.figure(figsize=(12,5))
plt.grid(True)
#plt.hlines(0,0,Lwl)
plt.plot(x,y,color = "blue",label = "Proa",linestyle="-.")  
plt.plot(xab,yo,color = "green",label = "Ombro",linestyle="dashed")
plt.plot(xac,yp,color = "red",label = "Popa",linestyle="dotted")
plt.plot(x,yr,color = "black",label = "Resultante",linestyle="solid")
plt.scatter(Lab,-A2,color="green",s=100)
plt.scatter(0,A1,color= "blue",s=100)
plt.scatter(Lac,-A3,color="red",s=100)
#plt.vlines(Lwl-325.5, -1.5, 1.5,)
plt.title("Interferência de projeto")
plt.xlabel("Comprimento")
plt.ylabel("Amplitude")
plt.legend()

"""
Para o segundo caso, como queremos que a interferência de ondas da Popa e Proa seja destrutiva,
temos que alterar a velocidade para que a Proa chegue com uma crista em na posição da Popa.

De tal forma que, 

Lambda = Lps , ou Lambda = Lps/2, ... 

lambda/lps = 1,1/2,1/3,1/4,...
"""  

x = np.linspace(0,Lwl, 500)
xab = np.linspace(Lab,Lwl,500)
xac = np.linspace(Lac,Lwl,500)

Lambda2 = LWL
k2 = 2*np.pi/Lambda2

Vs2 =np.sqrt((Lambda2*g/(2*np.pi)))

Vs2n = Vs2/0.5144

Fr2 = Vs2/np.sqrt(g*LWL)

def OndaProa2(x):
    if 0<=x<=Lwl:
        y = A1*np.sin(k2*x+np.pi/2)
        return y
    else:
        return 
    
y2 = [OndaProa2(xi) for xi in x]
    
def OndaOmbro2(x):
    if Lab<=x<=Lwl:
        y = A2*np.sin(-k2*(x-Lab)-np.pi/2)
        return y
    else:
        return 0
    
yo2 = [OndaOmbro2(xi) for xi in xab]    
    
def OndaPopa2(x):
    if Lac<=x<=Lwl:
        y = A3*np.sin(-k2*(x-Lac)-np.pi/2)
        return y
    else:
        return 0

yp2 = [OndaPopa2(xi) for xi in xac] 

def Resultante2(x):
    return OndaProa2(x) + OndaOmbro2(x) + OndaPopa2(x)

yr2 = [Resultante2(xi) for xi in x]    


plt.figure(figsize=(12,5))
plt.grid(True)
plt.plot(x,y2,color = "blue",label = "Proa",linestyle="-.")
plt.plot(xab,yo2,color = "green",label = "Ombro",linestyle="dashed")
plt.plot(xac,yp2,color = "red",label = "Popa",linestyle="dotted")
plt.plot(x,yr2,color = "black",label = "Resultante",linestyle="solid")
plt.scatter(Lab,-A2,color="green",s=100)
plt.scatter(0,A1,color= "blue",s=100)
plt.scatter(Lac,-A3,color="red",s=100)
plt.title("Interferência destrutiva")
plt.xlabel("Comprimento")
plt.ylabel("Amplitude")
plt.legend() 


print("A velocidade para interferência destrutiva é ",Vs2n,"nós")
print("O número de Froude para a interfêrencia destrutiva é ",Fr2)
    
    
    
    
    
    
    
    