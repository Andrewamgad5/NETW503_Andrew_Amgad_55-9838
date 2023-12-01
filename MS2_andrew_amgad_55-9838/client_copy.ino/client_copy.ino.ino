#include <ESP8266WiFi.h>
#include <DHT.h>

const char* ssid = "Orange_E20A";
const char* password = "Aeam_2001";
const char* server = "192.168.1.239";
const int port = 9900;

#define DHTPIN1 5 //DHT Sensor 1 Pin
#define DHTPIN2 4 //DHT Sensor 2 Pin
#define DHTTYPE DHT22

DHT dht1(DHTPIN1, DHTTYPE);
DHT dht2(DHTPIN2, DHTTYPE);

WiFiClient client;

void setup() {
 Serial.begin(115200);
 dht1.begin();
 dht2.begin();

 delay(10);
 Serial.println();
 Serial.print("Connecting to ");
 Serial.println(ssid);

 WiFi.begin(ssid, password);

 while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
 }

 Serial.println("");
 Serial.println("WiFi connected");
 Serial.println("IP address: ");
 Serial.println(WiFi.localIP());
}

void loop() {
 float h1 = dht1.readHumidity();
 float t1 = dht1.readTemperature();
 float h2 = dht2.readHumidity();
 float t2 = dht2.readTemperature();

 if (isnan(h1) || isnan(t1) || isnan(h2) || isnan(t2)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
 }

 if (client.connect(server, port)) {
    String data = "Temperature: " + String(t1) + ", Humidity: " + String(h1) + "\nTemperature: " + String(t2) + ", Humidity: " + String(h2);
    client.print(data);
    Serial.println("Data sent to the server.");
    delay(2000);
 } else {
    Serial.println("Connection failed.");
 }
 client.stop();

 delay(5000);
}