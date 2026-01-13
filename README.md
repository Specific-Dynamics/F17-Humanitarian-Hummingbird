*<div align="right"> Caleb Garcia, Vikram Procter, Minh Do, Ethan Sam, Chloe Fulbrook, Khai Huynh | December 13, 2025 </div>*

<img src="./pics/Specific_Dynamics_Logo_OneLine.png" alt="Logo Picture" width="435" height="256" />

# Specific Dynamics - F17 Humanitarian Hummingbird

## Our Mission

At Specific Dynamics, we are passionate about building a better world through engineering and innovation. We are pioneers in the domain of electrical, mechanical, and aerospace engineering, running on the cutting edge of efficiency, precision, and technology. We believe in creating a brighter future through humanitarian and technological execellence, while pushing the limits of possibility. Our team thrives on challenge, flourishing in pursuit of perfection, and continually redefining the frontiers of humanity. Through our creations, we strive to lead the industry in creating the next generation of sustainable aerospace systems, doing more with less and ensuring that nothing goes to waste. Our mission is to cultiavte people and production, laying the foundation for the next generation of engineers and innovators. Specific Dynamics — A Higher Purpose.

## Our Founder

Specific Dynamics was founded by our dear leader, Vikram Andrew Procter, on December 13th, 2025, amidst the chaos and struggles of the modern world. Our dear leader worked tirelessly to create a change — Specific Dynamics — while simultaneously pursuing residence as a neurosurgeon at John Hopkins University, a law degree at Harvard Law, and a Ph.D in Electrical Engineering at M.I.T. He single handedly created the resistor, and had his pioneering work in circuit theory, better known as Ohm's Law, stolen from him by malicious conspirators. In contrast to his greatness, our great leader came from humble beginnings. Our dear leader was born into a modest middle class family, scarcely earning more that a single million per annum. As a child, our brave leader faced many challenges, the stresses of choosing which car to drive each morning and which brand of caviar to have each night burdened him greatly. Despite this, our leader would rise to greatness, making his first billion dollars at the young age of twelve while climbing Mount Everest without an oxygen tank in only a quarter zip and Amiri jeans. Among other things, our great leader was also responsible for discovering penicillin, inventing the transistor, ideating quantum physics, and being the first to discover and contact extraterrestrial life. We dedicate this project to the honour of a great man, and our glorious leader! Heil, Vikram!

## Project Overview
PCB stator motors with the coils embedded in the pcb utilized in a remote control drone. 


## Team Roles

**Stator Motor and Brushless Controller:** Khai and Vikram

**PID Motor Control Loop:** Minh and Caleb

**Wireless Radio Control:** Chloe and Ethan

## Project Timeline
Week 1 | Jan 12 - Jan 18
-   Alpha PID dev board shipping Jan 16th
-   Alpha Communication Dev board shipping Jan 16th
-   Alpha PCB Stator tests shipping Jan 16th

Week 2 | Jan 19 - Jan 25
-   End of week Alpha stage has arrived
-   Stator motor shafts modeled and getting ready for cnc, (prototype in machine shop)

Week 3 | Jan 26 - Feb 1
-   Bi-weekly Status Report 1 Due Jan 26th
-   Alpha PCB finished testing and modifications are done
-   End of week beta dev Boards are shipping
-   End of week stator motor CNC is shipping 

Week 4 | Feb 2 - Feb 8
-   Design Review Presentation Video Due Feb 5th
-   Beta dev board arrive at end of week and testing can start
-   Characterization of stator motors underway

Week 5 | Feb 9 - Feb 15
-   Bi-weekly Status Report 1 Due Feb 9th
-   Dev boards arrive and testing starts Feb 9th

Week 6 | Feb 16 - Feb 22
-   Reading week (slave here please)
-   Lots of testing

Week 7 | Feb 23 - Mar 1
-   Requirements Specification, and Project Plan due Feb 23rd
-   Testing finishing up and MVP deliverables being recorded and written

Week 8 | Mar 2 - Mar 8
-   Bi-weekly Status Report 1 Due Mar 2nd
-   MVP Video Due March 6th
-   What should be working:
    - Radio communication working timely
    - PID tuned to fly with some drone motors and be tuneable
    - Stator motors tested and final design decided on
    - Everthing has been documented for testing and operation
    - Drone PCB designed and scaled properly

Week 9 | Mar 9 - Mar 15
-   Design Review Video Presentation Mar 9th
-   MVP Live Demo Due March 10th


Week 10 | Mar 16 - Mar 22
-   Bi-weekly Status Report 1 Due Mar 16th

Week 11 | Mar 23 - Mar 29
-   oooh la la

Week 12 | Mar 30 - April 5
-   Bi-weekly Status Report 1 Due Mar 30

Final Due | April 6 - April 7
-   Final prototype due April 6th
-   Final prototype Demo April 7th  


## Systems Overview
![SystemArchitectureBlockDiagram]()  
*Block diagram overview of project's functionality*

**Stator Motor and Brushless Controller**
- Built in PCB inductors for brushless motor
- Magnet sourcing
- https://www.openems.de/

**PID Motor Control Loop**
- IMU interfacing
- PID tuning
- Provide motor speed 

**Wireless Radio Control**
- Use ESP32 to communicate between controller and drone

**Battery Sourcing and Power Regulation**
- Source batteries with adequet capacity, current and weight
- Develope efficient regulator circuits


## Stator Motors
### PCB Motor Inductors
-   Epic [video](https://www.youtube.com/watch?v=CVszJMlvZcA) for inspiration
-   To buy motors [here](https://microbots.io/products/motorcell)
-   Open source [resource](https://github.com/microbotsio/MotorCell/tree/main/hardware/PCB%20Stator)

### Magnets

### Brushless Motor Controllers



## PID Motor Control Loop
### IMU Interfacing

### Microcontroller Utilization

### Motor Controller Speed Output



## Wireless Radio Control
### Microcontroller Utilization

### Antennna Placement

### Data Structure and Transfer Protocol


## Power Regulation
### Battery Sourcing

### Regulation Circuitry

