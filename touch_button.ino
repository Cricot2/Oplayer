
#include <CapacitiveSensor.h>
CapacitiveSensor Sensor = CapacitiveSensor(4, 6);
#define led 12
long val;
int x;

void setup(){
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop(){
  val = Sensor.capacitiveSensor(30);
  Serial.println(val);
  if (val >= 1000 && x == 0){
    digitalWrite(led, HIGH);
    x = 1;
    delay(500);
  }
  else if (val >= 1000 && x == 1){
    digitalWrite(led, LOW);
    x = 0;
    delay(500);
  }

  delay(10);
}