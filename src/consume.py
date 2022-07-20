#!/usr/bin/env python3
'''
Created on 20220710
Update on 20220720
@author: Eduardo Pagotto
 '''

from pulsar import Client
from pulsar import exceptions as ex
from pulsar import schema as sc

from RpaTeste import RpaTeste
from GracefulKiller import GracefulKiller

def main():
    print(f'Consumer Inicializado')
    client = Client('pulsar://localhost:6650')
    consumer = client.subscribe('persistent://rpa/ns01/tp01',subscription_name='subscriptionz-01', schema=sc.JsonSchema(RpaTeste))

    killer = GracefulKiller()
    while killer.kill_now is False:

        try:
            msg = consumer.receive(5000)
        except ex.Timeout as exp:
            print(str(exp))
            continue

        tt : RpaTeste = msg.value()
        print(f'Nome: {tt.nome} Idade {tt.idade}')
        consumer.acknowledge(msg)

    client.close()
    print(f'Consumer Finalizado')

if __name__ == '__main__':
    main()