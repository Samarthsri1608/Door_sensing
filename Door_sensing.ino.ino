int irpin = 2; 
int irstate = 0; 

void setup(){
  Serial.begin(9600); 
  pinMode(irpin, INPUT);
}

void loop(){
  irstate = digitalRead(irpin); 

  if(irstate == LOW){
    Serial.println("Door Opened");
    delay(5000);
  }
}