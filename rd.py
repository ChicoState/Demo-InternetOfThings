from time import sleep #timing libraries
import RPi.GPIO as GPIO #including the libraries for the "general" raspberry pi pins

light = 17 #init the var "light" to the 17th gpio pin on raspberry pi

from flask import (
	Flask,
    render_template, #will look for an html file
    request, #contains data that browser has sent to the app
)

GPIO.setmode(GPIO.BCM) #initialling pins by the "Broadcom SOC channel"

GPIO.setup(17, GPIO.OUT)  #setting pin as an output

app = Flask(__name__) #use name if using a single module and something else if importing a module

@app.route('/lights_on') #"/" means root of the website (rbp ip) followed by "lights_on" page

def setLights(): #"setLights" is what we name the route for further reference
    GPIO.output(light, GPIO.HIGH) #setting pin as an output, pulling voltage up (high), to the pin light (17)

    return 1 #end app
	
if __name__ == "__main__": #sets built in varaible name to main
    app.run('0.0.0.0', 5300) #the 0.0.0.0 means this app is accessible by any device on the network
