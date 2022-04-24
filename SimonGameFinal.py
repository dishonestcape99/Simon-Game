#Simon game Santiago & Jaden
import RPi.GPIO as GPIO
from time import sleep
import pygame
from random import *

pygame.init()

leds = [6,13,19,21]
switches = [20,16,12,26]

sounds = [pygame.mixer.Sound("one.wav"),
          pygame.mixer.Sound("two.wav"),
          pygame.mixer.Sound("three.wav"),
          pygame.mixer.Sound("four.wav")]
GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(switches, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

pattern = []
sequence = 0
rest = 1

try:
    while (True):
        num = randint(0,3)
        pattern.append(num)
        for i in pattern:
            GPIO.output(leds[i], True)
            sounds[i].play()
            sleep(.75)
            GPIO.output(leds[i], False)
            sleep(.25)
       
        for y in pattern:
            pressed = False
            while(not pressed):
                val = 5
                for x in range(len(switches)):
                    if(GPIO.input(switches[x]) == True):
                        val = x
                        pressed = True
                        switches[x] == False
                if val == y and pressed:
                    if sequence < 15:
                        GPIO.output(leds[val], True)
                    sounds[val].play()
                    if sequence >= 5:
                        rest -= 0.02
                        if rest <= 0.02:
                            rest = 0.02
                    sleep(rest)
                    GPIO.output(leds[val], False)
                    sleep(.50)
                    sequence += 1
                elif val != y and pressed:
                    for i in range(5):
                        GPIO.output(leds, True)
                        sleep(0.5)
                        GPIO.output(leds, False)
                    print("Game over! You have reached level", sequence)
                    input("Press CRTL + C to quit")
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nBye!")