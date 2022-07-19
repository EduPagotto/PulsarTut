#!/usr/bin/env python3
'''
Created on 20220710
Update on 20220719
@author: Eduardo Pagotto
 '''

from pulsar import Client
from pulsar import exceptions as ex
from pulsar import schema as sc

from RpaTeste import RpaTeste

def main():
    client = Client('pulsar://localhost:6650')
    consumer = client.subscribe('persistent://rpa/ns01/tp01',subscription_name='my-sub', schema=sc.JsonSchema(RpaTeste))

    while True:

        try:
            msg = consumer.receive(5000)
        except ex.Timeout as exp:
            print(str(exp))
            continue

        tt : RpaTeste = msg.value()
        print(f'Nome: {tt.nome} Idade {tt.idade}')
        consumer.acknowledge(msg)

    client.close()

if __name__ == '__main__':
    main()