#!/usr/bin/env python3
'''
Created on 20220710
Update on 20220711
@author: Eduardo Pagotto
 '''

import json
from pulsar import Client
from pulsar import schema as sc

def main():

    schema : dict = {}
    with open('./schema1.json', 'r') as file:
        schema = json.load(file)

    client = Client('pulsar://localhost:6650')
    producer = client.create_producer('my-topicZ3', schema=sc.JsonSchema(schema))

    for i in range(10):
        producer.send({'nome':'Eduardo', 'idade':i})
        #producer.send(('hello-pulsar-%d' % i).encode('utf-8'))

    client.close()

if __name__ == '__main__':
    #try:
    main()
    #except Exception as exp:
    #    print(str(exp))


# class Thermal(sc.Record):
#     nome = sc.String()
#     idade = sc.Integer()

# def main():

#     schema : dict = {}
#     with open('./schema1.json', 'r') as file:
#         schema = json.load(file)

#     t = Thermal
#     t.nome = "edu"

#     client = Client('pulsar://localhost:6650')
#     producer = client.create_producer('my-topicZ2', schema=sc.JsonSchema(Thermal))

#     for i in range(10):
#         t.idade = i
#         producer.send(t)
#         #producer.send(('hello-pulsar-%d' % i).encode('utf-8'))
#         #producer.send(('hello-pulsar-%d' % i).encode('utf-8'))

#     client.close()

# if __name__ == '__main__':
#     #try:
#     main()
#     #except Exception as exp:
#     #    print(str(exp))