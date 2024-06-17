import cv2
import matplotlib.pyplot as plt

def show(img,title,pos):
    img_rgb = img[:, :, ::-1]
    ax = plt.subplot(2, 2, pos)
    plt.imshow(img_rgb)
    plt.title(title)
    plt.axis()
    # plt.show()

img=cv2.imread('ace.png')
height,width=img.shape[:2]

res_img=cv2.resize(img,(width*2,height*2),interpolation=cv2.INTER_LINEAR)
res_img1=cv2.resize(img,(width*5,height*5),interpolation=cv2.INTER_AREA)
res_img2=cv2.resize(img,None,fx=1.5,fy=1)

show(img,"Original",1)
show(res_img,"resized",2)
show(res_img1,"resized",3)
show(res_img2,"resized",4)
plt.show()
