#include <Servo.h>

const float speed_sound = 0.0343;

//servo left
Servo servoTL;
Servo servoBL;
//servo right
Servo servoTR;
Servo servoBR;

//Ultrasonic sonic distance sensors
//left
const int trigL = 9;
const int echoL = 8;

//right
const int trigR = 7;
const int echoR = 6;

//LED's
int LEDg = 10;
int LEDy = 11;
int LEDr = 12;


void setup(){
  Serial.begin(9600);
  
  //left us
  pinMode(trigL, OUTPUT);
  pinMode(echoL, INPUT);
  
  //right us
  pinMode(trigR, OUTPUT);
  pinMode(echoR, INPUT);
  
  //Servo left
  servoTL.attach(5);
  servoBL.attach(4);
  //servo right
  servoTR.attach(3);
  servoBR.attach(2);
  
}

void loop(){
  //LEDs
  pinMode(LEDg, HIGH);
  pinMode(LEDy, HIGH);
  pinMode(LEDr, HIGH);
  //initialize
  long durationL;
  long durationR;
  float distanceL;
  float distanceR;
  //set up
  digitalWrite(trigL, LOW);
  delayMicroseconds(2);
  digitalWrite(trigL, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigL, LOW);

  durationL = pulseIn(echoL, HIGH, 30000);
  distanceL = (durationL * speed_sound) / 2.0;

  // trigger RIGHT
  digitalWrite(trigR, LOW);
  delayMicroseconds(2);
  digitalWrite(trigR, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigR, LOW);

  durationR = pulseIn(echoR, HIGH, 30000);
  distanceR = (durationR * speed_sound) / 2.0;

  Serial.println(distanceL);
  Serial.println(distanceR);
  
  
  //movement
  if (distanceR <= 50 && distanceL <= 50){
    straight();
  }
}

void straight(){
  digitalWrite(LEDg, HIGH);
  //left > 90 and right < 90 to move stright servo
  //servo left
  servoTL.write(125);
  servoBL.write(55);
  //servo right
  servoTR.write(125);
  servoBR.write(55);
  delay(1000);
  
  servoTL.write(55);
  servoBL.write(125);
  //servo right
  servoTR.write(55);
  servoBR.write(125);
  delay(1000);
}

void left(){
}

void right(){
}