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

    try:
        client = Client('pulsar://localhost:6650')
        producer = client.create_producer('persistent://rpa/ns01/tp01', schema=sc.JsonSchema(RpaTeste))

        t = RpaTeste()
        t.nome = "edu"

        for i in range(10):
            t.idade = i
            producer.send(t)
           
    except Exception as exp:
        print(str(exp))
    finally:
        client.close()

if __name__ == '__main__':
    main()
