## Microservices Deployment Platform  

This project is a platform designed to streamline the deployment and management of microservices in Kubernetes. The application enables users to authenticate securely and, upon authentication, grants access to create microservices, environments, and deployments.  

### Key Features  

The application operates with two independent APIs:  

- **deploy_auth**: A containerized API with a PostgreSQL database that securely manages user authentication using a JWT token-based authorization system.  
- **ms_api**: Handles CRUD operations on a PostgreSQL database and automates the creation of deployments in Kubernetes, simplifying the deployment process.  
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


## Environment Endpoints

| **Method**  | **Endpoint**                  | **Parameters**        | **Description**                                      |
|------------|------------------------------|----------------------|------------------------------------------------------|
| **GET**    | `/environment`               | N/A                  | Retrieve all environments.                          |
| **GET**    | `/environment/type/{env}`    | `env: EnvironmentType` | Retrieve environments filtered by type.            |
| **GET**    | `/environment/{env_id}`      | `env_id: int`        | Retrieve a specific environment by its ID.         |
| **POST**   | `/environment`               | JSON in body with environment | Create a new environment.         |
| **DELETE** | `/environment/{env_id}`      | `env_id: int`        | Delete an environment by its ID.                   |

## Deploy Endpoints

| **Method**  | **Endpoint**              | **Parameters**          | **Description**                                  |
|------------|--------------------------|------------------------|--------------------------------------------------|
| **GET**    | `/deploy`                 | N/A                    | Retrieve all deployments.                        |
| **GET**    | `/deploy/{deploy_id}`     | `deploy_id: int`       | Retrieve a specific deployment by its ID.       |
| **POST**   | `/deploy`                 | JSON in body with deploy | Create a new deployment.        |
| **DELETE** | `/deploy/{deploy_id}`     | `deploy_id: int`       | Delete a deployment by its ID.                  |

---

## Setup and Usage

### Prerequisites  

Before running the application, ensure you have the following installed:  

- **Docker** (required to run the containers)  
- **Docker Compose** (to manage multi-container applications)  
- **Kubernetes** (a working kubeconfig in the ~/.kube directory)

- Create a .env file to store secrets and algorithm configurations.

## Building the Application  

1. Clone, build, and run the **deployAuth** application: https://github.com/erikalls18/deployAuth.git.  
2. Clone, build and run the **ms_api** application.  

To build and start the application, run the following commands:  

```sh
docker-compose build
docker-compose up


