import glob2
import cv2

def batch_image_resizing(folder):
    for i in folder: # i is the individual image file name taken from a list
        img = cv2.imread(i,0)
        resized_img = cv2.resize(img,(500,500))
        cv2.imshow('Image',resized_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        #the below write command will work only if the script is run in the file
        #path of the images
        cv2.imwrite('new_' + i,resized_img)


#batch_image_resizing(glob2.glob('C:/Users/Toni Kristo/Desktop/Python/Udemy/Batch Image Resizing/Sample Images/*.jpg'))
batch_image_resizing(glob2.glob('*.jpg'))
