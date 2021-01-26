#define USE_ARDUINO_INTERRUPTS true
#include <PulseSensorPlayground.h> 
#include <Adafruit_Fingerprint.h>
#include <SoftwareSerial.h>


//FingerPrint
SoftwareSerial mySerial(2, 3);
Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);
uint8_t id;
PulseSensorPlayground pulseSensor;

//Pulse
const int PulseWire = 0; 
int Threshold = 550;

//LoginFingerPrint
int fingerprintID = 0;
int false_cnt = 0;



int mes = -1;
void setup() {
  Serial.begin(9600);

  
}
 
void loop() {
  false_cnt = 0;
  Serial.println("Please Type number");
  mes = readnumber();
  Serial.println(mes);
  if(mes == 1){
    Serial.println("FingerRegister");
    registerFingerPrint();
  }else if(mes == 2){
    Serial.println("FingerLogin");
    loginFingerPrint();
  }else if(mes == 3){
    Serial.println("PulseSensor");
    CheckPulseSensor();
  }else if(mes == 0){
    exit(1);
  }
  


}

uint8_t readnumber(void) {
  uint8_t num = 0;

  while (num == 0) {
    while (! Serial.available());
    num = Serial.parseInt();
  }
  return num;
}

uint8_t registerFingerPrint(void) {
  finger.begin(57600);
  if (finger.verifyPassword()) {
    Serial.println("Found Fingerprint!!");
  }
  Serial.println("Please put on your thumb");
  delayMicroseconds(10);
  id = readnumber();
  if (id == 0) {
    return;
  }
  while (!  getFingerprintEnroll() );
  delay(1000);

  return ;
  
}

uint8_t getFingerprintEnroll() {

  int p = -1;
  //Serial.println("Waiting for valid finger to enroll as #");
  Serial.println(0);
  while(true){
    p = finger.getImage();
    Serial.println("p"+p);
    if(p == FINGERPRINT_OK){
      Serial.println("Image converted");
      break;
    }
  }
  
  p = finger.image2Tz(2);
  delay(2000);
  
  p = finger.createModel();
  p = 0;
  if (p == FINGERPRINT_OK) {
    Serial.println("Prints matched!");
  } else {
    Serial.println("Unknown error");
    return true;
  }
  
  
  p = finger.storeModel(id);
  if (p == FINGERPRINT_OK) {
    //Serial.println("Stored!"); 
    Serial.println(1); 
  } else {
    Serial.println("error");
    
  }
  return true;
}


uint8_t loginFingerPrint(void){
  finger.begin(57600);
  if (finger.verifyPassword()) {
    Serial.println("Found Fingerprint!!");
  }
  Serial.println("Please put on your thumb");
  delayMicroseconds(10);
  
  while(true){
    if(false_cnt == 300){
      Serial.print("error");
      break;
    }
    fingerprintID = getFingerprintID();
    Serial.println(fingerprintID);
    delayMicroseconds(10);
    if(fingerprintID != 0){
      Serial.print("YourFingerID:");
      Serial.println(fingerprintID);
      false_cnt = 300;
    }else{
      false_cnt += 1;
    }
  }
  
}


int getFingerprintID() {
  uint8_t p = finger.getImage();
  if (p != FINGERPRINT_OK)  return 0;
 
  p = finger.image2Tz();
  if (p != FINGERPRINT_OK)  return 0;
 
  p = finger.fingerFastSearch();
  if (p != FINGERPRINT_OK)  return 0;
 
  return finger.fingerID;
}



uint8_t CheckPulseSensor(void){
  pulseSensor.analogInput(PulseWire);
  pulseSensor.setThreshold(Threshold);

  pulseSensor.begin();
  delay(20);
  unsigned long start_second = millis();
  int pulse_num = 0;
  int pulse_sum = 0;
  while(true){
    if(millis() -  start_second >= 30000){
      break;
    }
    if(pulseSensor.sawStartOfBeat()){
      int myBPM = pulseSensor.getBeatsPerMinute();
      Serial.println(myBPM);
      pulse_num++;
      pulse_sum += myBPM; 
    }
    
    
    
    delay(20);
  }
  //Serial.print("pulse_sum");
  Serial.println("average_pulse");
  int average_pulse = pulse_sum / pulse_num;
  Serial.println(average_pulse);
  
}
