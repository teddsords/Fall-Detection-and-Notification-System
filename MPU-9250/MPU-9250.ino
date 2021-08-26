#include <MPU9250.h>
#include <Wire.h>

MPU9250 IMU (Wire, 0x68);
int status;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  
  status = IMU.begin();
  if (status < 0) {
    Serial.println("IMU initialization unsuccessful");
    Serial.println("Check IMU wiring or try cycling power");
    Serial.print("Status: ");
    Serial.println(status);
    while(1) {}
  }

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

  // Data from temperature sensor
  Serial.print("Temperature: ");
  Serial.println(IMU.getTemperature_C(),2);

  Serial.print("\n\n");

  delay(2000);

}
