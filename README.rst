=====
Python Photo Editor
=====

Python Photo Editor is simple python program that uses c++ opencv library to do simple photo editing tasks
like converting to grayscale, posterization, resize, rotating etc

Detailed documentation is in the "docs" directory.

About
-----------

Dir Structure

├── docs
│   ├── quickguide.txt
│   └── test_resize.txt
├── images
│   ├── cat.jpeg
│   └── dog.jpeg
├── processed_images
│   ├── gray_cat.jpeg
│   ├── poster_cat.jpeg
│   ├── resized_cat.jpeg
│   ├── rotated_cat.jpeg
│   └── test_cat.jpeg
├── README.rst
├── src
│   ├── packages
│   │   ├── image_processer.py
│   │   ├── image_processer.pyc
│   │   ├── __init__.py
│   │   ├── __init__.pyc
│   │   ├── ui.py
│   │   └── ui.pyc
│   ├── photo.py
│   └── slide.py
└── tests
    └── test_opencv_resize.py

1. Follow docs/quickguide to start using Photo Editor
2. Source Images will be stored in images dir.
3. Processed Images will be store in processed_images dir.
4. Test cases are stores in tests dir. To run test case do following
	cd tests
	python test_case.py
	
