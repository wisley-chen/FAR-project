# Goal of this project

One major complication of a spinal cord injury resulting in paralysis is the consequential lack of ability to maintain a healthy body temperature. 
Our design aims to reduce the risk of frostbite by notifying the disabled individual when their skin temperature is too low.

Our physical computing prototype contains a thermistor to collect temperature input data, an analog-to-digital converter, 
and a buzzer module to communicate output to the user. The python code functions to calculate an average skin temperature, 
and determine if the value falls in one of the 3 ranges:

1) The wearer’s skin temperature remains above 0 C and no output is received.
2) The thermistor measures a temperature between 0 C and -5 C and the buzzer module emits a warning noise to gain the attention of both the user and caregiver.
3) The thermistor reads below -5 C. The buzzer noise is sounded and a warning text* is sent over Bluetooth to the user’s primary caregiver, alerting them that the wearers extremities are at risk of frostbite.


