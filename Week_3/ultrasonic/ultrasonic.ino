/* 
  Ultrasonic Sensor (HC-SR04) with Arduino IoT Cloud
  This code sends distance readings from an HC-SR04 ultrasonic sensor to the IoT Cloud.
*/

#include "thingProperties.h"  // Includes IoT Cloud configuration

// Define pins for the ultrasonic sensor
#define TRIG_PIN 2
#define ECHO_PIN 3

void setup() {
  Serial.begin(9600);
  delay(1500);  // Wait for Serial Monitor to open

  // Initialize IoT Cloud properties
  initProperties();

  // Connect to Arduino IoT Cloud
  ArduinoCloud.begin(ArduinoIoTPreferredConnection);

  // Debugging mode for connection info
  setDebugMessageLevel(2);
  ArduinoCloud.printDebugInfo();

  // Set pin modes
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  ArduinoCloud.update();  // Keep IoT Cloud connection alive

  float distance = getDistance();  // Get sensor reading

  if (distance != -1) {  // Only update if distance is valid
    ultrasonic = distance;
    Serial.print("Distance: ");
    Serial.print(ultrasonic);
    Serial.println(" cm");
  } else {
    Serial.println("Sensor error! No valid reading.");
  }

  delay(2000);
}

// Function to measure distance using HC-SR04
float getDistance() {
  // Send trigger pulse
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // Read echo time with a timeout (30ms)
  long duration = pulseIn(ECHO_PIN, HIGH, 30000);

  // If no echo is received, return -1 (invalid reading)
  if (duration == 0) {
    Serial.println("No echo received! Check sensor connection.");
    return -1;
  }

  // Convert duration to distance (cm)
  float distance = duration * 0.034 / 2;
  return distance;
}

/*
  This function runs when the ultrasonic variable updates in the IoT Cloud
*/
void onUltrasonicChange() {
  Serial.println("Ultrasonic value changed in IoT Cloud!");
}
