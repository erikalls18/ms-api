# ms-api
This project is a platform designed to streamline the deployment and management of microservices in Kubernetes. The application enables users to authenticate securely and, upon authentication, grants access to various microservices using a JWT token, ensuring efficient and seamless deployment workflows.
Key Features

    User Authentication: Secure login system with JWT token-based authorization.
    Microservice Deployment: Simplified and efficient access to deploy and manage microservices.
Tech Stack

    Backend: Python - FastAPI
    Containerization: Docker
    Database: PostgreSQL 
    Orchestration: Kubernetes

Setup and Usage
Prerequisites

Ensure you have the following installed on your machine:

    Docker
    Docker Compose

Building the Application

To build the Docker containers, run: docker-compose build
To start the application, use: docker-compose up
