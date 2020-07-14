import pytest
from docker import models, errors
from src.tracker import container

# from tracker import container


def test_get_container():
    with pytest.raises(errors.NotFound) as e:
        sample_container = container.get_container("cname")

        assert sample_container == models.containers.Container
    assert e.type is errors.NotFound


def test_run_container():
    image_name = "image1"
    container_name = "container_name"
    ports = {"80/tcp": 80}
    with pytest.raises(errors.ImageNotFound) as e:
        sample_container = container.run_container(image_name, container_name, ports)

        assert sample_container == models.containers.Container
    assert e.type is errors.ImageNotFound
