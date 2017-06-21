import numpy as np
import cv2
from matplotlib import pyplot as plt

# img = None
# for f in files:

img = cv2.imread('1.jpg',0)


def onclick(event):
    if event.dblclick:
    	#write data for image cordinates
    	f = open("earPointData.txt", "a");
    	f.write( 'x:'+str(event.xdata) + ',y:' + str(event.ydata) + "\n"  )
    	f.close();
    	#showing the data on click event
    	print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
        	  (event.button, event.x, event.y, event.xdata, event.ydata))
    	
    	

cid = plt.connect('button_press_event', onclick)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

plt.show();

