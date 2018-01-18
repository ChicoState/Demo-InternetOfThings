# Getting Started with IoT Demo: LED Automation

## How LED Automation Works
LED automation is an example of how IoT can be implemented with smart-home controllers. The LED Automation allows user to turn on an LED with a verbal command.

To activate the verbal commands one must say "OK google" or "Alexa" followed by a verbal command that the user programs themselves. Once the commands are accepted, the request will be sent to IFTTT, which will send a network request to the Raspberry Pi server, then this will be read by the Flask classes, and finally turn on the LED.

## Software needed
To get started, install the proper OS on the Raspberry Pi. A good way to start is with the NOOBS.

If you do not have NOOBS set up on your Raspberry Pi, click [here](https://www.raspberrypi.org/downloads/noobs/).

Once you have NOOBS set up on Raspberry Pi then you will need the following tools:

* Set up [Google Home](https://support.google.com/googlehome/answer/7126472?hl=en)
* Set Up [Amazon Alexa](https://www.amazon.com/gp/help/customer/display.html?nodeId=201601770)
* [Set up Flask on Raspberry Pi](https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/)
* Make an account with [IFTTT](https://ifttt.com/discover)

## Steps to Getting Started with LED Automation:

Once you have all the software needed you will then need to clone the repository to your desktop (or where ever you please) by opening the terminal, changing directory where you would like to clone then inputing:<br />
   "git clone https://github.com/ChicoState/Demo-InternetOfThings"
   
   To run the python code you can type in the terminal:<br />
   "python3 rd.py"
   
   Remember to wire up the Raspberry Pi and LED properly, if you need help doing so please refer to "Additional Links and Documentation".

##  Helpful Videos to get Started
Diagram to wire up Raspberry Pi with LED (Instead of pin 25 use pin 17), [click here](https://cdn.sparkfun.com/assets/e/1/4/c/a/528bd59d757b7f65548b4567.png) <br />
To get a visual idea of the LED Automation, [click here](https://www.youtube.com/watch?v=zp-HlLbT-xA)<br />
To get a quick explanation of what IFTTT is, [click here](https://www.youtube.com/watch?v=YV3DEmmDHdc)<br />
To see a similar example of the example here but with a Relay insdead, [click here](http://www.instructables.com/id/Google-Home-Raspberry-Pi-Power-Strip/)<br />
If you need a better explaination of LED Automation, [this link](https://www.youtube.com/watch?v=1Eo9NSiS3Y8) will send you the most thorough example I found on Youtube.<br />

