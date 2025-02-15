#include "thingProperties.h"  // Required for Arduino IoT Cloud integration
#define TRIG_PIN 3  // Ultrasonic sensor trigger pin
#define ECHO_PIN 2  // Ultrasonic sensor echo pin
// Variables to store sensor readings
float distanceCM = 0;
bool objectDetected = false;
void setup() {
    Serial.begin(115200);
    pinMode(TRIG_PIN, OUTPUT);
    pinMode(ECHO_PIN, INPUT);
    // Initialize Arduino IoT Cloud
    initProperties();
    ArduinoCloud.begin(ArduinoIoTPreferredConnection);
    // Wait for cloud connection
    while (!ArduinoCloud.connected()) {
        ArduinoCloud.update();
        delay(500);
    }
    Serial.println("Connected to Arduino IoT Cloud!");
}
void loop() {
    ArduinoCloud.update();  // Update cloud variables
    distanceCM = getUltrasonicDistance();
    Serial.print("Distance: ");
    Serial.print(distanceCM);
    Serial.println(" cm");
    // If object is too close (<10 cm), trigger alarm
    if (distanceCM < 10) {
        objectDetected = true;
        Serial.println(" detected");
    } else {
        objectDetected = false;
    }
    delay(500);  // Update rate
}
// Function to measure distance using Ultrasonic Sensor
float getUltrasonicDistance() {
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);
    
    long duration = pulseIn(ECHO_PIN, HIGH);
    return duration * 0.034 / 2;  // Convert to cm
}