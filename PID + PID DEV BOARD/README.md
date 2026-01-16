# PID Board and Algo Documentation
The purpose of this markdown document is to provide justification of design decisions and document the development of the control system powering the drone. The end goal is to develop a transferable control system to levitate and control a homemade drone.

## Parts and Justification
Each of the parts that will be used for the project are listed below, along with a short justification as to why this was chosen. 

|Part|Model|
|-|-|
|MCU|ESP32-C6-VROOM-N8|
|IMU|ICM-40609-D|
|Buck (5V)|AP63205WU-7|
|LDO (1.8V)|MIC5504-1.8YM5-TR|

Motors will be handled with an integrated ESC, will be integrated once Khai and Vikram get their shit together.

### Microcontroller
To simplify life, an ESP32 was chosen. This already has built-in wifi, bluetooth and many other features. A rough choice is the **ESP32-C6-VROOM-N8**.

This was chosenfor the following reasons:
 
| Feature              | Why it's useful     |
| -------              |  ---------------    |
| Flash                | 8MB of Flash Storage|
| GPIO                 | |
| More reasons later  | |

Links:

[Datasheet](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32c6/esp32-c6-devkitc-1/user_guide_v1.1.html#related-documents)

[Digikey Link](https://www.digikey.com/en/products/detail/espressif-systems/esp32-c6-devkitc-1-n8/17728861?_gl=1*bsjl7y*_up*MQ..*_gs*MQ..&gclid=CjwKCAiA95fLBhBPEiwATXUsxLBFwHvS1fMWHF4lVN0X_DOU84KKaCmtfjcDqLiBISJI6qHKk3xq1BoCA_UQAvD_BwE&gclsrc=aw.ds&gbraid=0AAAAADrbLlg1yetCyhefuNT5N8oWAvpoc)

## IMU
Our IMU will be **ICM-40609-D**. This IMU is specifically made for drone usage, lowk gotta figure out how ts works.

Links:

[Datasheet](https://invensense.tdk.com/download-pdf/icm-40609-d-datasheet/)

[Digikey Link](https://www.digikey.com/en/products/detail/tdk-invensense/ICM-40609-D/19200630)
