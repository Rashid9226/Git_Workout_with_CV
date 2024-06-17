import cv2
import matplotlib.pyplot as plt
import numpy as np

def show(img,title,pos):
    img_rgb=img[:, :, ::-1]
    ax=plt.subplot(1,3,pos)
    plt.title(title)
    plt.imshow(img_rgb)
    plt.axis()

img=cv2.imread('ace.png')
height,width=img.shape[:2]
ace=img[64:654,468:814]
luffy=img[100:636,61:464]
show(img,"original",1)
show(ace,"Ace",3)
show(luffy,"Luffy",2)
plt.show()