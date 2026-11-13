
int in2  = 2;
int in3  = 3;
int in4  = 4;
int in5  = 5;


int in8  = 8;
int in9  = 9;
int in10 = 10;
int in11 = 11;

int enAr = A0;
int enBr = A1;
int enAl = A2;
int enBl = A3;

int green  = 12;
int yellow = A4;
int red    = A5;


const int TRIG = 6;
const int ECHO = 7;

// ================= WALL FOLLOW SETTINGS =================

const int WALL_DIST  = 100;  
const int BASE_SPEED = 180;   
const float KP       = 1.2;   

// ========================================================

void setup() {
  Serial.begin(9600);

  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(in5, OUTPUT);

  pinMode(in8, OUTPUT);
  pinMode(in9, OUTPUT);
  pinMode(in10, OUTPUT);
  pinMode(in11, OUTPUT);

  pinMode(enAr, OUTPUT);
  pinMode(enBr, OUTPUT);
  pinMode(enAl, OUTPUT);
  pinMode(enBl, OUTPUT);

  pinMode(green, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(red, OUTPUT);

  stopMotors();
}


void loop() {
  long distance = getDistance();
  Serial.println(distance);

  if (distance < 25) {
    digitalWrite(red, HIGH);
    drive(100, 220);  // sharp right
    return;
  }
  digitalWrite(red, LOW);


  int error = WALL_DIST - distance;    
  int correction = KP * error;

  int leftSpeed  = BASE_SPEED - correction;
  int rightSpeed = BASE_SPEED + correction;

  leftSpeed  = constrain(leftSpeed, 100, 255);
  rightSpeed = constrain(rightSpeed, 100, 255);

  drive(leftSpeed, rightSpeed);


  if (abs(error) < 10) {
    digitalWrite(green, HIGH);
    digitalWrite(yellow, LOW);
  } else {
    digitalWrite(green, LOW);
    digitalWrite(yellow, HIGH);
  }
}

// ================= FUNCTIONS =================


long getDistance() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  long duration = pulseIn(ECHO, HIGH, 25000);
  if (duration == 0) return 300;

  return duration / 58;
}


void drive(int leftSpeed, int rightSpeed) {

  analogWrite(enAl, leftSpeed);
  analogWrite(enBl, leftSpeed);

  analogWrite(enAr, rightSpeed);
  analogWrite(enBr, rightSpeed);

  // LEFT motors forward
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  digitalWrite(in5, HIGH);

  // RIGHT motors forward
  digitalWrite(in8, LOW);
  digitalWrite(in9, HIGH);
  digitalWrite(in10, HIGH);
  digitalWrite(in11, LOW);
}

// Stop motors
void stopMotors() {
  analogWrite(enAl, 0);
  analogWrite(enBl, 0);
  analogWrite(enAr, 0);
  analogWrite(enBr, 0);

  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  digitalWrite(in5, LOW);

  digitalWrite(in8, LOW);
  digitalWrite(in9, LOW);
  digitalWrite(in10, LOW);
  digitalWrite(in11, LOW);
}
