#include "FastLED.h"

#define NUM_LEDS 8             // LED灯珠数量
#define DATA_PIN 6              // Arduino输出控制信号引脚
#define LED_TYPE WS2812         // LED灯带型号
#define COLOR_ORDER GRB         // RGB灯珠中红色、绿色、蓝色LED的排列顺序

uint8_t max_bright = 255;       // LED亮度控制变量，可使用数值为 0 ～ 255， 数值越大则光带亮度越高

CRGB leds[NUM_LEDS];            // 建立光带leds
void setup() {
  LEDS.addLeds<LED_TYPE, DATA_PIN, COLOR_ORDER>(leds, NUM_LEDS);  // 初始化光带
  FastLED.setBrightness(max_bright);                            // 设置光带亮度
}

void loop() {
  leds[0] = CRGB::White;          // 设置光带中第一个灯珠颜色为红色，leds[0]为第一个灯珠，leds[1]为第二个灯珠
  leds[1] = CRGB::White;
  leds[2] = CRGB::White;
  leds[3] = CRGB::White;
  leds[4] = CRGB::White;
  leds[5] = CRGB::White;
  leds[6] = CRGB::White;
  leds[7] = CRGB::White;
  FastLED.show();                // 更新LED色彩
  delay(500);                     // 等待500毫秒
}
