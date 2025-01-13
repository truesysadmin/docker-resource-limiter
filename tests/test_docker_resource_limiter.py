import os

from docker_resource_limiter.docker_resource_limiter import (
    get_config_path,
    limit_container_resources,
    cpus,
    mem_limit
)

import pytest


@pytest.fixture
def mocker():
    try:
        from unittest import mock
    except ImportError:
        import mock
    return mock.Mock()


def test_get_config_path_current_directory(tmp_path):
    """Test get_config_path() when config.ini is in current directory."""
    config_file = tmp_path / 'config.ini'
    config_file.write_text('[Settings]\nkeywords = test')
    os.chdir(tmp_path)
    assert get_config_path() == 'config.ini'


def test_get_config_path_default_path(tmp_path, monkeypatch):
    """Test get_config_path() when config.ini is not found."""
    monkeypatch.setattr(os.path, 'exists', lambda path: False)
    assert get_config_path() == '/etc/docker-resource-limiter/config.ini'


def test_limit_container_resources(mocker):
    """Test limit_container_resources() function."""
    mock_container = mocker.Mock()
    limit_container_resources(mock_container)
    mock_container.update.assert_called_once_with(
        cpu_period=100000,
        cpu_quota=int(cpus * 100000),
        mem_limit=mem_limit
    )
