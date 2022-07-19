#!/usr/bin/env python3
'''
Created on 20220710
Update on 20220718
@author: Eduardo Pagotto
 '''

from pulsar import Client, schema


def main():
    client = Client('pulsar://localhost:6650')
    consumer = client.subscribe('my-topic',subscription_name='my-sub', schema=schema.JsonSchema())

    while True:
        msg = consumer.receive()
        print("Received message: '%s'" % msg.data())
        consumer.acknowledge(msg)

    client.close()

if __name__ == '__main__':
    main()