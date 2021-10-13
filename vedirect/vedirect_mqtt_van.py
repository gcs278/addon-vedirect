#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse, os
import paho.mqtt.client as mqtt
from vedirect import Vedirect
import logging


if __name__ == '__main__':
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

    parser = argparse.ArgumentParser(description='Process VE.Direct protocol')
    parser.add_argument('--port', help='Serial port')
    parser.add_argument('--timeout', help='Serial port read timeout', type=int, default='60')
    parser.add_argument('--mqttuser', help='MQTT broker port', type=str)
    parser.add_argument('--mqttpass', help='MQTT broker address', type=str)
    parser.add_argument('--topicprefix', help='MQTT topic prefix', type=str, default='vedirect/')
    args = parser.parse_args()
    ve = Vedirect(args.port, args.timeout)

    mqtt_user = args.mqttuser
    mqtt_password = args.mqttpass
    topicprefix = args.topicprefix

    if not topicprefix.endswith('/'):
        topicprefix = topicprefix + "/"

    client = mqtt.Client("battery")
    client.username_pw_set(mqtt_user, mqtt_password)
    client.connect("127.0.0.1")

    client.loop_start()

    def mqtt_send_callback(packet):
        logging.info(f" Victron Data Received.")
        client.publish(topicprefix + "status", "online")
        for key, value in packet.items():
            if key != 'SER#': # topic cannot contain MQTT wildcards
                # logging.info(f" Publishing to topic {topicprefix + key} with value {value}")
                client.publish(topicprefix + key, value)

    client.publish(topicprefix + "status", "offline")
    logging.info(" Starting Victron Direct MQTT Service")

    ve.read_data_callback(mqtt_send_callback)
    
    client.publish(topicprefix + "status", "offline")