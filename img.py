import numpy as np
import cv2
from matplotlib import pyplot as plt
import os

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

# img = None
# for f in files:

data_images = load_images_from_folder('.');
print(data_images);
#img = cv2.imread('1.jpg',0)
#----------------------------------

index = 0

# def toggle_images(event):
#     global index

#     index += 1

#     if index < len(data_images):
#         plt.imshow(data_images[index])
#         plt.draw()
#     else:        
#         plt.close()

#----------------------------------


def onclick(event):
    if event.dblclick:
    	if event.button == 1:
	    	#write data for image cordinates
	    	f = open("earPointData.txt", "a");
	    	f.write( 'x:'+str(event.xdata) + ',y:' + str(event.ydata) + "\n"  )
	    	f.close();
	    	#showing the data on click event
	    	print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
        	  (event.button, event.x, event.y, event.xdata, event.ydata));	
    else:
		print(event)    		
    	
        
cid = plt.connect('button_press_event', onclick)

plt.imshow(data_images[index])

#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

plt.show();

