import docker
client = docker.from_env()

# Read more on docker sdk 
# https://docker-py.readthedocs.io/en/stable/

def get_container(id_or_name):
    return client.containers.get(id_or_name)

def run_container(image,name,ports={},detach=False):
    return client.containers.run(image, name=name,ports=ports, detach=detach)

def list_containers():
    container_list = client.containers.list()
    for i in container_list:
        return i.attrs['Id'],i.attrs['Name']