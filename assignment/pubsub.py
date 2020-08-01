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

    def create_exchange(self,id, exchange_name):
        ch = this.channels[id]
        ch.exchange_declare(exchange_name, type='fanout')

    def publish_message(self, exchange_name, channel_id, sample_message):
        msg =  amqp.Message(sample_message)
        ch = this.channels[id]
        ch.publish_message(sample_message, exchange_name)

    def queue(self, id, exchange_name, queue_name):
        ch = this.channels[id]
        ch.queue_declare(queue_name)
        ch.queue_bind(queue_name, exchange_name)
        
    def rcv_msg(self, id, queue_name):
        ch = this.channels[id]
        msg = ch.basic_get(queue_name)
        if msg is not None:
            # do something
            ch.basic_ack(msg.delivery_tag)

    def wait_for_msg(self, id, queue_name):
        ch = this.channels[id]
        def mycallback(msg):
            print 'received', msg.body, 'from channel #', msg.channel.channel_id
        ch.basic_consume(queue_name, callback=mycallback, no_ack=True)
        while True:
            ch.wait()
