#!/usr/bin/env python
# coding: utf-8

# # LINHA - COLUNA - CANAL

# ###### IMPORTS

# In[1]:


import cv2
import numpy as np
import os
from datetime import datetime
from dateutil import relativedelta


# ###### CONSTANTES

# In[2]:


jx = 5    ### eixo x da janela
jy = 5    ### eixo y da janela
canal = 1 ### colorido = 1 / escala de cinza = 0


# ###### Tratamento da imagem

# In[3]:


##def trataImagem(img):
    ## Tratar canais

def criaImagemNova(y, x, c):
    return np.empty((y, x, c))


# ######  Valida se pixels e extremos das janelas estão dentro da imagem

# In[4]:


def pixelValido(y, x, maxY, maxX):
    return y > 0 and x > 0 and y < maxY and x < maxX

def janelaValida(y, x, maxY, maxX, janelaY, janelaX):
    return (pixelValido((y+janelaY/2), (x+janelaX/2), maxY, maxX) and
            pixelValido((y-janelaY/2), (x-janelaX/2), maxY, maxX) and
            pixelValido((y+janelaY/2), (x-janelaX/2), maxY, maxX) and
            pixelValido((y-janelaY/2), (x+janelaX/2), maxY, maxX))


# ######   Função genérica para percorrer a imagem dada

# In[5]:


def percorrerImg(img, newImg, func):
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            for c in range(img.shape[2]):
                func(img, newImg, y, x, c)


# ######  Algoritmo ingênuo

# In[6]:


def calculaPixelIngenuo(img, newImg, y, x, c):
    if janelaValida(y, x, img.shape[0], img.shape[1], jy, jx):
        soma = 0
        for lin in range(-(jy//2), jy//2+1):
            for col in range(-(jx//2), jx//2+1):
                soma += img[y+lin][x+col][c]
        newImg[y][x][c] = soma/(jx*jy)
    else:
        newImg[y][x][c] = img[y][x][c]

def ingenuo(img):
    ##trataImagem(img)
    newImg = criaImagemNova(img.shape[0], img.shape[1], img.shape[2])
    percorrerImg(img, newImg, calculaPixelIngenuo)
    cv2.imwrite('ingenuo.bmp', newImg)


# ######  Algoritmo separável

# In[7]:


def calculaPixelSeparavelY(img, newImg, y, x, c):
    if janelaValida(y, x, img.shape[0], img.shape[1], jy, 0):
        soma = 0
        for lin in range(-(jy//2), jy//2+1):
            soma += img[y+lin][x][c]
        newImg[y][x][c] = soma/(jy)
    else:
        newImg[y][x][c] = img[y][x][c]
        
def calculaPixelSeparavelX(img, newImg, y, x, c):
    if janelaValida(y, x, img.shape[0], img.shape[1], 0, jx):
        soma = 0
        for col in range(-(jx//2), jx//2+1):
            soma += img[y][x+col][c]
        newImg[y][x][c] = soma/(jx)
    else:
        newImg[y][x][c] = img[y][x][c]

def separavel(img):
    ##trataImagem(img)
    newImg = criaImagemNova(img.shape[0], img.shape[1], img.shape[2])
    percorrerImg(img, newImg, calculaPixelSeparavelY)
    percorrerImg(newImg, img, calculaPixelSeparavelX)
    cv2.imwrite('separavel.bmp', img)


# ##### Imagem integral

# In[8]:


def criaImagemIntegralY(img, newImg, y, x, c):
    if y != 0:
        newImg[y][x][c] = newImg[y-1][x][c] + img[y][x][c]
        
def criaImagemIntegralX(img, newImg, y, x, c):
    if x != 0:
        newImg[y][x][c] = newImg[y][x-1][c] + img[y][x][c]
        
def calculaPixelIntegral(img, newImg, y, x, c):
    minX = x - (jx//2) -1
    minY = y - (jy//2) -1
    maxX = x + (jx//2)
    maxY = y + (jx//2)
    if janelaValida(y, x, img.shape[0], img.shape[1], jy+1, jx+1):
        soma = img[maxY][maxX][c]
        soma += img[minY][minX][c]
        soma -= img[maxY][minX][c]
        soma -= img[minY][maxX][c]
        newImg[y][x][c] = soma/(jx*jy)

def integral(img):
    ##trataImagem(img)
    newImg = criaImagemNova(img.shape[0], img.shape[1], img.shape[2])
    percorrerImg(img, newImg, criaImagemIntegralY)
    aux = criaImagemNova(img.shape[0], img.shape[1], img.shape[2])
    percorrerImg(newImg, aux, criaImagemIntegralX)
    percorrerImg(aux, img, calculaPixelIntegral)
    cv2.imwrite('integral.bmp', img)


# ##### Remove os arquivos caso existam

# In[9]:


def apagaArquivosExistentes():
    if os.path.isfile('ingenuo.bmp'):
        os.remove('ingenuo.bmp')
    if os.path.isfile('separavel.bmp'):
        os.remove('separavel.bmp')
    if os.path.isfile('integral.bmp'):
        os.remove('integral.bmp')


# ##### Chama todas as funções de filtro da média

# In[10]:


apagaArquivosExistentes()

img = cv2.imread('arroz.bmp', 1)

init = datetime.now()
ingenuo(img)
end = datetime.now()
print("Ingenuo: ")
print(relativedelta.relativedelta(end, init))

init = datetime.now()
separavel(img)
end = datetime.now()
print("Separavel: ")
print(relativedelta.relativedelta(end, init))

init = datetime.now()
integral(img)
end = datetime.now()
print("Integral: ")
print(relativedelta.relativedelta(end, init))

