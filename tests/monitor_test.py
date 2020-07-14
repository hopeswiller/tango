import pytest
from docker import models, errors
from src.tracker import container

# from tracker import container


def test_get_container():
    with pytest.raises(errors.NotFound) as e:
        sample_container = container.get_container("cname")

        assert sample_container == models.containers.Container
    assert e.type is errors.NotFound
