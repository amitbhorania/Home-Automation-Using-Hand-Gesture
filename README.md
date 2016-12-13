# Home-Automation-Using-Hand-Gesture
This is the project of Home Automation using Hand Gestures with Raspberry Pi, ADXL345 Accelerometer Sensor and Machine Learning Algorithm developed in Python.

Directory Structure
===================
-> Three Directories are included here
	1. Working Final Code - Contains the files which are finalised and working for the Project
	2. Extra Code during Development - 	Contains the files which we used during the development of the project 
										for the sensor interface, algorithm development and debugging
	3. Gesture Sample Files - 	Contains the Sensor data's sample files which are captured from the Raspberry PI for the 
								Designing of the Machine Learning Algorithm and various Gestures Training

Compilation and Run
===================
	1. Keep the working code files in the MicroSD Card of the Raspberry PI
	2. Start the Raspberry PI and wait for the Login screen to come up
	3. Login into the Raspberry PI with the credentials
	4. Open the Terminal and go to the code directory
	5. Run the following command
		python main.py
	6. Code will start running and will continuously take the sensor readings and process it to detect the hand gestures
