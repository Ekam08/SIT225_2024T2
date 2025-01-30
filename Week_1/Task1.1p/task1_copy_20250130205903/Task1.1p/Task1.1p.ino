void setup() {
  pinMode(LED_BUILTIN, OUTPUT);  
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {  
    int blinks = Serial.parseInt();  

    for (int i = 0; i < blinks; i++) {  
      digitalWrite(LED_BUILTIN, HIGH);
      delay(500);  
      digitalWrite(LED_BUILTIN, LOW);
      delay(500);
    }

    Serial.println(random(2, 3));  
  }
}