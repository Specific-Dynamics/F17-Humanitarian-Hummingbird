/*
    The file controlling the receiving esp of this button-to-light test. 
*/

#include <string.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "nvs_flash.h"
#include "esp_wifi.h"
#include "esp_now.h"
#include "esp_log.h"
#include "driver/gpio.h"

#include "esp_mac.h"

#define LED_GPIO GPIO_NUM_26
#define WIFI_CHANNEL 1

typedef struct{
    uint8_t command;
} espnow_cmd_t;

static const char *TAG = "RECEIVER";

// wifi init required for espnow
static void wifi_init(void){
    ESP_ERROR_CHECK(esp_netif_init());
    ESP_ERROR_CHECK(esp_event_loop_create_default());

    wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
    ESP_ERROR_CHECK(esp_wifi_init(&cfg));
    ESP_ERROR_CHECK(esp_wifi_set_mode(WIFI_MODE_STA));
    ESP_ERROR_CHECK(esp_wifi_start());
    ESP_ERROR_CHECK(esp_wifi_set_channel(WIFI_CHANNEL, WIFI_SECOND_CHAN_NONE));

}   


// receive callback for espnow
static void espnow_recv_cb(const esp_now_recv_info_t *info, const uint8_t *data, int len){
    if(len != sizeof(espnow_cmd_t)) return;

    espnow_cmd_t cmd;
    memcpy(&cmd, data, sizeof(cmd));

    gpio_set_level(LED_GPIO, cmd.command);
    ESP_LOGI(TAG, "LED %s", cmd.command ? "ON" : "OFF");
}

void app_main_receiver(void){
    nvs_flash_init();
    wifi_init();


    gpio_config_t io = {
        .pin_bit_mask = 1ULL << LED_GPIO,
        .mode = GPIO_MODE_OUTPUT
    };
    gpio_config(&io);

    esp_now_init();
    esp_now_register_recv_cb(espnow_recv_cb);

    uint8_t mac[6];
    esp_read_mac(mac, ESP_MAC_WIFI_STA);
    ESP_LOGI("MAC", "Station MAC: %02x:%02x:%02x:%02x:%02x:%02x", 
         mac[0], mac[1], mac[2], mac[3], mac[4], mac[5]);
}
