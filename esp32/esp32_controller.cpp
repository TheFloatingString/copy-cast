#include <WiFi.h>
#include <ESP32Servo.h>
#include <HTTPClient.h>
//#include <Arduino_JSON.h>
#include <ArduinoJson.h>
  
const char* ssid = "MIT GUEST";


Servo servo1; //thumb
Servo servo2; //index
Servo servo3; //middle
Servo servo4; //ring
Servo servo5; //pinky

  
void setup() {
  
  Serial.begin(115200);
  delay(4000);
  WiFi.begin(ssid);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
  
  Serial.println("Connected to the WiFi network");

  //servo1.attach(23); //thumb`
  servo2.attach(19); //index
  servo3.attach(23); //middle
  servo4.attach(26); //ring
  servo5.attach(25); //pinky

  zeroFingers();
  
}
  
void loop() {

  DynamicJsonDocument doc(2048);

  
  if ((WiFi.status() == WL_CONNECTED)) { //Check the current connection status
  
    HTTPClient http;
  
    http.begin("https://octopus-app-j626i.ondigitalocean.app/emit_controller"); //Specify the URL
    int httpCode = http.GET();                                        //Make the request
  
    if (httpCode > 0) { //Check for the returning code
  
        String payload = http.getString();


        deserializeJson(doc, payload);

        double J2 = doc["J2"];
        double J5 = doc["J5"];
        double J9 = doc["J9"];
        double J13 = doc["J13"];
        double J17 = doc["J17"];

        setFingers(J5, J9, J13, J17);
      }
  
    else {
      Serial.println("Error on HTTP request");
    }
  
    http.end(); //Free the resources
  }
  
  delay(10);
  
}

void setFingers(int j5, int j9, int j13, int j17)
{

  Serial.print(j5);
  Serial.print(" ");
  Serial.print(j9);
  Serial.print(" ");
  Serial.print(j13);
  Serial.print(" ");
  Serial.print(j17);
  Serial.println();

  
  servo2.write(j5); //index
  servo3.write(j9); //middle
  servo4.write(j13+90); //ring
  servo5.write(j17); //pinky
}

void zeroFingers()
{
  setFingers(0, 0, 0, 0);
}
