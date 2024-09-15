# Fully Automated Data Pipeline with Kafka, PySpark, and Docker

This project demonstrates a fully automated data pipeline designed to generate and process synthetic datasets using Kafka for real-time streaming and PySpark for distributed data processing. The entire system is containerized using Docker for portability and easy deployment.

## Features

- **Real-time Data Streaming**: Uses Apache Kafka for generating and streaming synthetic data in real-time.
- **Distributed Processing**: PySpark is used for scalable distributed data processing of the streamed data.
- **Containerized**: All components (Kafka, PySpark, data generation) are containerized using Docker for easy setup and deployment.
- **Scalable**: Designed to handle large volumes of data in a distributed fashion.
- **Automated**: Fully automated pipeline from data generation to processing.

## Technologies Used

- **Python 3.12**
- **Apache Kafka**: A distributed event streaming platform for handling real-time data streams.
- **PySpark**: A Python API for Apache Spark, enabling distributed data processing.
- **Docker**: Containerization tool to package the application for portability.
- **Docker Compose**: To orchestrate multi-container Docker applications.
