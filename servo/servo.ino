/*
 * Servo controller on ESP32DevkitC
 */
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>
#include <CircularBuffer.h>
#include <ESP32Servo.h>

// UART service UUID
#define SERVICE_UUID           "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
#define CHARACTERISTIC_UUID_RX "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
#define CHARACTERISTIC_UUID_TX "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"

// COMMAND
#define CMD_ANGLE1    0
#define CMD_ANGLE2    1
#define CMD_ANGLE3    2
#define CMD_DUTYCYCLE 3

// Number of servos
#define N_SERVOS 3

// for TEST flag
#define TEST_AXIS 2 // 0 = all servo, 1 = servo1, 2 = servo2, 3 = servo3

// pin
const int servoPin1 = 16;
const int servoPin2 = 17;
const int servoPin3 = 25;
const int servoPins[N_SERVOS] = {servoPin1, servoPin2, servoPin3};

// angle range
const double min_angle = 5;
const double max_angle = 175;

// Published values for FS90 servos; adjust if needed
int minUs = 500;
int maxUs = 2200;

// servo objects
Servo servo1; 
Servo servo2;
Servo servo3;
Servo servos[N_SERVOS] = {servo1, servo2, servo3};

// BLE variables
BLEServer *pServer = NULL;
BLECharacteristic * pTxCharacteristic;
bool deviceConnected = false;
bool oldDeviceConnected = false;
bool isEngineStarted = false;
uint8_t txValue = 0;
CircularBuffer<String, 10> buffer;

// Server callback
class ServerCallbacks: public BLEServerCallbacks {
    void onConnect(BLEServer* pServer) {
      Serial.println("connected");
      deviceConnected = true;
    };

    void onDisconnect(BLEServer* pServer) {
      Serial.println("disconnected");
      deviceConnected = false;
      pServer->startAdvertising(); // restart advertising
    }
};

// Data recieved callback
class DataRecievedCallbacks: public BLECharacteristicCallbacks {
    void onWrite(BLECharacteristic *pCharacteristic) {
      buffer.push(pCharacteristic->getValue().c_str());
    }
};

void parse_command() {
  String command = buffer.pop();
  if (command == "") {
    return;
  }
//  Serial.println(command);
  String type  = command.substring(0, 1); // command type
  String value = command.substring(2);    // command value
  double angle = value.toDouble();
  switch (type.toInt()) {
    case CMD_ANGLE1:
    {
      Serial.print("CMD_ANGLE1 ");
      Serial.println(angle);
      servos[0].write(angle);
      break;
    }
    case CMD_ANGLE2:
    {
      Serial.print("CMD_ANGLE2 ");
      Serial.println(angle);
      servos[1].write(angle);
      break;
    }
    case CMD_ANGLE3:
    {
      Serial.print("CMD_ANGLE3 ");
      Serial.println(angle);
      servos[2].write(angle);
      break;
    }
    default:
    {
      Serial.println("CMD_UNKNOWN");
    }
  }
}

void setup() {
  Serial.begin(115200);
  int i=0;

  // setup servos
  for (i=0; i<N_SERVOS; i++) {
    servos[i].setPeriodHertz(50);      // Standard 50hz servo
    servos[i].attach(servoPins[i], minUs, maxUs);
  }

  // Create the BLE Device
  BLEDevice::init("Servo Controller");

  // Create the BLE Server
  pServer = BLEDevice::createServer();
  pServer->setCallbacks(new ServerCallbacks());

    // Create the BLE Service
  BLEService *pService = pServer->createService(SERVICE_UUID);

  // Create a BLE Characteristic
  pTxCharacteristic = pService->createCharacteristic(
                        CHARACTERISTIC_UUID_TX,
                       BLECharacteristic::PROPERTY_NOTIFY
                      );
                      
  pTxCharacteristic->addDescriptor(new BLE2902());

  BLECharacteristic * pRxCharacteristic = pService->createCharacteristic(
                        CHARACTERISTIC_UUID_RX,
                        BLECharacteristic::PROPERTY_WRITE
                      );

  pRxCharacteristic->setCallbacks(new DataRecievedCallbacks());

  // Start the service
  pService->start();

  // Start advertising
  pServer->getAdvertising()->start();
  Serial.println("Waiting a client connection to notify...");
}

void loop() {
  parse_command();
  delay(50);
}
