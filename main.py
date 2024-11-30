import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
import Triangulation as tri


left_imgPath = r"/home/lintan/Depth-Estimation/Images/rame_020_lft.png"
right_imgPath = r"/home/lintan/Depth-Estimation/Images/frame_020_rgt.png"

left_image = cv.imread(left_imgPath, cv.IMREAD_GRAYSCALE)
right_image = cv.imread(right_imgPath, cv.IMREAD_GRAYSCALE)

display = tri.Triangulation()
print(display.img_rectification(left_image, right_image))