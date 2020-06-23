// Arduino touch button bang with litle return.

#include <CapacitiveSensor.h> 

CapacitiveSensor Sensor1 = CapacitiveSensor(4, 6);
CapacitiveSensor Sensor2 = CapacitiveSensor(9, 7);
CapacitiveSensor Sensor3 = CapacitiveSensor(2, 13);

#define button_play 12
#define button_moins 11
#define button_plus 10

long val_play;
long val_moins;
long val_plus;

void setup(){
  
  pinMode(button_play, OUTPUT);
  pinMode(button_moins, OUTPUT);
  pinMode(button_plus, OUTPUT);
}

void loop(){
  
  val_play = Sensor1.capacitiveSensor(30);
  val_moins = Sensor2.capacitiveSensor(30);
  val_plus = Sensor3.capacitiveSensor(30);
  
  if (val_play >= 1000){
    digitalWrite(button_play, HIGH);
  }
  else if (val_moins >= 1000){
    digitalWrite(button_moins, HIGH);
  }
  else if (val_plus >= 1000){
    digitalWrite(button_plus, HIGH);
  }
  else {
    digitalWrite(button_play, LOW);
    digitalWrite(button_moins, LOW);
    digitalWrite(button_plus, LOW);
  }
  
  delay(10);
}
