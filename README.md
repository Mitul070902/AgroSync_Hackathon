Escalating food demands necessitate sustainable agriculture that optimizes resources. Water scarcity poses a major challenge. This project proposes a smart irrigation system leveraging sensor data, machine learning (ML), and robust hardware. It aims to minimize water use while maximizing crop yield by dynamically adapting irrigation to each farm's unique environment.

Two ESP32 microcontrollers form the core. One resides at the farm with a camera, while the other, with internet access, resides at the farmer's location. LoRaWAN, a long-range, low-power communication protocol, bridges potential internet gaps at the farm, ensuring efficient data exchange.

Sensors (soil moisture, humidity, temperature) provide real-time data on crop health and the environment. Edge processing at the farm site reduces data transmission and power consumption. Processed data is then securely transmitted via LoRaWAN to the farmer's ESP32, which acts as a gateway, pushing data to the cloud for storage and analysis.

The cloud platform facilitates data aggregation and analysis. ML models, including a Naive Bayes algorithm for pump activation and a Support Vector Regressor for optimal soil moisture prediction, ensure precise and dynamic water application.

A user-friendly web application empowers farmers with real-time data visualizations, crop health monitoring, and ML insights. The system continuously learns by storing data, refining ML models over time for even greater water efficiency and improved crop yields.

This smart irrigation system, integrating sensor data, ML, and robust hardware with long-range communication, offers a promising solution for sustainable agriculture.

