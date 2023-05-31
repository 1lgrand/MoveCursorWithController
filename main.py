import XInput as input
import pyautogui
import os
from time import sleep





while True:
    print(input.get_button_values(input.get_state(0))["A"])


