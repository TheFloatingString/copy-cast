from decimal import DivisionByZero
import math

class rJointClass:
    
    def __init__(self):
        self.x1 = None
        self.y1 = None

        self.x2 = None
        self.y2 = None

        self.x3 = None
        self.y3 = None

    def add_coords1(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

    def add_coords2(self, x2, y2):
        self.x2 = x2
        self.y2 = y2

    def add_coords3(self, x3, y3):
        self.x3 = x3
        self.y3 = y3

    def compute_mid_angle(self):
        try:
            vector_1 = {"x":self.x2-self.x1, "y":self.y2-self.y1}
            vector_2 = {"x":self.x3-self.x2, "y":self.y3-self.y2}
            
            vector_1_theta = math.atan(vector_1["y"]/vector_1["x"])*(360/(math.pi*2))
            vector_2_theta = math.atan(vector_2["y"]/vector_2["x"])*(360/(math.pi*2))

            mid_angle = 180 + (vector_2_theta - vector_1_theta)

            return mid_angle
        except ZeroDivisionError:
            return 0