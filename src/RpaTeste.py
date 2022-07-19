#!/usr/bin/env python3
'''
Created on 20220710
Update on 20220719
@author: Eduardo Pagotto
 '''

from pulsar import schema as sc

class RpaTeste(sc.Record):
    nome = sc.String()
    idade = sc.Integer()