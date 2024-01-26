#include "DHT.h"

#define DHTPIN 2     
#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321

DHT dht(DHTPIN, DHTTYPE);

String cmd;

void setup() {
  Serial.begin(115200);
  Serial.println(F("tempHumidity example!"));

  dht.begin();
}

void loop() {
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  // Check if any reads failed and exit early (to try again).
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }
  // Reading command from python until encounter newline
  cmd = Serial.readStringUntil('\n');
  // If Temp is the command, get temperature in Celcius
  if (cmd == "Temp"){
    temperature = dht.readTemperature();
    Serial.print("Temp: ");
    Serial.println(temperature);
  }
  // If Humidity is the command, get Humidity
  if (cmd == "Humidity"){
    humidity = dht.readHumidity();
    Serial.print("Humidity: ");
    Serial.println(humidity);
  }
  // Wait a few seconds between measurements.
  delay(2000);
}
