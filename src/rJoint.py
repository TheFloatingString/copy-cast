from decimal import DivisionByZero
from ftplib import parse150
import math

class rJointClass():
    
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

            if mid_angle > 180:
                mid_angle = 180

            if mid_angle < 0:
                mid_angle = 0

            return mid_angle
        except ZeroDivisionError:
            return 0

class rHandClass():

    def __init__(self):
        self.landmarks_list = None
        self.return_dict = {
            "J2": None,
            "J5": None,
            "J9": None,
            "J13": None,
            "J17": None
        }

    def get_landmarks_list(self, landmarks_list):
        self.landmarks_list = landmarks_list

    def wrap_joint_class(self, index1, index2, index3):
        rJoint_obj = rJointClass()
        rJoint_obj.add_coords1(self.landmarks_list[index1][0], self.landmarks_list[index1][1])
        rJoint_obj.add_coords2(self.landmarks_list[index2][0], self.landmarks_list[index2][1])
        rJoint_obj.add_coords3(self.landmarks_list[index3][0], self.landmarks_list[index3][1])
        mid_angle = rJoint_obj.compute_mid_angle()
        return mid_angle

    def return_joint_dict(self):

        self.return_dict["J2"] = self.wrap_joint_class(1,2,3)
        self.return_dict["J5"] = self.wrap_joint_class(0,5,6)
        self.return_dict["J9"] = self.wrap_joint_class(0,9,10)
        self.return_dict["J13"] = self.wrap_joint_class(0,13,14)
        self.return_dict["J17"] = self.wrap_joint_class(0,17,18)

        return self.return_dict