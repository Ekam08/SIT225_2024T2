// Code generated by Arduino IoT Cloud, DO NOT EDIT.

#include <ArduinoIoTCloud.h>
// Code generated by Arduino IoT Cloud, DO NOT EDIT.

#include <ArduinoIoTCloud.h>
#include <Arduino_ConnectionHandler.h>  // ✅ Keep this, it handles cloud connection

const char SSID[]     = "DESKTOP";    // Network SSID (name)
const char PASS[]     = "ekamgaba";   // Network password

WiFiConnectionHandler ArduinoIoTPreferredConnection(SSID, PASS);  // ✅ Use this instead

void onUltrasonicChange();  // Declare function

float ultrasonic;  // Declare IoT Cloud variable

void initProperties() {
  ArduinoCloud.addProperty(ultrasonic, READWRITE, ON_CHANGE, onUltrasonicChange);
}
