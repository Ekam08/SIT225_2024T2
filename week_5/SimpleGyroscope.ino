#include <Arduino_LSM6DS3.h>

float x, y, z;

void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
}

void loop() {
  if (IMU.gyroscopeAvailable()) {
    IMU.readGyroscope(x, y, z);
    
    // Print data in CSV format (x,y,z)
    Serial.print(x);
    Serial.print(",");
    Serial.print(y);
    Serial.print(",");
    Serial.println(z);
  }
}