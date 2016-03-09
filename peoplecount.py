from ubidots import ApiClient
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

try:

    api = ApiClient("2ca001387c4c47c9cb8077e2aa4304ba59ec46aa")

    people = api.get_variable("56b762ae7625423eb1aa078c")

except:

    print "Couldn't connect to the API, check your Internet connection"

counter = 0

peoplecount = 0

while(1):

    presence = GPIO.input(4)

    if(presence):

        peoplecount += 1

        presence = 0

        time.sleep(1.5)

    time.sleep(1)

    counter += 1

    if(counter==10):

        print peoplecount

        people.save_value({'value':peoplecount})

        counter = 0

        peoplecount = 0
