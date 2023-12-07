Given the requirements and assumptions, we will need to create the following core classes, functions, and methods:

1. `MQTTClient`: This class will handle the MQTT communication between the Raspberry Pi and the Arduino. It will have methods to connect to the broker, publish messages, and subscribe to topics.

2. `WiFiManager`: This class will manage the WiFi network hosted by the Raspberry Pi. It will have methods to start the network, stop the network, and check the network status.

3. `LightController`: This class will control the PWM lights. It will have methods to turn the lights on/off, adjust the brightness, and get the current status of the lights.

4. `GUI`: This class will handle the touch-friendly GUI. It will have methods to display the status of the lights and the network, and to get user input.

5. `SystemMonitor`: This class will monitor the system status and display updates on the GUI. It will have methods to check the connectivity between the Raspberry Pi and the Arduino, and to display warnings in case of connectivity failures.

Now, let's start with the entrypoint file, `main.py`.

main.py
