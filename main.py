import XInput as input
import pyautogui as pya
import os
from time import sleep
import keyboard

#N of controller (MAX 4 Controllers connected)
print(input.get_connected()) # Write in N the index of the returned touple
N = 0

#Thumbs states
    #Left Thumb: [0]
    #Right Thumb: [1]
LEFT_THUMB = 0
RIGHT_THUMB = 1
XVALUE = 0
YVALUE = 1

    
while True:
    currentx,currenty = pya.position()

    while(input.get_thumb_values(input.get_state(0))[LEFT_THUMB][XVALUE] > 0):
        currentx += 20
        pya.moveTo(currentx, currenty)

    while(input.get_thumb_values(input.get_state(0))[LEFT_THUMB][XVALUE] < 0):
        currentx -= 20
        pya.moveTo(currentx, currenty)

    

    


