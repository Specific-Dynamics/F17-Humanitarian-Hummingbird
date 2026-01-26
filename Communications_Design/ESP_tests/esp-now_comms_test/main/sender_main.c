/*
    The file controlling the sender of this button-to-light project. 
*/

#include <string.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "nvs_flash.h"
#include "esp_wifi.h"
#include "esp_now.h"
#include "esp_log.h"
#include "driver/gpio.h"    // a fun note is that need to add driver to the CMakeLists
                            // i mean, need to add any additional includes there but this is the one that caused me problems

#define BUTTON_GPIO GPIO_NUM_15     // uses GPIO15
#define WIFI_CHANNEL 1              // set WIFI_CHANNEL to be the same for sender/receiver

// receiver mac address (pulled from calling the mac function thingy in receiver_main)
uint8_t receiver_mac[] = {0x84, 0xf7, 0x03, 0xd7, 0xaa, 0xcc};

// bare-bones struct type to transmit the command. 
// works in this case cause its a binary on/off, but would likely need to be adjusted for real data
typedef struct{
    uint8_t command;
} espnow_cmd_t;

static const char *TAG = "SENDER";  // this just helps w/ the monitor logs

// wifi init required for espnow
// basically copied this out of the example project
static void wifi_init(void){
    ESP_ERROR_CHECK(esp_netif_init());
    ESP_ERROR_CHECK(esp_event_loop_create_default());

    wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
    ESP_ERROR_CHECK(esp_wifi_init(&cfg));
    ESP_ERROR_CHECK(esp_wifi_set_mode(WIFI_MODE_STA));
    ESP_ERROR_CHECK(esp_wifi_start());
    ESP_ERROR_CHECK(esp_wifi_set_channel(WIFI_CHANNEL, WIFI_SECOND_CHAN_NONE));
}

// button polling task???
// polling for now cause easier, would maybe wanna move to interrupt-driven later?
static void button_task(void *arg){
    bool last_state = false;

    while(1){
        // for those not comfy w/ freeRTOS, all tasks need to have an infinite loop inside them (either while(1) or for(;;))
        // anything outside the loop runs once at task creation (in app_main_sender in this case), and then the loop runs continuously
        // but this doesnt cause issues (like blocking) as long as the task gives up control using a delay or yield
        // (i mean, we only have one task in this case so doesnt really matter, but still)

        bool pressed = !gpio_get_level(BUTTON_GPIO);    // read button state

        if(pressed != last_state){
            // if state of button has changed, store the light state in cmd
            espnow_cmd_t cmd = {
                .command = pressed ? 1 : 0
            };

            esp_now_send(receiver_mac, (uint8_t *)&cmd, sizeof(cmd));   // transmit using espnow
            ESP_LOGI(TAG, "Button %s", pressed ? "PRESSED" : "RELEASED");   // a monitor log to keep track

            last_state = pressed;   // reset last_state of the button
        }

        vTaskDelay(pdMS_TO_TICKS(50));  // debounce i hope (seems to be okay!)
                                        // also allows for the task to give up control of the cpu
    }
}

void app_main_sender(void){
    // essentially like your normal main()
    // stole much of this from the example project. note that some of this stuff should probably have better error handling, but
    // i dont think its super necessary for just this test. 

    nvs_flash_init();
    wifi_init();

    gpio_config_t io = {
        .pin_bit_mask = 1ULL << BUTTON_GPIO,
        .mode = GPIO_MODE_INPUT,
        .pull_up_en = GPIO_PULLUP_ENABLE
    };
    gpio_config(&io);

    esp_now_init();

    esp_now_peer_info_t peer = {0};
    memcpy(peer.peer_addr, receiver_mac, ESP_NOW_ETH_ALEN);
    peer.channel = WIFI_CHANNEL;
    peer.ifidx = WIFI_IF_STA;
    peer.encrypt = false;

    esp_now_add_peer(&peer);

    ESP_LOGI(TAG, "app_main_sender started?");  // monitor log to ensure the right app_main ran

    xTaskCreate(button_task, "button task", 2048, NULL, 5, NULL);
}
