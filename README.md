# FAR-project

One major complication of a spinal cord injury resulting in paralysis is the consequential lack of ability to maintain a healthy body temperature. 
Our design aims to reduce the risk of frostbite by notifying the disabled individual when their skin temperature is too low.

Our physical computing prototype contains a thermistor to collect temperature input data, an analog-to-digital converter, 
and a buzzer module to communicate output to the user. The python code functions to calculate an average skin temperature, 
and determine if the value falls in one of the 3 ranges.

#TEST CASES
The following describes 3 sample tests with the expected input and output. Our test plan can then be compared with actual data obtained from running the program. 
Input: Temperature data (converted from analog to celsius), recorded every second


Outputs: Current temperature, average of 6 most recent temperatures, thermometer, buzzer module (Y/N), text alert (Y/N)

Test 1: Normal Conditions
Input: [36.0, 35.5, 35.8, 35.6, 36.1, 35.4, 34.8, 35.1]
Outputs: 
  Average: [36.0, 35.8, 35.8, 35.7, 35.8, 35.7, 35.5, 35.5]
  Buzzer Warning: [N, N, N, N, N, N, N, N]
  Text Alert: [N, N, N, N, N, N, N, N]
  Thermometer: > 34 

Test 2: Frostnip
Input: [35.1, 33.5, 33.1, 31.9, 31.5, 31.0, 29.4, 28.5]
Outputs:
	Average: [35.1, 34.3, 33.9, 33.4, 33.0, 32.7, 31.7, 30.9]
	Buzzer Warning: [N, N, Y, Y, Y, Y, Y, Y]
	Text Alert: [N, N, N, N, N, N, N, N]
	Thermometer: 34 > Temp > 29

Test 3: Frostbite
Input: [30.1, 29.5, 28.0, 25.9, 25.6, 25.8, 26.4, 26.3]
Outputs: 
	Average: [30.1, 29.8, 29.2, 28.4, 27.8, 27.5, 26.9, 26.3]
	Buzzer Warning: [Y, Y, Y, Y, Y, Y, Y, Y]
	Text Alert: [N, N, N, Y, Y, Y, Y, Y]
Thermometer: Temp < 29



Testing of Computing Prototype

Test 1: Normal Conditions
Input: [37.1, 39.4, 40.2, 40.5, 40.8, 41.1, 41.0, 41.3]
Outputs: 
  Average: [37.1, 38.3, 38.9, 39.3, 39.6, 39.9, 40.5, 40.8]
  Buzzer Warning: [N, N, N, N, N, N, N, N]
  Text Alert: [N, N, N, N, N, N, N, N]
Thermometer (Measuring Heat Pack): [44.5, 44.8, 45.0, 45.1, 45.2, 45.1, 45.3, 45.2]

Test 2: Frostnip
Input: [31.4, 31.5, 31.3, 31.3, 31.3, 31.4, 31.6, 31.5]
Outputs:
	Average: [31.4, 31.5, 31.4, 31.4, 31.4, 31.4, 31.4, 31.4]
	Buzzer Warning: [Y, Y, Y, Y, Y, Y, Y, Y]
	Text Alert: [N, N, N, N, N, N, N, N]
	Thermometer: [30.2, 30.2, 30.2, 30.3, 30.2, 30.2, 30.3, 30.3]

Test 3: Frostbite
Input: [29.1, 28.2, 26.8, 25.3, 25.0, 24.8, 24.6, 24.6]
Outputs: 
	Average: [29.1, 28.7, 28.0, 27.4, 26.9, 26.5, 25.8, 25.2]
	Buzzer Warning: [Y, Y, Y, Y, Y, Y, Y, Y]
	Text Alert: [N, Y, Y, Y, Y, Y, Y, Y]
Thermometer (Measuring Ice Water): [3.3, 3.2, 3.5, 3.3, 3.4, 3.6, 3.3, 3.2]
