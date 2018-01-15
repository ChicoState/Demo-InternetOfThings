from time import sleep
import RPi.GPIO as GPIO

light = 17

from flask import (
	Flask,
	render_template,
	request,
)

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.Out)

app = Flask(__name__)

@app.route('/lights_on')

def setLights():
	GPIO.output(light, GPIO.HIGH)

return 1
	
if __name__ == "__main__":
	app.run('0.0.0.0', 5300)
