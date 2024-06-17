import cv2
import matplotlib.pyplot as plt

def show(img,title,pos):
    img_rgb=img[:, :, ::-1]
    ax=plt.subplot(2,2,pos)
    plt.imshow(img_rgb)
    plt.title(title)
    plt.axis()
img=cv2.imread("ace.png")
height,width=img.shape[:2]
m180=cv2.getRotationMatrix2D((width/2.0,height/2.0),180,1)
m90=cv2.getRotationMatrix2D((width/2.0,height/2.0),90,1.26)
m270=cv2.getRotationMatrix2D((width/2.0,height/2.0),270,1.26)
image180=cv2.warpAffine(img,m180,(width,height))
image270=cv2.warpAffine(img,m270,(width,height))
image90=cv2.warpAffine(img,m90,(width,height))


show(img,"image",1)
show(image270,"rotated Right with perfect fit in frame",2)
show(image90,'Rotated left',3)
show(image180,"Upward image",4)

plt.show()
