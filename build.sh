#!/usr/bin/env bash

pack create --from packaging/
pack control Version 1.0.0
pack control Package docker-resource-limiter
pack control Architecture amd64
pack control Description "Service to limit docker containers by name"
pack control Maintainer "SAY10"
pack service ./docker-resource-limiter.service
pack add  docker_resource_limiter/docker_resource_limiter.py /usr/local/bin
pack add  docker_resource_limiter/config.toml /etc/docker-resource-limiter/

pack build
