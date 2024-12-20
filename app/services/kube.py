from db.models.deploy import Deploy
from db.models.microservice import Microservice 
from kubernetes import dynamic, config
from kubernetes import client as k8s_client
from kubernetes.client import api_client
from kubernetes.config import load_config
import time

def check_namespace_exist(namespace_api, new_namespace):
    
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
        print(f"Error creating namespace: {e}")

def create_manifest(image, name,  version, command):
    manifest = {
        #deploy in general
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {
            "name": name
        },
        "spec": {
            "replicas": 2,
            "selector": {
                "matchLabels": {
                    "app": "example-deploy"
                }
            },
            #pods
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

def execute_manifiest():
    pass

def create_deploy_k8s (deploy: Deploy ):
    deploy_id = deploy.id
    name = deploy.microservice.name
    environment=  deploy.environment.env
    new_namespace = f"{name}-{environment}"
    new_deploy = f"{new_namespace}-{deploy_id}"
    img = deploy.microservice.image
    version=  deploy.version
    command= deploy.command

    #Create API to interact with Kubernetes 30
    client = dynamic.DynamicClient(
        api_client.ApiClient(configuration=config.load_kube_config())
    )
    namespace_api = client.resources.get(api_version="v1", kind="Namespace")
    deployment_api = client.resources.get(api_version="apps/v1", kind="Deployment")

    if check_namespace_exist(namespace_api, new_namespace):
        manifest = create_manifest(img, new_deploy, version, command=["sleep", "3600"])
        deployment_api.create(body = manifest, namespace = new_namespace)
    else: 
        create_namespace(namespace_api, new_namespace)
        manifest = create_manifest(img, new_deploy, version, command=["sleep", "3600"])
        deployment_api.create(body = manifest, namespace = new_namespace)
        


