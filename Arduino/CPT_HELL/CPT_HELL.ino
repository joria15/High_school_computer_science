int in2 = 2;
int in3 = 3;
int in4 = 4;
int in5 = 5;


int in8 = 8;
int in9 = 9;
int in10 = 10;
int in11 = 11;


int enAr = A0;
int enBr = A1;


int enAl = A2;
int enBl = A3;

int green = 12;
int yellow = A4;
int red = A5;




const int TRIG = 6;  // Trigger pin
const int ECHO = 7; // Echo pin
void setup() {


  pinMode(TRIG, OUTPUT); //Configure Trigger as an Output (to send a signal)
  pinMode(ECHO, INPUT); //Configure Echo as an Input (to receive a signal)
  Serial.begin(9600);




  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(in5, OUTPUT);


  pinMode(enAr, OUTPUT);
  pinMode(enBr, OUTPUT);
 
  pinMode(enAl, OUTPUT);
  pinMode(enBl, OUTPUT);

  pinMode(green, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(red, OUTPUT);



  pinMode(in8, OUTPUT);
  pinMode(in9, OUTPUT);
  pinMode(in10, OUTPUT);
  pinMode(in11, OUTPUT);
 
  // Turn off motors - Initial state
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  digitalWrite(in5, LOW);

  digitalWrite(in8, LOW);
  digitalWrite(in9, LOW);
  digitalWrite(in10, LOW);
  digitalWrite(in11, LOW);


}


void loop(){



  digitalWrite(TRIG, HIGH);//Set TRIG pin HIGH
  delayMicroseconds(10); //Pause 10 microseconds
  digitalWrite(TRIG, LOW); //Set TRIG pin LOW




  float distance = pulseIn(ECHO, HIGH);
  distance = distance / 58;


  Serial.print(" cm: ");
  Serial.println(distance);
  delay(500);

//middle
  if (distance >= 80 && distance <= 125 ){
    digitalWrite(green, HIGH);
    forward();
    digitalWrite(green, LOW);
  }

//inner left
 if (distance < 80){
    digitalWrite(red, HIGH);
    forward();
    delay(200);
    left();
    delay(200);
    digitalWrite(red, LOW);
  }
//inner right
 if (distance > 125 && distance < 175){
    digitalWrite(yellow, HIGH);
    forward();
    delay(200);
    right();
    delay(200);
  }
//outer middle
  if (distance >= 175 && distance < 200 ){
    digitalWrite(green, HIGH);
    forward();
    digitalWrite(green, LOW);
  }
//outer right
 if (distance >= 200){
    digitalWrite(red, HIGH);
    left();
    delay(400);
    forward();
    delay(400);
    right();
    delay(200);
    digitalWrite(red, LOW);
  }
//outer left

  // if (distance >= 175 && distance < 250){
  //   forward();
  //   delay(250);
  //   left();
  //   delay(250);
  // }


 
 






}








void forward(){


  analogWrite(enAr, 200);
  analogWrite(enBr, 200);


  analogWrite(enAl, 200);
  analogWrite(enBl, 200);


  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  digitalWrite(in5, HIGH);








  digitalWrite(in8, LOW);
  digitalWrite(in9, HIGH);
  digitalWrite(in10, HIGH);
  digitalWrite(in11, LOW);
}




void left(){


  analogWrite(enAr, 200);
  analogWrite(enBr, 200);


  analogWrite(enAl, 100);
  analogWrite(enBl, 100);


  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  digitalWrite(in5, HIGH);








  digitalWrite(in8, LOW);
  digitalWrite(in9, HIGH);
  digitalWrite(in10, HIGH);
  digitalWrite(in11, LOW);
}




void right(){


  analogWrite(enAr, 100);
  analogWrite(enBr, 100);


  analogWrite(enAl, 200);
  analogWrite(enBl, 200);


  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  digitalWrite(in5, HIGH);








  digitalWrite(in8, LOW);
  digitalWrite(in9, HIGH);
  digitalWrite(in10, HIGH);
  digitalWrite(in11, LOW);
}




void tankRight() {
  // Set motors to maximum speed, needed if enable A/B jumper pins removed
  // For PWM maximum possible values are 0 to 255
  //analogWrite(enA, 255);
  //analogWrite(enB, 255);








  // Turn on motor A & B
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  digitalWrite(in5, HIGH);
  delay(125);








  digitalWrite(in8, LOW);
  digitalWrite(in9, LOW);
  digitalWrite(in10, LOW);
  digitalWrite(in11, LOW);
  delay(125);








  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  digitalWrite(in5, HIGH);
  delay(200);








  digitalWrite(in8, LOW);
  digitalWrite(in9, HIGH);
  digitalWrite(in10, HIGH);
  digitalWrite(in11, LOW);
  delay(200);
}








void tankLeft(){
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  digitalWrite(in5, LOW);
  delay(500);








  digitalWrite(in8, LOW);
  digitalWrite(in9, LOW);
  digitalWrite(in10, HIGH);
  digitalWrite(in11, LOW);
  delay(500);








 
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  digitalWrite(in5, HIGH);
  delay(1000);








  digitalWrite(in8, LOW);
  digitalWrite(in9, HIGH);
  digitalWrite(in10, HIGH);
  digitalWrite(in11, LOW);
  delay(1000);
}















































