import asyncio
import sys
import time

import cv2
import gym
import numpy as np
import gym.spaces

CMD_ANGLE1    = "0"
CMD_ANGLE2    = "1"
CMD_ANGLE3    = "2"
ANGLE_LOW     = 5
ANGLE_HIGH    = 175
N_AXIS        = 2
if N_AXIS == 1:
    CMD_ANGLES = [CMD_ANGLE2]
elif N_AXIS == 2:
    CMD_ANGLES = [CMD_ANGLE2, CMD_ANGLE3]
else:
    CMD_ANGLES = [CMD_ANGLE1, CMD_ANGLE2, CMD_ANGLE3]

CAMERA_IMAGE_PATH  = "catkin_ws/camera_image.jpg"
BUTTON_STATUS_PATH = "catkin_ws/button_status.txt"


# min-max scaling
def min_max(x, axis=None):
    min_x = x.min(axis=axis, keepdims=True)
    max_x = x.max(axis=axis, keepdims=True)
    result = (x - min_x) / (max_x - min_x)
    return result

class MrRobotarmEnv(gym.Env):
    def __init__(self):
        super().__init__()
        img = self.read_image() # read camera image
        self.action_space      = gym.spaces.Box(low=ANGLE_LOW, high=ANGLE_HIGH, shape=(N_AXIS, ), dtype=np.float32)
            
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=img.shape, dtype=np.float32) # image size
        self.ble_motor = None
        self.loop      = None
        self.viewer    = None
        self.rewards   = 0

    def set_ble_motor(self, ble_motor, loop):
        self.ble_motor = ble_motor
        self.loop      = loop
        # reset observation
        self.reset()

    def reset(self):
        self.motor_action(CMD_ANGLE1, "90")
        self.motor_action(CMD_ANGLE2, ANGLE_HIGH)
        self.motor_action(CMD_ANGLE3, "0")
        observation   = self.read_image() # read the camera image
        return observation

    def step(self, a):
        # action
        for i in range(N_AXIS):
            self.motor_action(CMD_ANGLES[i], a[i])

        # next observation
        observation   = self.read_image() # read the camera image

        # calculate reward
        button_status = self.read_button_status() # read the button status
        reward = -1
        if not button_status:
            reward = 1

        done = False

        return observation, reward, done, {}

    def render(self, mode='human'):
        img = self.read_image() # read the camera image
        if mode == 'rgb_array':
            return img
        elif mode == 'human':
            from gym.envs.classic_control import rendering
            if self.viewer is None:
                self.viewer = rendering.SimpleImageViewer()
            self.viewer.imshow(img)
            return self.viewer.isopen

    def motor_action(self, motor_num, angle):
        self.loop.run_until_complete(self.ble_motor.write(motor_num, angle)) # servo action
        time.sleep(0.5)

    def read_image(self):
        def read_whole_image():
            with open(CAMERA_IMAGE_PATH, 'rb') as f:
                check_chars = f.read()[-2:]
                if check_chars != b'\xff\xd9':
                    return None
                else:
                    return cv2.imread(CAMERA_IMAGE_PATH) # read the camera image

        img = read_whole_image()
        while img is None:
            img = read_whole_image()

        # shrink the image
        h, w = img.shape[:2]
        size = (int(h / 2), int(w / 2))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
        # img = min_max(img)
        # !!TEST!!
        img = img.flatten()

        return img

    def read_button_status(self):
        button_status = open(BUTTON_STATUS_PATH).read() # read the button status
        while not button_status:
            button_status = open(BUTTON_STATUS_PATH).read() # read the button status
        return int(button_status)
