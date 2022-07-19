#!/usr/bin/env python3
'''
Created on 20220710
Update on 20220711
@author: Eduardo Pagotto
 '''

#import json
from pulsar import Client
from pulsar import schema as sc

class rpaTeste(sc.Record):
    nome = sc.String()
    idade = sc.Integer()

def main():

    # schema : dict = {}
    # with open('./pulsar-dsk/schema2.json', 'r') as file:
    #     schema = json.load(file)

    try:
        client = Client('pulsar://localhost:6650')
        producer = client.create_producer('persistent://rpa/ns01/tp01', schema=sc.JsonSchema(schema))

        t = rpaTeste
        t.nome = "edu"

        for i in range(10):
            t.idade = i
            producer.send(t)
            #producer.send(('hello-pulsar-%d' % i).encode('utf-8'))

    except Exception as exp:
        print(str(exp))
    finally:
        client.close()

if __name__ == '__main__':
    main()
