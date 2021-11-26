#import RPi.GPIO as GPIO
import time
from flask import Flask
app = Flask(__name__)


# PINS
FORWARD = 35
BACKWARD = 36
LEFT = 37
RIGHT = 38
LIGHT = 40

# DFFAULTS
DURATION = 1.0
DURATION_2 = 2.0

GPIO.setmode(GPIO.BCM)
GPIO.setup(FORWARD, GPIO.OUT)
GPIO.setup(BACKWARD, GPIO.OUT)
GPIO.setup(LEFT, GPIO.OUT)
GPIO.setup(RIGHT, GPIO.OUT)
GPIO.setup(LIGHT, GPIO.OUT)


def singleInstruction(pin, duration):
    reset()
    GPIO.output(pin, 1)
    time.sleep(duration)
    GPIO.output(pin, 0)


def dualInstruction(pin1, pin2, duration):
    reset()
    GPIO.output(pin1, 1)
    GPIO.output(pin2, 1)
    time.sleep(duration)
    GPIO.output(pin1, 0)
    GPIO.output(pin2, 0)


def reset():
    GPIO.output(FORWARD, 0)
    GPIO.output(BACKWARD, 0)
    GPIO.output(LEFT, 0)
    GPIO.output(RIGHT, 0)


@app.route('/forward')
def goForward():
    singleInstruction(FORWARD, DURATION)


@app.route('/backward')
def goBackward():
    singleInstruction(BACKWARD, DURATION)


@app.route('/forward-left')
def goForwardLeft():
    dualInstruction(FORWARD, LEFT, DURATION_2)


@app.route('/forward-right')
def goForwardRight():
    dualInstruction(FORWARD, RIGHT, DURATION_2)


@app.route('/backward-left')
def goBackwardLeft():
    dualInstruction(BACKWARD, LEFT, DURATION_2)


@app.route('/backward-right')
def goBackwardRight():
    dualInstruction(BACKWARD, RIGHT, DURATION_2)
