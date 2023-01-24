##DP3 Physical Computing Prototype Code
##Team 19

##Import statements
import PCF8591_3 as ADC
from time import sleep
import math
from gpiozero import PWMOutputDevice

##Sets up the buzzer, and sets its value at 0.0 
DO = 17
buzzer = PWMOutputDevice(13)
buzzer.value = 0.0

##Sets up for input from sensors for output into the rasberry pi
def setup():
        ADC.setup(0x48) ##Setting up the ADC
        
##Takes input from thermistor, calculates average temperature from a data set of 6 values, and sends outputs from buzzer module
def input_output():       
        status = 1
        tmp = 1

        ##Defining key variables
        temp_avg = 0
        temp_list=[]

        ##Runs indefinitely
        while True:

                ##Converts analog data from the thermistor to digital data (degrees Celsius)
                analogVal = ADC.read(0)
                Vr = 5 * float(analogVal) / 255
                Rt = 10000 * Vr / (5 - Vr)
                temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
                temp = temp - 273.15

                ##Adds each temperature to blank temp_list
                temp_list.append(temp)

                ##Restricts the list to only taking the latter 6 values
                temp_list = temp_list[-6:]
                
                ##Calculates the average temperature and stores it in temp_avg
                temp_avg = sum(temp_list)/len(temp_list)
                print ('Current temperature is ', temp, 'C')
                print ('Average Temperature from last 6 values is ', temp_avg, 'C')
                 
                ##If the temperature is between 0 and -5 degrees inclusive, buzzer sounds 1 time
                if 34 >= temp_avg >= 29:
                        for i in range(2):
                                buzzer.value = 0
                                sleep(0.01)
                                buzzer.value = 0.05
                                sleep(0.01)

                ##If the temperature drops lower than -5 degrees, buzzer sounds twice in 1 second intervals. A notification is sent to the caretaker's phone
                elif temp_avg < 29:
                        for i in range(2):
                                buzzer.value = 0
                                sleep(1)
                                buzzer.value = 0.1
                                sleep(1)
                        print("Notification is sent from FAR to caretaker phone")
                        print("\n")

                ##If the temperature is higher than 34 degrees, no output from the buzzer
                else:
                        buzzer.value = 0.0
                        
                sleep(1) ##0.2 second delay in between measuring the next temperature value
        
##Main function, calls upon setup() and input_output()
def main():
        setup()
        input_output()

main()




