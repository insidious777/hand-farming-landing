#!/bin/bash

COMPOSE="/usr/local/bin/docker-compose --no-ansi"
DOCKER="/usr/bin/docker"

cd ~/hand-farming-landing/
$COMPOSE run certbot renew && $COMPOSE restart nginx
$DOCKER system prune -af