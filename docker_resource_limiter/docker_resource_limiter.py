import docker
import os
import time
import toml


def get_config_path():
    """Returns the path to the configuration file."""
    if os.path.exists('config.toml'):
        return 'config.toml'
    return '/etc/docker-resource-limiter/config.toml'


# Load configuration from TOML file
config_path = get_config_path()
with open(config_path, 'r') as f:
    config = toml.load(f)

# Access configuration values
settings = config.get('settings', {})
keywords = settings.get('keywords', '').split(',')
cpus = settings.get('cpus', 0.5)
mem_limit = settings.get('mem_limit', '100m')

client = docker.from_env()


def limit_container_resources(container):
    """Applies resource limits to the given container."""
    try:
        # Calculate memswap_limit based on mem_limit
        memswap_limit = int(mem_limit[:-1]) * 1024 * 1024 * 2  # Double the mem_limit

        container.update(
            cpu_period=100000,
            cpu_quota=int(cpus * 100000),
            mem_limit=mem_limit,
            memswap_limit=memswap_limit  # Set memswap_limit
        )
        print(f"Limited resources for container: {container.name}")
    except Exception as e:
        print(f"Error limiting resources for container {container.name}: {e}")


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


def main():
    while True:
        try:
            monitor_docker_events()
        except Exception as e:
            print(f"Error in monitor_docker_events: {e}")
        time.sleep(5)


if __name__ == "__main__":
    main()
