#!/usr/bin/env python3
'''
Created on 20220710
Update on 20220713
@author: Eduardo Pagotto
 '''

from pulsar import Client, schema

def main():

    client = Client('pulsar://localhost:6650')
    consumer = client.subscribe('persistent://rpa/ns01/topic-01','test',schema=schema.StringSchema())
    producer = client.create_producer('persistent://rpa/ns01/topic-01',schema=schema.StringSchema())

    for i in range(10):
        print('send msg "hello-%d"' % i)
        producer.send_async('hello-%d' % i, callback=None)
    producer.flush()
    for i in range(10):
        msg = consumer.receive()
        consumer.negative_acknowledge(msg)
        print('receive and nack msg "%s"' % msg.data())
    for i in range(10):
        msg = consumer.receive()
        consumer.acknowledge(msg)
        print('receive and ack msg "%s"' % msg.data())
    try:
        # No more messages expected
        msg = consumer.receive(100)
        print('receive trash msg "%s"' % msg.data())
    except:
        print("no more msg")
        pass

    consumer.close()
    producer.close()


if __name__ == '__main__':
    main()