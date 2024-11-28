import cv2 as cv
import numpy as np
import json
from types import SimpleNamespace

# Configuration
class calculation_config:
    
    def __init__(self):
        # Adjusted based on different specs of stereo cameras
        self.focal_length = 10
        self.distance_cameras = 5
        # Adjusted based on different image dimensions
        self.frame_width = 1280
        self.frame_height = 720
        
# (1) Need to determine the image point of each frames(left and right) to get the disparity
# (2) Use the formula: depth = (focal_length * distance_cameras) / disparity
class Triangulation():

    def __init__(self):
        self.config = self.get_default_config()
    
    def config_updated(self, jsonobject):
        self.config = json.loads(self.jdump(jsonobject), object_hook = lambda d: SimpleNamespace(**d))
    
    def get_default_config(self):
        return calculation_config
    
    def image_point():
        
        return
