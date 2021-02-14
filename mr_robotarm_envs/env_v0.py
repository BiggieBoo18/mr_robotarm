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
CMD_DUTYCYCLE = "3"
ANGLE_LOW     = 5
ANGLE_HIGH    = 175

CAMERA_IMAGE_PATH  = "catkin_ws/camera_image.jpg"
BUTTON_STATUS_PATH = "catkin_ws/button_status.txt"

class MrRobotarmEnv(gym.Env):
    def __init__(self):
        super().__init__()
        img = self.read_image() # read camera image
        self.action_space      = gym.spaces.Box(low=ANGLE_LOW, high=ANGLE_HIGH, shape=(1,), dtype=np.float32)
        self.observation_space = gym.spaces.Box(low=0, high=255, shape=img.shape, dtype=np.float32) # image size
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
        self.motor_action(CMD_ANGLE2, ANGLE_HIGH)
        observation   = self.read_image() # read the camera image
        return observation

    def step(self, a):
        # action
        self.motor_action(CMD_ANGLE2, a[0])

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
        self.loop.run_until_complete(self.ble_motor.write("0", 90))          # servo1
        time.sleep(0.5)
        self.loop.run_until_complete(self.ble_motor.write(motor_num, angle)) # servo2
        time.sleep(0.5)
        self.loop.run_until_complete(self.ble_motor.write("2", 0))           # servo3
        time.sleep(1)

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
        img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)

        return img

    def read_button_status(self):
        button_status = open(BUTTON_STATUS_PATH).read() # read the button status
        while not button_status:
            button_status = open(BUTTON_STATUS_PATH).read() # read the button status
        return int(button_status)
