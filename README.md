# Docker Resource Limiter

This application monitors Docker events and automatically limits resources (CPU and memory) for containers with specific names. It's designed to help you control resource usage in your Docker environment and prevent runaway containers from consuming excessive resources.

## Features

* **Event Monitoring:** Continuously monitors Docker events for container creation.
* **Name-based Filtering:**  Applies resource limits only to containers with names that match specific keywords or patterns.
* **Resource Control:** Sets CPU shares and memory limits for targeted containers.
* **Configurable:**  Allows you to customize the keywords, CPU shares, and memory limits through an INI configuration file.
* **Systemd Integration:** Runs as a systemd service for reliable execution and management.
* **Easy Installation:**  Packaged as a Debian package (`.deb`) for easy installation on Debian-based systems.
* **CI/CD Integration:** Includes GitHub Actions workflows for automated testing, linting, and release.

## Installation

1. Download the latest `.deb` package from the Releases page.
2. Install the package using `dpkg -i`:

   ```bash
   sudo dpkg -i docker-resource-limiter_X.X.X-X_all.deb
