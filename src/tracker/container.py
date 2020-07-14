import docker
client = docker.from_env()

# Read more on docker sdk 
# https://docker-py.readthedocs.io/en/stable/

def get_container(id_or_name):
    try:
        return client.containers.get(id_or_name)
    except docker.errors.NotFound:
        raise docker.errors.NotFound('Container Name not found')
    

def run_container(image,name,ports={},detach=False):
    try:
        return client.containers.run(image, name=name,ports=ports, detach=detach)
    except docker.errors.ImageNotFound:
        raise docker.errors.ImageNotFound(f'Image {image} not found, repo does not exist')
    

def list_containers():
    container_list = client.containers.list()
    for i in container_list:
        return i.attrs['Id'],i.attrs['Name']
