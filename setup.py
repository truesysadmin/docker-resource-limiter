from setuptools import setup, find_packages

setup(
    name='docker-resource-limiter',
    version='0.1.0',
    packages=find_packages(include=['docker_resource_limiter', 'tests']),
    test_suite='tests',
    install_requires=['docker'],
    entry_points={
        'console_scripts': [
            'docker-resource-limiter = '
            'docker_resource_limiter:main'
        ]
    },
    data_files=[
        ('/etc/docker-resource-limiter', ['config.ini'])
    ],
    test_suite='tests',
    # Add the following line to include your package data
    package_data={'docker_resource_limiter': ['*.py']},
    zip_safe=False  # This is generally needed when using package_data
)
