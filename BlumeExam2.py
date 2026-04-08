from gpiozero import LED, Button
from time import sleep

global redLed
redLed = LED(22)
global greenLed
greenLed = LED(27)
global blueLed
blueLed = LED(17)

global redButton
redButton = Button(18)
global greenButton
greenButton = Button(16)
global blueButton
blueButton = Button(20)

#turns off all LEDs at start of program
redLed.off()
greenLed.off()
blueLed.off()

# Functions to control the RGB color of the LED
def redColor():
    global redLed
    #redLed = RGBLED(red = 255, green = 0, blue = 0)
    #redLed.color(255,0,0)
    
    #Turns on red LED and turns off remaining colors
    redLed.on()
    greenLed.off()
    blueLed.off()
    
def greenColor():
    global greenLed
    #greenLed = RGBLED(red = 0, green = 255, blue = 0)
    #greenLed.color(0,255,0)
    
    #Turns on green LED and turns off remaining colors
    redLed.off()
    greenLed.on()
    blueLed.off()
    
def blueColor():
    #Accesses blueLed global variable
    global blueLed
    #blueButton = RGBLED(red = 0, green = 0, blue = 255)
    #blueLed.color(0,0,255)
    
    #Turns on blue LED and turns off remaining colors
    redLed.off()
    greenLed.off()
    blueLed.on()

#Checks if each button is being pressed and runs
#corresponding button's color method
if redButton.is_pressed:
    redColor()
elif greenButton.is_pressed:
    greenColor()
elif blueButton.is_pressed:
    blueColor()

