#!/usr/bin/env bashio
set -e

bashio::config.require 'mqtt_user'
bashio::config.require 'mqtt_password'
bashio::config.require 'mqtt_topicprefix'

MQTT_USER=$(bashio::config 'mqtt_user')
MQTT_PASSWORD=$(bashio::config 'mqtt_password')
TOPIC_PREFIX=$(bashio::config 'mqtt_topicprefix')

echo "STARTING"
PYTHONPATH=/vedirect/vedirect python3 /vedirect_mqtt_van.py --port /dev/ttyUSB0 --mqttuser $MQTT_USER --mqttpass $MQTT_PASSWORD --topicprefix $TOPIC_PREFIX
