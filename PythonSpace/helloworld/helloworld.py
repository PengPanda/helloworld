import cv2
import numpy as np
import matplotlib as plt

print 'hello world!'
print 'my name is', 'PengPanda', '!'
# myname = raw_input()
# print myname

a = 100
if a >= 0:
    print a
else:
    print -a

b = True
print b
b = 123
print b

img = cv2.imread('E:\\workspace\\PythonSpace\\helloworld\\rg.bmp')
cv2.imshow('Image', img)
cv2.waitKey(1000)
# cv2.destroyAllWindows()

myimg = img.copy()
cv2.imshow('myimage', myimg)
cv2.waitKey(1000)

emptyImage = np.zeros(img.shape, np.uint8)
cv2.imshow('emptyImage', emptyImage)
cv2.waitKey(1000)

cv2.destroyAllWindows()


