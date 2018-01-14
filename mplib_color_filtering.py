#image tutorial from matplotlib
#https://matplotlib.org/users/image_tutorial.html#plotting-numpy-arrays-as-images
'''
This allows you filter the undesired colors from an image by the plt.imshow
function, with the clim arguement allowing for the filtering.
the plt.hist function allows for viewing the colors in the image as a histogram.
-could use something like a waitkey to be able to show multiple images if they
exist.
- time.sleep() is one option
- the script must be run in the file path of the images (ex using atom)
'''
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob2
#import time

def mplib_color_filtering(files):
    for f in files:
        img = mpimg.imread(f)
        lum_img = img[:,:,0]
        imgplot = plt.imshow(lum_img, clim=(0,60)) #clim adjusted from 255 to 60
        imgplot.set_cmap('nipy_spectral')
        plt.colorbar()
        #plt.hist(lum_img.flatten(), 256, range=(0.0,255), fc = 'k', ec = 'k')
        plt.show()
        #plt.waitforbuttonpress()
        #time.sleep(1)
        #plt.destroy() #find a similar method

mplib_color_filtering(glob2.glob('*.jpg'))
