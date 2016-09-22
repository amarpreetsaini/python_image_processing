import cv2
import sys

#Import custom functions for image processing
from packages.image_processer import *

#Import custom ui function
from packages.ui import *

print ("Welcome to photo editor")
filename = raw_input('Enter a file name: ')

try:
    f = open('../images/'+filename, "r")
    f.close()
except:
    print("There is no file named", filename)
    sys.exit()

# main function to start image processing

def main():    
    image = cv2.imread('../images/'+filename)
    cv2.imshow('Input image',image)
    cv2.waitKey(0)

    choice = menu()
    if choice == 1:
	    gray_scale(image,filename)
    elif choice == 2:
	    poster(image,filename)
    elif choice == 3:
	    resize(image,filename)
    elif choice == 4:
	    rotate_image(image,filename)
    elif choice == 5:
	    loop = 0

if __name__ == "__main__":
    # execute only if run as a script
    main()

print "Thankyou for using photo editor"
