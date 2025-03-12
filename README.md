## Microservices Deployment Platform
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

## Microservices Endpoints

| **Method**  | **Endpoint**            | **Parameters**      | **Description**                                  |
|------------|------------------------|--------------------|--------------------------------------------------|
| **GET**    | `/services`             | `limit: int = 100` | Retrieve a list of microservices.               |
| **GET**    | `/services/{ms_id}`     | `ms_id: int`       | Retrieve a specific microservice by its ID.     |
| **POST**   | `/services`             | JSON in body with microservice | Create a new microservice. |
| **PUT**    | `/services/{ms_id}`     | `ms_id: int`, JSON in body with microservice | Update an existing microservice. |
| **DELETE** | `/services/{ms_id}`     | `ms_id: int`       | Delete a microservice by its ID.                |


## Deploy Endpoints

| **Method**  | **Endpoint**              | **Parameters**          | **Description**                                  |
|------------|--------------------------|------------------------|--------------------------------------------------|
| **GET**    | `/deploy`                 | N/A                    | Retrieve all deployments.                        |
| **GET**    | `/deploy/{deploy_id}`     | `deploy_id: int`       | Retrieve a specific deployment by its ID.       |
| **POST**   | `/deploy`                 | JSON in body with deploy | Create a new deployment.        |
| **DELETE** | `/deploy/{deploy_id}`     | `deploy_id: int`       | Delete a deployment by its ID.                  |

---
## Environment Endpoints

| **Method**  | **Endpoint**                  | **Parameters**        | **Description**                                      |
|------------|------------------------------|----------------------|------------------------------------------------------|
| **GET**    | `/environment`               | N/A                  | Retrieve all environments.                          |
| **GET**    | `/environment/type/{env}`    | `env: EnvironmentType` | Retrieve environments filtered by type.            |
| **GET**    | `/environment/{env_id}`      | `env_id: int`        | Retrieve a specific environment by its ID.         |
| **POST**   | `/environment`               | JSON in body with environment | Create a new environment.         |
| **DELETE** | `/environment/{env_id}`      | `env_id: int`        | Delete an environment by its ID.                   |


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
