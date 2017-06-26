import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib.patches import Circle
import os

#----------------------------------
# Loading all images from folder
#----------------------------------
imageFolder = './train_3_last'
resultFile = "result.txt"
images = []
imageName = []
    
def load_images_from_folder(folder):
    for filename in sorted(os.listdir(folder)):
        # img = cv2.imread(os.path.join(folder,filename))
        # if img is not None:
        #     images.append(img)
        imageName.append(filename)
        print filename
    return imageName


data_images = load_images_from_folder(imageFolder);
print(data_images);
print  len(data_images)
# Global index value of image current postion.
index = 0
imagecordinate =[];    

#----------------------------------
# On Click event listner for capturing coordinates in image
# On double tap will get points
#----------------------------------

def onclick(event):
    if event.dblclick:
        if event.button == 1:
            if len(imagecordinate) == 0:
                imagecordinate.append(data_images[index]);    
            imagecordinate.append(event.xdata);
            imagecordinate.append(event.ydata);
            #cv2.circle(img, (int(event.xdata),int(event.ydata)), 2, (255,255,0), 25)
            #cv2.circle(img, (int(event.xdata),int(event.ydata)), 2, (255,0,0), 5)
            #circ = Circle((int(event.xdata),int(event.ydata)),10)
            #plt.add_patch(circ)
            plt.scatter([10], [20])
            plt.scatter(x=[30, 40], y=[50, 60], c='r', s=40)
            plt.show()
            #write data for image cordinates
            if len(imagecordinate) == 5:
                f = open(resultFile, "a");
                #f.write( 'x:'+str(event.xdata) + ',y:' + str(event.ydata) + "\n"  )
                f.write( str(imagecordinate) + "\n"  )
                f.close();
                imagecordinate[:] = [];
            #showing the data on click event
            print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
              (event.button, event.x, event.y, event.xdata, event.ydata));  
        
    else:
        print(event)            
        
cid = plt.connect('button_press_event', onclick)

#----------------------------------
# On key press event listner for capturing keyboard actions
# On right arrow -> next image is shown
# On left arrow -> previous image is shown 
#----------------------------------

def on_key(event):
    if event.key == "right":
        global index

        index += 1
        print index
        if index < len(data_images):
            img=[];
            img = cv2.imread(os.path.join(imageFolder,data_images[index]))
            if img is not None:
                print img
                plt.imshow(img)
                plt.draw()
        else:        
            plt.close()
    
    if event.key == "left":
        index -= 1

        if index > -1:
            plt.imshow(data_images[index])
            plt.draw()
        else:        
            plt.close()
            # index = len(data_images) -1
            # print index
            # plt.imshow(data_images[index])
            # plt.draw()
    
pid = plt.connect('key_press_event', on_key)

img = cv2.imread(os.path.join(imageFolder,data_images[index]))
if img is not None:
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show();

