#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT22
#define SOIL_PIN A0

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  int soilRaw = analogRead(SOIL_PIN);
  float soilMoisture = map(soilRaw, 1023, 0, 0, 100); // Inverted scale
  float rainfall = 1.0;

  if (!isnan(temperature) && !isnan(humidity)) {
    Serial.print(temperature); Serial.print(",");
    Serial.print(humidity); Serial.print(",");
    Serial.print(soilMoisture); Serial.print(",");
    Serial.println(rainfall);
  }

  delay(5000);
}