/********************************************************************
; File name:    MPU-9250.ino            
; Date:         6 de setembro de 2021          
; Version:      1.0                              
; Arduino IDE:  v1.8.16  
; Author:       Teddy Ordoñez              
*********************************************************************/

/* 
This code was created by using Bolder Flight MPU-9250 library created by Brian R. Taylor
Currently using version 1.0.1. Firstly we create an MPU9250 object to call its functions.
When creating the object, we will be using I2C for communication protocol and 0x68
is the I2C address for the sensor. After it, we initiate the object and we start
reading the sensors in the loop function.
*/

#include <MPU9250.h>      // Including library for MPU-9250 sensor
#include <Wire.h>         // Including library for I2C communication
int status;               // Creating variable for receiving the status after initiating the object
MPU9250 IMU(Wire, 0x68);  // Creating IMU object

void setup() {
  Serial.begin(115200);   // Beginning communication with Serial monitor @ 115200 baud rate
  status = IMU.begin();   // Initiating object
}

void loop() {
  // put your main code here, to run repeatedly:
  IMU.readSensor();

  // Data from accelerometer
  Serial.print("Accelerometer X axis: ");
  Serial.print(IMU.getAccelX_mss(), 3);

  Serial.print("\t Accelerometer Y Axis: ");
  Serial.print(IMU.getAccelY_mss(), 2);

  Serial.print("\t Accelerometer Z Axis: ");
  Serial.println(IMU.getAccelZ_mss(), 2);

  // Data from Gyro
  Serial.print("Gyro X axis: ");
  Serial.print(IMU.getGyroX_rads(), 2);

  Serial.print("\t Gyro Y Axis: ");
  Serial.print(IMU.getGyroY_rads(), 2);

  Serial.print("\t Gyro Z Axis: ");
  Serial.println(IMU.getGyroZ_rads(), 2);

  // Data from Magnetomer
  Serial.print("Magnetomter X axis: ");
  Serial.print(IMU.getMagX_uT(), 2);

  Serial.print("\t Magnetometer Y Axis: ");
  Serial.print(IMU.getMagY_uT(), 2);

  Serial.print("\t Magnetometer Z Axis: ");
  Serial.println(IMU.getMagZ_uT(), 2);


  Serial.print("-------------------------\n");

  delay(2000);      // Fix delay time

}
