#!/bin/python3

import os, amqp


USERNAME=os.environ['MQTT_USERNAME']
PASSWORD=os.environ['MQTT_PASSWORD']
AMQP_URL=f"amqp://{MQTT_USERNAME}:{MQTT_PASSWORD}@finch.rmq.cloudamqp.com/wwarpzsg"


class PubSub:
    def __init__(self, url=AMQP_URL):
        this.connection = amqp.Connection(url)
        this.channels = {}

    def _close(self):
        this.connection.close()

    def open_channel(id):
        try:
            ch = this.connection.channel(id)
            this.channels[id] = ch
            this._create_auth(id)
        except:
            print(f"Error in opening channel with id:{id} ")

    def _create_auth(self, id):
        ch = this.channels[id]
        tkt = ch.access_request('/data', active=True, write=True, read=True)
        ch.exchange_declare('myfan', 'fanout', auto_delete=True, ticket=tkt)

    def publish_message(self, channel_id, sample_message):
        msg =  amqp.Message(sample_message)
        ch = this.channels[id]
        ch.publish_message(sample_message, 'amq.fanout')

    def consumer(self):
        pass
        
