void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(A0));  // seed with floating pin noise for better randomness
}

void loop() {
  int num1 = random(0, 100);   // random number 0-99
  int num2 = random(0, 100);   // random number 0-99

  Serial.print(num1);
  Serial.print("x");
  Serial.println(num2);

  delay(500);  // send every 500ms, adjust as needed
}