import cv2 as cv
import numpy as np
import json
from types import SimpleNamespace

class calculation_config:
    
    def __init__(self):
        self.focal_length = 10
        self.baseline = 5

class Triangulation():

    def __init__(self, dir = "left"):
        self.config = self.get_default_config()
    
    def config_updated(self, jsonobject):
        self.config = json.loads(self.jdump(jsonobject), object_hook = lambda d: SimpleNamespace(**d))
    
    def get_default_config(self):
        return calculation_config
    
    