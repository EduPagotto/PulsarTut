#!/usr/bin/env python3
'''
Created on 20220710
Update on 20220719
@author: Eduardo Pagotto
 '''

from pulsar import Client
from pulsar import schema as sc

class RpaTeste(sc.Record):
    nome = sc.String()
    idade = sc.Integer()

def main():
    client = Client('pulsar://localhost:6650')
    consumer = client.subscribe('persistent://rpa/ns01/tp01',subscription_name='my-sub', schema=sc.JsonSchema(RpaTeste))

    while True:
        msg = consumer.receive()
        print("Received message: '%s'" % msg.data())
        consumer.acknowledge(msg)

    client.close()

if __name__ == '__main__':
    main()