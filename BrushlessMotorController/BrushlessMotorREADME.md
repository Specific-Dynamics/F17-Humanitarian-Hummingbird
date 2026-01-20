*<div align="right"> Vikram Procter, Khai Huynh | Jan 13, 2026 </div>*

# PCB Stator Motor | Specific Dynamics - F17 Humanitarian Hummingbird

## Overview
Building a pcb brusheless stator motor using the pcb traces as the motor coils 

### Component Selction
- Microcontroller [STM32F405RGT6](https://www.digikey.ca/en/products/detail/stmicroelectronics/STM32F405RGT6/2754208) to run timing and phase control.

- FET driver [DRV8329BREER](https://www.digikey.ca/en/products/detail/texas-instruments/DRV8329BREER/18178578) as gate driver for each phase mosfet. Each chip drives 6 fets or enough for 1 motor.

- NMOS selected [CSD17581Q5A](https://www.ti.com/product/CSD17581Q5A), [digikey](https://www.digikey.ca/en/products/detail/texas-instruments/CSD17581Q5A/6205539)

## Microcontroller


## MOSFET Driver
**Fault Detection:**  
*nFAULT* pin: Fault indicator output. This pin is pulled logic low during a fault condition and requires an external pull-up resistor to 3.3V to 5.0V. (Pg. 5)

Current Sense Operation:
- Monitors low side drain current by find voltage drop across R_sense. This voltage is then variably amplified.
- *SP, SN* pins: voltage drop across R_sense
- *CSAGAIN* pin: Resistor pull down determines gain. Should be shorted to GND

