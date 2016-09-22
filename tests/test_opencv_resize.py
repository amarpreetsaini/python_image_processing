import unittest
import cv2
from PIL import Image

class TestResize(unittest.TestCase):
        	
    def test_resize(self):
	image = cv2.imread('../images/cat.jpeg')
	resized_image = cv2.resize(image, (100, 100)) 
	cv2.imwrite('../processed_images/test_cat.jpeg',resized_image)
	new_name = 'test_cat.jpeg'
	filename = '../processed_images/'+new_name
	with Image.open(filename) as im:
	    new_width, new_height = im.size
	self.assertEqual(new_width, 100)    
        print "Passed"

if __name__ == '__main__':
    unittest.main()
