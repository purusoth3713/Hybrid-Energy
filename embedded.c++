#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_INA219.h>

Adafruit_INA219 ina219;

int relayPin = 7;
float voltage, current, power;

void setup() {
    Serial.begin(115200);
    ina219.begin();
    pinMode(relayPin, OUTPUT);
}

void loop() {
    voltage = ina219.getBusVoltage_V();
    current = ina219.getCurrent_mA();
    power = voltage * (current / 1000.0);

    if (power < 50) {
        digitalWrite(relayPin, HIGH);
    } else {
        digitalWrite(relayPin, LOW);
    }

    Serial.print("Voltage: "); Serial.print(voltage);
    Serial.print(" V, Current: "); Serial.print(current);
    Serial.print(" mA, Power: "); Serial.print(power); Serial.println(" W");
    delay(1000);
}
