### image processing codes python 

# import statement blocks 

import matplotlib.pyplot as plt

from scipy import misc,ndimage

face = misc.face()#to create face array

#Use different gaussian kernels for smoothing
blurred_face = ndimage.gaussian_filter(face, sigma=3)
very_blurred = ndimage.gaussian_filter(face, sigma=15)#Results

#to draw image
plt.imshow(very_blurred)

#to show image 
plt.show()
