# # Microservices Deployment Platform
This project is a platform designed to streamline the deployment and management of microservices in Kubernetes. The application enables users to authenticate securely and, upon authentication, grants access to various microservices using a JWT token, ensuring efficient and seamless deployment workflows.
Key Features

    User Authentication: Secure login system with JWT token-based authorization.
    Microservice Deployment: Simplified and efficient access to deploy and manage microservices.
#
# Tech Stack

- **Backend**: Python - FastAPI  
- **Containerization**: Docker  
- **Database**: PostgreSQL  
- **Orchestration**: Kubernetes

## Deploy Endpoints

| Method  | Endpoint           | Description                                | Parameters          | Response |
|---------|--------------------|--------------------------------------------|---------------------|-----------|
| GET     | `/deploy`          | Retrieves all deploys                      | Token in headers    | List of deploys |
| GET     | `/deploy/{id}`     | Retrieves a specific deploy by ID          | `deploy_id` in URL, Token in headers | Deploy data |
| POST    | `/deploy`          | Creates a new deploy                       | JSON in body with deploy data, Token in headers | Created deploy |
| DELETE  | `/deploy/{id}`     | Deletes a specific deploy                  | `deploy_id` in URL, Token in headers | Deletion confirmation |

### Usage Examples

#### Get all deploys
`


## Setup and Usage
## Prerequisites

Ensure you have the following installed on your machine:

    Python
    Docker 
    Kubernetes

Building the Application
docker-compose build

Start the aplication
docker-compose up
