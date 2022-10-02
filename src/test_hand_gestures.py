import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model

import requests
import json

from src import rJoint

import time

mediapipe_hands_obj = mp.solutions.hands
hands_obj = mediapipe_hands_obj.Hands(max_num_hands=1, min_detection_confidence=0.7)
mediapipe_draw_obj = mp.solutions.drawing_utils

model = load_model("static/model/mp_hand_gesture")

gesture_names_file = open("static/model/gesture.names", "r")
class_names = gesture_names_file.read().split("\n")
gesture_names_file.close()
print(class_names)


capture = cv2.VideoCapture(0)

while True:

    _, frame = capture.read()
    x, y, c = frame.shape

    frame = cv2.flip(frame, 1)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands_obj.process(frame_rgb)

    class_name = ""

    if result.multi_hand_landmarks:
        landmarks = []

        for handslms in result.multi_hand_landmarks:

            # print(handslms)

            for lm in handslms.landmark:
                lmx = int(lm.x*x)
                lmy = int(lm.y*y)

                landmarks.append([lmx, lmy])

            # print(len(landmarks))
            # print(landmarks[20])

            # rJoint1 = rJoint.rJointClass()
            # rJoint1.add_coords1(landmarks[0][0], landmarks[0][1])
            # rJoint1.add_coords2(landmarks[5][0], landmarks[5][1])
            # rJoint1.add_coords3(landmarks[6][0], landmarks[6][1])
            # mid_angle = str(round(rJoint1.compute_mid_angle()))

            rHand_obj = rJoint.rHandClass()
            rHand_obj.get_landmarks_list(landmarks)
            mid_angles_dict = rHand_obj.return_joint_dict()

            mediapipe_draw_obj.draw_landmarks(frame, handslms, mediapipe_hands_obj.HAND_CONNECTIONS)
            cv2.putText(frame, str(round(mid_angles_dict["J2"])), (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
            cv2.putText(frame, str(round(mid_angles_dict["J5"])), (80,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
            cv2.putText(frame, str(round(mid_angles_dict["J9"])), (150,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
            cv2.putText(frame, str(round(mid_angles_dict["J13"])), (220,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
            cv2.putText(frame, str(round(mid_angles_dict["J17"])), (290,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

        print(mid_angles_dict)

        resp = requests.post("https://octopus-app-j626i.ondigitalocean.app/receive_controller", data=json.dumps(mid_angles_dict), headers={"Content-Type": "application/json"})

    cv2.imshow("repli.cate - Gesture Tracking", frame)
    if cv2.waitKey(1) == ord("q"):
        break 

capture.release()
cv2.destroyAllWindows()
