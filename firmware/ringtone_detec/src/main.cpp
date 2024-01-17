#include <Arduino.h>

#include "tensorflow/lite/micro/all_ops_resolver.h"
#include "tensorflow/lite/micro/micro_error_reporter.h"
#include "tensorflow/lite/micro/micro_interpreter.h"
#include "tensorflow/lite/micro/system_setup.h"
#include "tensorflow/lite/schema/schema_generated.h"

// #include "NeuralNetwork.h"
#include "model_data.h"

// NeuralNetwork *nn;

const int microphonePin = 35;  // Replace A0 with the actual analog pin you are using
const int bufferSize = 10000;  // Assuming a sample rate of 16000 Hz and recording duration of 3 seconds

void recordMicrophone(float* audioData);

void setup() {
  pinMode(microphonePin, INPUT);
  Serial.begin(115200);
  // nn = new NeuralNetwork();
}

void loop() {
  // put your main code here, to run repeatedly:
  float audioData[bufferSize];

  recordMicrophone(audioData);

  delay(1000);
}


void recordMicrophone(float* audioData) {
  Serial.println("Recording...");

  // Record for the specified duration
  unsigned long startTime = millis();
  for (int i = 0; i < bufferSize; i++) {
    audioData[i] = analogRead(microphonePin);  // Normalize to the range [-1, 1]
    delayMicroseconds(100);  // Adjust this delay based on your microphone's characteristics
  }

  Serial.println("Recording finished");
}