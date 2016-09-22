import cv2
import numpy as np

def gray_scale(image,filename):
    gray_image = cv2.cvtColor( image, cv2.COLOR_RGB2GRAY )
    new_name = 'gray_'+filename
    cv2.imwrite('../processed_images/'+new_name,gray_image)
    print("Image converted to gray scale")
    image = cv2.imread('../processed_images/'+new_name)
    cv2.imshow('Input image',image)
    cv2.waitKey(0)

def poster(image,filename):
    image[image >= 128]= 255
    image[image < 128] = 0
    new_name = 'poster_'+filename
    cv2.imwrite('../processed_images/'+new_name,image)
    print("Image converted to Posterized")
    image = cv2.imread('../processed_images/'+new_name)
    cv2.imshow('Input image',image)
    cv2.waitKey(0)

def resize(image,filename):
    width = input('Enter new width: ')
    height = input('Enter new height: ')
    resized_image = cv2.resize(image, (width, height)) 
    new_name = 'resized_'+filename
    cv2.imwrite('../processed_images/'+new_name,resized_image)
    print("Image resized to new size")
    image = cv2.imread('../processed_images/'+new_name)
    cv2.imshow('Input image',image)
    cv2.waitKey(0)

def rotate_image(image,filename):
    angle = input('Enter the angle: ')
    image_center = tuple(np.array(image.shape[0:2])/2)
    rot_mat = cv2.getRotationMatrix2D(image_center,angle,1.0)
    rotated_image = cv2.warpAffine(image, rot_mat, image.shape[0:2],flags=cv2.INTER_LINEAR)
    new_name = 'rotated_'+filename
    cv2.imwrite('../processed_images/'+new_name,rotated_image)
    print("Image rotated to new angle")
    image = cv2.imread('../processed_images/'+new_name)
    cv2.imshow('Input image',image)
    cv2.waitKey(0)

