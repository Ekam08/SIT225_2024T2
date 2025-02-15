#include <ArduinoIoTCloud.h>
#include <Arduino_ConnectionHandler.h>

const char SSID[]     = "DESKTOP";    // Network SSID (name)
const char PASS[]     = "sehajgaba";    // Network password (use for WPA, or use as key for WEP)

void onDistanceChange();
void onAlarmChange();

float distance;
bool alarm;
void onDistanceChange() {
    Serial.println("Distance value updated in the IoT Cloud.");
    
}

void onAlarmChange() {
    Serial.println("Alarm status updated in the IoT Cloud.");
    
}

void initProperties(){

  ArduinoCloud.addProperty(distance, READWRITE, ON_CHANGE, onDistanceChange);
  ArduinoCloud.addProperty(alarm, READWRITE, ON_CHANGE, onAlarmChange);



}

WiFiConnectionHandler ArduinoIoTPreferredConnection(SSID, PASS);

