import docker
import os
import time
import toml


def get_config_path():
    # ... (no changes) ...


# Load configuration from TOML file
# ... (no changes) ...


client = docker.from_env()


def limit_container_resources(container, event_action):
    """Applies resource limits to the given container."""
    try:
        # Calculate memswap_limit based on mem_limit
        memswap_limit = int(mem_limit[:-1]) * 1024 * 1024 * 2

        container.update(
            cpu_period=100000,
            cpu_quota=int(cpus * 100000),
            mem_limit=mem_limit,
            memswap_limit=memswap_limit
        )
        print(f"Limited resources for container: {container.name} "
              f"(event: {event_action})")
    except Exception as e:
        print(f"Error limiting resources for container {container.name}: {e}")


def monitor_docker_events():
    """Monitors Docker events and limits resources."""
    for event in client.events(decode=True):
        if event['Type'] == 'container' and event['Action'] in ('create', 'start', 'restart'):
            container_name = event['Actor']['Attributes']['name']
            if any(keyword in container_name for keyword in keywords):
                try:
                    container = client.containers.get(event['id'])
                    limit_container_resources(container, event['Action'])
                except docker.errors.NotFound:
                    print(f"Container not found: {event['id']}")
                except Exception as e:
                    print(f"Error getting container: {e}")


def main():
    # ... (no changes) ...


if __name__ == "__main__":
    main()
