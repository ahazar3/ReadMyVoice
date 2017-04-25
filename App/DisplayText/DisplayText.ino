#include <Adafruit_GFX.h>    // Core graphics library
#include <Adafruit_TFTLCD.h> // Hardware-specific library

// The control pins for the LCD can be assigned to any digital or
// analog pins...but we'll use the analog pins as this allows us to
// double up the pins with the touch screen (see the TFT paint example).
#define LCD_CS A3 // Chip Select goes to Analog 3
#define LCD_CD A2 // Command/Data goes to Analog 2
#define LCD_WR A1 // LCD Write goes to Analog 1
#define LCD_RD A0 // LCD Read goes to Analog 0

#define LCD_RESET A4 // Can alternately just connect to Arduino's reset pin

#define BLACK   0x0000
#define BLUE    0x001F
#define RED     0xF800
#define GREEN   0x07E0
#define CYAN    0x07FF
#define MAGENTA 0xF81F
#define YELLOW  0xFFE0
#define WHITE   0xFFFF

Adafruit_TFTLCD tft(LCD_CS, LCD_CD, LCD_WR, LCD_RD, LCD_RESET);

char val; // Data received from the serial port
int ledPin = 13; // Set the pin to digital I/O 13

 void setup() {
  Serial.begin(9600);
  //tft.reset();
  uint16_t identifier = tft.readID();


  tft.begin(identifier);
  tft.setTextColor(BLACK);
  tft.setTextSize(4);
  tft.setRotation(tft.getRotation()+1);
  }


void loop() {
   if (Serial.available() > 0 ) 
   { 
    tft.fillScreen(WHITE);
    tft.setCursor(0,0);
    while(Serial.available()){// If data is available to read,
      
       //val = Serial.read(); // read it and store it in val
       //tft.print(val + " " );
      tft.print(Serial.readStringUntil('\n'));
    }
 

   //delay(2000);
   }
}

