#!/usr/bin/env python
# coding: utf-8

# # LINHA - COLUNA - CANAL

# ##### IMPORTS

# In[1]:


import cv2
import numpy as np
import os


# ##### CONSTANTES

# In[2]:


gblur = 0  ### 1 para gaussiano e 0 para box blur
totalBlurs = 7
boxToGaussian = 2
jSize = 15    ### tamanho da janela (quadrada)
batata = 10


# ###### Tratamento da imagem

# In[3]:


def criaImagemNova(y, x, c):
    return np.empty((y, x, c))


# ##### Fontes de luz

# In[4]:


def separaLuz(img, newImg):
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            somaCanais = 0
            for c in range(img.shape[2]):
                somaCanais += img[y][x][c]
            for c in range(img.shape[2]):
                if somaCanais < 390:
                    newImg[y][x][c] = 0
                else:
                    newImg[y][x][c] = img[y][x][c]


# ##### Borra luz

# In[5]:


def borraLuz(img, newImg):
    for i in range(totalBlurs):
        incremento = 0 if (i+1)%2 == 1 else 1
        if gblur == 1:
            janela = jSize*(i+1)+incremento
            newImg += cv2.GaussianBlur(img, (janela, janela), 0)
        else:
            for j in range(boxToGaussian):
                janela = jSize*(i+1)+incremento - 6*i
                newImg += cv2.blur(img, (janela, janela))


# ##### Soma imagens

# In[6]:


def somaImagensPonderada(img, mascara):
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            for c in range(img.shape[2]):
                img[y][x][c] = 0.9*img[y][x][c] + 0.1*mascara[y][x][c]


# ##### Bloom filter

# In[7]:


def bloom(img):
    luzes = criaImagemNova(img.shape[0], img.shape[1], img.shape[2])
    separaLuz(img, luzes)
    print('1')
    luzBorrada = criaImagemNova(img.shape[0], img.shape[1], img.shape[2])
    borraLuz(luzes, luzBorrada)
    cv2.imwrite('luzBorrada0.bmp', luzBorrada)
    print('2')
    somaImagensPonderada(img, luzBorrada)
    cv2.imwrite('bloom0.bmp', img)
    print('3')


# # Main

# In[8]:


img = cv2.imread('GT2.bmp', 1)
img = img.astype (np.float32)

bloom(img)

