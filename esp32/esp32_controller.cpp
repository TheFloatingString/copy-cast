#include <WiFi.h>
#include <HTTPClient.h>
//#include <Arduino_JSON.h>
#include <ArduinoJson.h>
  
const char* ssid = "MIT GUEST";
  
void setup() {
  
  Serial.begin(115200);
  delay(4000);
  WiFi.begin(ssid);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
  
  Serial.println("Connected to the WiFi network");
  
}
  
void loop() {

  DynamicJsonDocument doc(2048);

  
  if ((WiFi.status() == WL_CONNECTED)) { //Check the current connection status
  
    HTTPClient http;
  
    http.begin("https://octopus-app-j626i.ondigitalocean.app/emit_controller"); //Specify the URL
    int httpCode = http.GET();                                        //Make the request
  
    if (httpCode > 0) { //Check for the returning code
  
        String payload = http.getString();
        Serial.println(httpCode);
        Serial.println(payload);

        deserializeJson(doc, payload);

        double J2 = doc["J2"];
        double J5 = doc["J5"];
        double J9 = doc["J9"];
        double J13 = doc["J13"];
        double J17 = doc["J17"];

        Serial.print(J2);
        Serial.print(" ");
        Serial.print(J5);
        Serial.print(" ");
        Serial.print(J9);
        Serial.print(" ");
        Serial.print(J13);
        Serial.print(" ");
        Serial.println(J17);

      
        
      }
  
    else {
      Serial.println("Error on HTTP request");
    }
  
    http.end(); //Free the resources
  }
  
  delay(10);
  
}