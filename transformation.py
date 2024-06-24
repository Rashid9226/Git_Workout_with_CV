import cv2
import matplotlib.pyplot as plt
import numpy as np

"""Affine transformation
An affine transformation matrix(say 2*3) for 2D transformations is of the form:
[[a,b,tx],[c,d,ty]]
if a=10,b=25 and tx=100 then :
    a=10: This value will scale the x-coordinates of the image by a factor of 10.
    This means the image will be stretched horizontally by a factor of 10.
    -Makes the image 10 times wider (horizontal stretch).
    
    
    b=25: This value introduces a shear effect in the x-direction. Each pixel's 
    x-coordinate will be affected by its y-coordinate scaled by 25, creating a skewed effect.
    -Tilts (skews) the image, making it slant horizontally based on its vertical position.
    
    tx=100: This translates the image 100 pixels to the right.

also if c=30,d=50,ty=100 means
    c = 30: Tilts (skews,shear) the image, making it slant vertically based on its horizontal position.
    d = 50: Makes the image 50 times taller (vertical stretch).
    ty = 100: Moves the image 100 pixels down.
    
Horizontal Stretching and Skewing: The image gets wider and tilts based on its height.
Vertical Stretching and Skewing: The image gets taller and tilts based on its width.
Translation: The entire image moves to the right and down.
    """


def show(img,title,p):
    img_rgb = img[:, :, ::-1]
    ax = plt.subplot(2,2, p)
    plt.title(title)
    plt.imshow(img_rgb)
    plt.axis()

img=cv2.imread("ace.png")

height,width= img.shape[:2]
M1 =np.float32([[1,0.1,-100],[0.2,1,-50]])
"""image is not stretched but tilted in both horizontally and vertically and from x axis
 -100 moved and from y axis-50 moved which means they have transformed from the end of
both x and y axis of the image
"""
dst_img1 = cv2.warpAffine(img,M1,(width,height))
M2 =np.float32([[1.6,0,0],[0,1,0]])
dst_img2 = cv2.warpAffine(img,M2,(width,height))

"""
Affine Transformation Matrix: This matrix is a combination of translation, rotation, scaling, and
shearing. Even a slight change in the points used to compute the matrix can cause these combined 
transformations to behave differently.
"""

pts_1 = np.float32([[0,0],[100,0],[50,60]])
pts_2 = np.float32([[20,0],[150,0],[60,80]])
M = cv2.getAffineTransform(pts_1,pts_2)
# print(M)
aff_img =cv2.warpAffine(img,M,(width,height))

show(img,"Original",1)
show(dst_img1,'titled image',2)
show(dst_img2,'Stretched Image',3)
show(aff_img,'Affine Image',4)

plt.show()