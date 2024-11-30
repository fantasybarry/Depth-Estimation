import cv2 as cv
import numpy as np
import json
from types import SimpleNamespace

class cameraConfig:
    def __init__(self):
        # Adjusted based on different specs of stereo cameras
        self.focal_length = 2.1
        self.distance_cameras = 120 # mm
        self.fov = 110 # in degrees(horizontal)

        self.blur_size = 5
        self.block_size = 5
        self.max_disparity = 64
# (1) Need to determine the image point of each frame(left and right) to get the disparity
# (2) Use the formula: depth = (focal_length * distance_cameras) / disparity
class Triangulation:
    def __init__(self):
        self.config = self.get_default_config()
    
    def get_default_config(self):
        return cameraConfig()
    
    def get_blur_level(self):
        blur_size = self.blur_size
        return (blur_size, blur_size)
    
    # Use Gaussian Blur to remove the noise
    def gaussian_blur(self, image):
        image = cv.GaussianBlur(image, self.get_blur_level, 0)
        return image
    
    ###################################################################################################
    # Image Rectification to reduces the 2D stereo Correspondence problem 
    # To a 1D problem(To put two images into one epipolar line)
    ###################################################################################################

    # Obtain the strong features(points) of left and right images
    def img_rectification(self, left_image, right_image):
        # Store the left corners and right corners of input images, respectively 
        left_corners = cv.goodFeaturesToTrack(left_image, maxCorners=50, 
                                              qualityLevel=0.01, minDistance=10, blockSize=self.config.block_size, 
                                              useHarrisDetector=True, k=0.04)
        right_corners = cv.goodFeaturesToTrack(right_image, maxCorners=50, 
                                               qualityLevel=0.01, minDistance=10, blockSize=self.config.block_size,
                                               useHarrisDetector=True, k=0.04)
        # Use cornerSubpix to get precise pixel location
        left_corners = cv.cornerSubPix(left_image, left_corners, winSize=(5, 5), zeroZone=(-1, -1), 
                                       criteria=(cv.TermCriteria_EPS + cv.TermCriteria_MAX_ITER, 100, 0.001))
        right_corners = cv.cornerSubPix(right_image, right_corners, winSize=(5,5), zeroZone=(-1, -1),
                                        criteria=(cv.TermCriteria_EPS + cv.TermCriteria_MAX_ITER, 100, 0.001))
        # Optical Flow function(if the input tested file is video or consecutive frame)
        # def optical_flow():
        return left_corners, right_corners

    # Calibrating the camera
    #def camera_calibration():

    # Find the fundamental matrix which encodes all aspects of the scene used to compute a rectification matrix
    def fundamental_matrix_calculation(self, left_corner_points, right_corner_points):
        return
        
        


    # Calculate the disparity
    #def disparity_calculation(self, left_image, right_image):
        # Assign rows and columns to height and weight, respectively
        #height, width = left_image.shape

        # Iterate over each y(rows) of the input image
        #for y in range()
    
    # Calculate the depthaaaaaa
    # def depth_calculation():
    




