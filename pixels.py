from PIL import Image
import numpy as np

# Abre a imagem com a extensão, e garante que ela se torbe RGB, que significa red, blue, green
im = Image.open('Syngenta.bmp').convert('RGB')

# transformo a imagem em um array do numpy, uma biblioteca muito utilizada para esse tipo de coisa
na = np.array(im)

# essa linha organiza em um array de 3 valores RGB e encontra as cores de cada linha
colours, counts = np.unique(na.reshape(-1,3), axis=0, return_counts=1)

print(colours)
print(counts)

#Resposta: 298 pixels verdes
#site papra conferir: https://convertingcolors.com/rgb-color-255_255_255.html?search=RGB(96,192,0)
# a mensagem eu não consegui descobrir
"""
0 0 0  em rgb = preto = 125236
96 192 0 = verde que usaram ali = 298 
255 255 255 = branco = 466

PS: A mensagem seria me contrate?
"""