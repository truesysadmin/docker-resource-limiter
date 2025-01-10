from setuptools import setup, find_packages

setup(
    name='docker-resource-limiter',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['docker'],
    entry_points={
        'console_scripts': [
            'docker-resource-limiter = '
            'docker_resource_limiter:main'
        ]
    },
    data_files=[
        ('/etc/docker-resource-limiter', ['config.ini'])
    ]
)
