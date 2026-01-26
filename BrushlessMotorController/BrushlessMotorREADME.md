*<div align="right"> Vikram Procter, Khai Huynh | Jan 13, 2026 </div>*

# PCB Stator Motor | Specific Dynamics - F17 Humanitarian Hummingbird

## Overview
Building a pcb brusheless stator motor using the pcb traces as the motor coils 

### Component Selction

### Drone  Motor and Brushless Controller
- Drone Motors: COTS [YSIDO](https://www.aliexpress.com/item/1005005729701162.html)

- Microcontroller [STM32F405RGT6](https://www.digikey.ca/en/products/detail/stmicroelectronics/STM32F405RGT6/2754208) to run timing and phase control.

- FET driver [DRV8329BREER](https://www.digikey.ca/en/products/detail/texas-instruments/DRV8329BREER/18178578) as gate driver for each phase mosfet. Each chip drives 6 fets or enough for 1 motor.

- NMOS selected [CSD17581Q5A](https://www.ti.com/product/CSD17581Q5A), [digikey](https://www.digikey.ca/en/products/detail/texas-instruments/CSD17581Q5A/6205539)

## Microcontroller
*Find CubeMX .ioc file in STM32_Brushless... folder for exact pin specifications*

**Back EMF (Bemf) Measurement**
All 3 ADCs and all channels will be used to sample the Bemf for positional and speed feedback correction. Two ADCs are responsible for 

## MOSFET Driver
**Sleep and Reset**  
*nSLEEP Pin*: When this pin is pulled low the device goes into sleep mode. By pulsing it low for 1-1.2us the device can be reset without entering sleep mode. This pin has an internal pulldown, so STM32 **must pull pin high!**

**Fault Detection:**  
*nFAULT pin*: Fault indicator output. This pin is pulled logic low during a fault condition and requires an external pull-up resistor to 3.3V to 5.0V. (Pg. 5)

**Current Sense Operation:**
- Monitors low side drain current by find voltage drop across R_sense. This voltage is then variably amplified.
- *SP, SN pins*: voltage drop across R_sense
- *CSAGAIN pin*: Resistor pull down determines gain. Should be shorted to GND for 5x amplification. Could be replaced with 50kohm for 10x amplification. For 40x amplification connect CSAGAIN to AVDD or 3.3V 
    - $I=\frac{V_{so}-\frac{V_{CSAREF}}{8}}{CSAGAIN\times R_{SENSE}}$
    - For using a R_sense=0.5mΩ, and CSAGAIN=40x, and a $V_{CSAREF}$=3.3V, and a max V_so=3.3V:  
    - $I_{max}=\frac{3.3V-\frac{3.3V}{8}}{40\times 0.5m\Omega}=144A$
    - With this set up the resolution is 5A/0.1V

**Deadtime (Shoot Through Protection)**
- *DT pin*: Controlls deadtime (shoot through protection). By pulling the pin to ground via a resistor, the res val determines deadtime given by (pg.20):  
    - $R_{DT}(k\Omega)=\frac{Deadtime (ns)}{5}-10k\Omega$
    - If DT is grounded then default dead time of 55ns
    - 10k means 100ns, 20k means 150ns, 30k means 200ns

**Over Current Protection**
- *VDSLVL pin*: (Pg. 27) The voltage inputed to this pin determines threshold for an overcurrent event. The current is measured by finding the voltage drop across the mosfets as $I=V_{DS}*R_{DS(on)}$. When $V_{DS} > V_{DSLVL}$ for longer than the tDS_DG deglitch time, a VDS_OCP event is recognized. 
    - To set max current at 10A, with the R_DS(on)=3mOhm-4mOhm then V_DS=30mV-40mV
    - $V_{DSLVL}$ can range from 0.1-2.5V, meaning given this current limmmit and the R_DS(on) we cannot limmit internally.
    - Using the minimum $V_{DSLVL}=0.1V$ then limmit is set to 34.5A
    - So this feature will be disabled by grounding $V_{DSLVL}$ through **100kΩ** resistor
    - Same goes for VSENSE Overcurrent Protection (SEN_OCP) (Pg.27), which looks at the voltage drop across the R_sense

- *DRVOFF pin*: (pg. 24) When this pin is pulled high the Gate drivers are overriden and pulled low turning off all FETs. There is an strong internal pull down to prevent false positives. This pin will be connected to a comparitor monitoring the R_sense voltage to ensure when current max is reached the DRVOFF pin is pulled high 

