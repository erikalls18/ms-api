from db.models.deploy import Deploy
from db.models.microservice import Microservice 
from kubernetes import dynamic, config
from kubernetes import client as k8s_client
from kubernetes.client import api_client
from kubernetes.config import load_config
import time

def check_namespace_exists(namespace_api, new_namespace):
    
    try: 
        if  namespace_api.get(name=new_namespace):
            return True
    except Exception as e :
        return False

def create_namespace(namespace_api, name):
    namespace_manifest = {
        "apiVersion": "v1",
        "kind": "Namespace",
        "metadata": {"name": name},
    }
    try:
        namespace_api.create(body=namespace_manifest)
        print(f"Namespace {name} created successfully.")
    except Exception as e:
        print(f"Error creating namespace: {e} {name}")


def create_manifest(image, name, version, command):
    manifest = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {
            "name": name
        },
        "spec": {
            "replicas": 2,
            "strategy": {
                "type": "RollingUpdate",
                "rollingUpdate": {
                    "maxSurge": "25%",
                    "maxUnavailable": "25%"
                }
            },
            "selector": {
                "matchLabels": {
                    "app": "example-deploy"
                }
            },
            "template": {
                "metadata": {
                    "labels": {
                        "app": "example-deploy"
                    }
                },
                "spec": {
                    "containers": [
                        {
                            "name": "new-container",
                            "image": f"{image}:{version}",
                            "ports": [{"containerPort": 8005}],
                            "command": command
                        }
                    ]
                }
            }
        }
    }
    return manifest

def check_deploy_exists(deployment_api, new_namespace, new_deploy):
    try: 
        if  deployment_api.get(name=new_deploy, namespace=new_namespace):
            print("existe1")
            return True
    except Exception as e :
        return False

def create_deploy_k8s (deploy: Deploy ):
    deploy_id = deploy.id
    name = deploy.microservice.name.lower()
    environment=  deploy.environment.env
    new_namespace = f"{name}-{environment}"
    new_deploy = f"{new_namespace}"
    img = deploy.microservice.image
    version=  deploy.version
    command= deploy.command.split()
  
    client = dynamic.DynamicClient(
        api_client.ApiClient(configuration=config.load_kube_config())
    )
    namespace_api = client.resources.get(api_version="v1", kind="Namespace")
    deployment_api = client.resources.get(api_version="apps/v1", kind="Deployment")

    if check_namespace_exists(namespace_api, new_namespace):
        manifest = create_manifest(img, new_deploy, version, command)
    else: 
        manifest = create_manifest(img,  new_deploy, version, command)
        create_namespace(namespace_api, new_namespace)
       
     

    if check_deploy_exists(deployment_api, new_namespace, new_deploy):
        deployment_api.replace(body=manifest, namespace=new_namespace, name=new_deploy)
    else: 
        deployment_api.create(body = manifest, namespace = new_namespace)

def delete_deploy_in_K8s(deploy: Deploy):
    deploy_id = deploy.id
    name = deploy.microservice.name.lower()
    environment=  deploy.environment.env
    new_namespace = f"{name}-{environment}"
    new_deploy = f"{new_namespace}"
    

    client = dynamic.DynamicClient(
        api_client.ApiClient(configuration=config.load_kube_config())
    )
    namespace_api = client.resources.get(api_version="v1", kind="Namespace")
    deployment_api = client.resources.get(api_version="apps/v1", kind="Deployment")

    try: 
        deployments= deployment_api.get(name=new_deploy, namespace=new_namespace)
        if deployments:
            deployment_api.delete(name=deployments.metadata.name, namespace=new_namespace)
            print(f"Deployment with deploy_id {deploy_id} deleted successfully2.")
        else:
            print(f"No Deployment found with deploy_id {deploy_id}.")
    except Exception as e:
        print(f"Error deleting deployment: {e}")


       



        


