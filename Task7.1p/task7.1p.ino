#include <DHT.h>

#define DHTPIN 2       // DHT22 data pin connected to D2
#define DHTTYPE DHT22  
DHT dht(DHTPIN, DHTTYPE);

void setup() {
    Serial.begin(9600);
    dht.begin();
}

void loop() {
    float temp = dht.readTemperature();
    float hum = dht.readHumidity();

    if (!isnan(temp) && !isnan(hum)) {
        Serial.print(temp);
        Serial.print(",");
        Serial.println(hum);
    }
    delay(2000); // Capture data every 2 seconds
}
