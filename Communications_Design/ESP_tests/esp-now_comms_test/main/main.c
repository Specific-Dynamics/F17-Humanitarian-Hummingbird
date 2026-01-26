
/*
    This project basically a test of the esp-now protocol. Currently very simple, just clicking a button on one esp makes
    a light turn on on the other esp (while button held down).

    This file allows switching of which app_main is to be used to actually build and flash.
    This means that we can have all the code for different parts (receiver or transmitter) in the same project for easier organization,
    but still flash them independently. 

    Note that it's still necessary to update the COM port and board type in settings.json to choose the right board.
    And also that you need to make sure that the files are appropriately included in CMakeLists. 

*/

void app_main_sender();
void app_main_receiver();
void app_main_example();

void app_main(void){
    app_main_sender();
}