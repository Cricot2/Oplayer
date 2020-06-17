
// Arduino touch button bang with litle return.
#include <CapacitiveSensor.h>
CapacitiveSensor Sensor = CapacitiveSensor(4, 6);
#define button_play 12
long val;

void setup(){
  pinMode(button_play, OUTPUT);
}

void loop(){
  val = Sensor.capacitiveSensor(30);
  if (val >= 1000){
    digitalWrite(button_play, HIGH);
    delay(500);
    digitalWrite(button_play, LOW);
    delay(70);
    digitalWrite(button_play, HIGH);
    delay(100);
  }
  else {
    digitalWrite(button_play, LOW);
  }

  delay(10);
}
