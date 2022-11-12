'''
Detection of image with displaying name of the image

Code contributed by Rupesh Phanindra Sai Ande

To reach me... Check the code...

Happy Learning

'''

import numpy as np
import cv2
# Load an colour image in grayscale

print("""
Code written by : Rupesh Phanindra Sai Ande
Mail id  : rupeshphani.5@gmail.com
LinkedIn : https://www.linkedin.com/in/rupesh-ande
Instagram: rupesh_ande
      """)

img=cv2.imread('/Users/rupeshande/Downloads/Image_detection+Name/keerty.jpg')
output=img.copy()
#Adding the text using putText() function
text=cv2.putText(output,'keerthy',(10,60),cv2.FONT_HERSHEY_SIMPLEX,3,(255,0,0),6)
cv2.imshow('image',output)
cv2.waitKey(0)
cv2.destroyAllWindows()





