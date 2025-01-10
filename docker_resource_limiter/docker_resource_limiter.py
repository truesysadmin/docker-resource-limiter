import configparser
import docker
import os
import time


def get_config_path():
    """Returns the path to the configuration file."""
    if os.path.exists('config.ini'):
        return 'config.ini'
    return '/etc/docker-resource-limiter/config.ini'


# Load configuration from INI file
config = configparser.ConfigParser()
config_path = get_config_path()
config.read(config_path)

# Get configuration values
keywords = config.get(
    'Settings', 'keywords',
    fallback='limit_resources,test,special'
).split(',')
cpus = config.getfloat('Settings', 'cpus', fallback=0.5)
mem_limit = config.get('Settings', 'mem_limit', fallback='100m')

client = docker.from_env()


def limit_container_resources(container):
    """Applies resource limits to the given container."""
    try:
        container.update(
            cpu_period=100000,
            cpu_quota=int(cpus * 100000),
            mem_limit=mem_limit
        )
        print(f"Limited resources for container: {container.name}")
    except Exception as e:
        print(f"Error limiting resources for "
              f"container {container.name}: {e}")


def monitor_docker_events():
    """Monitors Docker events and limits resources."""
    for event in client.events(decode=True):
        if event['Type'] == 'container' and event['Action'] == 'create':
            container_name = event['Actor']['Attributes']['name']
            if any(keyword in container_name for keyword in keywords):
                try:
                    container = client.containers.get(event['id'])
                    limit_container_resources(container)
                except docker.errors.NotFound:
                    print(f"Container not found: {event['id']}")
                except Exception as e:
                    print(f"Error getting container: {e}")


if __name__ == "__main__":
    while True:
        try:
            monitor_docker_events()
        except Exception as e:
            print(f"Error in monitor_docker_events: {e}")
        time.sleep(5)
