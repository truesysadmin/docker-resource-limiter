from setuptools import setup, find_packages

setup(
    name='docker-resource-limiter',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[
        'docker',
        # Use a conditional requirement for stdeb
        'stdeb; python_version<"3.0"',  # For older Python versions
    ],
    entry_points={
        'console_scripts': [
            'docker-resource-limiter = '
            'docker_resource_limiter:main'
        ]
    },
    data_files=[
        ('/etc/docker-resource-limiter', ['config.ini'])
    ],
    package_data={'docker_resource_limiter': ['*.py']},
    description="A tool to monitor Docker events and limit container resources",
    long_description="""
    This application monitors Docker events and automatically limits
    resources (CPU and memory) for containers with specific names.
    It's designed to help you control resource usage in your Docker
    environment and prevent runaway containers from consuming excessive
    resources.
    """,
    zip_safe=False  # This is generally needed when using package_data
)
