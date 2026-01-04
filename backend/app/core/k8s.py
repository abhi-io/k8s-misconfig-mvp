from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException

def get_k8s_client():
    try:
        config.load_incluster_config()
    except ConfigException:
        config.load_kube_config()  # minikube uses this

    return {
        "core": client.CoreV1Api(),
        "apps": client.AppsV1Api(),
    }
