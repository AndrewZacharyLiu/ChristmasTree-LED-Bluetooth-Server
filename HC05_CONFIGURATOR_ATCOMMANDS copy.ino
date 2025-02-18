#include <SoftwareSerial.h>
#include <FastLED.h>
#define LED_PIN 8
#define NUM_LEDS 300
#define BUFFER_SIZE 32
CRGB leds[NUM_LEDS];
SoftwareSerial BTSerial(10, 11);   // RX | TX
char commandBuffer[BUFFER_SIZE];   // Fixed-size buffer
int index = 0;
int pattern = 0;

void shimmer() {
  for (int i = 0; i < 4; i++) {
    fadeToBlackBy(leds, NUM_LEDS, 4);
    delay(10);
  }
  for (int stars = 0; stars < 8; stars++) {
    leds[random(NUM_LEDS)] = CRGB(150, 150, 150);
    delay(3);
  }
}

void processCommand(const char* command) {
  // Check for "OFF" command
  if (strcmp(command, "OFF") == 0) {
    Serial.println("Light OFF");
    FastLED.clear();
    FastLED.show();
    pattern = 0;
    return;
  }
  
  // Check for "COLOR:" prefix
  else if (strncmp(command, "COLOR:", 6) == 0) {
    const char* colorCode = command + 6; // Get the part after "COLOR:"
    if (strlen(colorCode) == 6) {        // Ensure it's a valid 6-character hex code
      pattern = 0;
      unsigned long hexColor = strtoul(colorCode, NULL, 16); // Convert hex to integer
      CRGB colorCode = CRGB((hexColor >> 16) & 0xFF, // Extract red
                        (hexColor >> 8) & 0xFF,  // Extract green
                        hexColor & 0xFF);        // Extract blue
      fill_solid( leds, NUM_LEDS, colorCode);
      FastLED.show();
      Serial.print("Set color");
    } else {
      Serial.println("Invalid COLOR format. Use COLOR:RRGGBB");
    }
    return;
  }
  
  // Check for "PATTERN:" prefix
  else if (strncmp(command, "PATTERN:", 8) == 0) {
    const char* patternValue = command + 8; // Get the part after "PATTERN:"
    pattern = atoi(patternValue);      // Convert the value to an integer
    if (pattern > 0) {                     // Ensure it's a valid number
      Serial.print("Set pattern to: ");
      Serial.println(pattern);
      // Example: Update your pattern logic here
    } else {
      Serial.println("Invalid PATTERN format. Use PATTERN:?");
    }
    return;
  }

  else if (strncmp(command, "GRAD:", 5) == 0) {
    if (strlen(command) < 17) {
      Serial.println("Error: Command too short for GRAD format.");
      return;
    }
    pattern = 0;
    char colorCode1[7] ={0}; // Array to hold the first color code
    char colorCode2[7] = {0}; // Array to hold the second color code
    strncpy(colorCode1, command + 5, 6);
    colorCode1[6] = '\0'; // Ensure null-termination
    strncpy(colorCode2, command + 11, 6);
    colorCode2[6] = '\0'; // Ensure null-termination  
    unsigned long hexColor1 = strtoul(colorCode1, NULL, 16); // Convert hex to integer
    unsigned long hexColor2 = strtoul(colorCode2, NULL, 16); // Convert hex to integer
    CRGB colorCRGB1 = CRGB((hexColor1 >> 16) & 0xFF, // Extract red
                        (hexColor1 >> 8) & 0xFF,  // Extract green
                        hexColor1 & 0xFF);        // Extract blue
    CRGB colorCRGB2 = CRGB((hexColor2 >> 16) & 0xFF, // Extract red
                        (hexColor2 >> 8) & 0xFF,  // Extract green
                        hexColor2 & 0xFF);        // Extract blue
    // Apply the gradient
    fill_gradient_RGB(leds, NUM_LEDS, colorCRGB1, colorCRGB2);
    FastLED.show();
    Serial.println("Set gradient successfully");
    Serial.print("Set grad");
    return;
  }
  
  // If no valid command is found
  Serial.print("Invalid command: ");
  Serial.println(command);
  leds[1] = CRGB(0, 0, 255); // Error indication
  FastLED.show();
}


void setup() {
  FastLED.addLeds<WS2812B, LED_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setBrightness(50);
  pinMode(9, OUTPUT);
  digitalWrite(9, LOW);
  //9600
  //38400
  Serial.begin(9600);
  BTSerial.begin(9600);
  FastLED.clear();
  FastLED.show();
}

void loop() {
    switch (pattern) {
      case 1:
        shimmer();
        FastLED.show();
      break;
    }
    

    if (Serial.available())           
    BTSerial.write(Serial.read());  

  // Read from HC-05 and process commands
  while (BTSerial.available()) {
    char incomingChar = BTSerial.read();
    
    if (incomingChar == '\n') {
      commandBuffer[index] = '\0';
      processCommand(commandBuffer);
      index = 0;                          // Reset index for the next command
    } else {
      if (index < BUFFER_SIZE - 1) {      // Prevent overflow
        commandBuffer[index++] = incomingChar;
      } else {
        commandBuffer[index] = '\0';
        processCommand(commandBuffer);    // Process the incomplete command
        Serial.println("Warning: Buffer overflow, processing early.");
        index = 0;                        // Reset index for the next command
      }
    }
  }
}
