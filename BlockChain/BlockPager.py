# Designed by Barun
#Date 21/9/2019
###########################################

# Export RCA security library  or pycrpto
import hashlib
import random
import string
import json
import binascii
import numpy as np
import pandas as pd
import pylab as pl
import logging
import datetime
import collections

# following imports are required by PKI
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

#########################################3

#generate public and private key

#######################################################3
#Blockchain is a chain  of block which contain information that which stores inside a block that depends on the type of block.
# Ex Bitcoin ,Let says we have five block b1 ,b2 ,b3 --b5 ,b1 want to send 200/- rs b2 ,b1  has traction detail and feedback.
# All blocks  are containni
#Satoshi Nakamoto created the first virtual currency in the world called Bitcoin
#
#Client  > one who will buy goods from sender ,element of block chain.
#Miners   >Miner who pic the transtions and assemble them into hash connnected block.
#Blockchain >  Datastructure of all connected member ,temper-proof,Distributed p2p networks.
#
#
#
#
#
#######################################################

class client:
    def __init__(self):
        random = Crypto.Random.new().read
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
      return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')
      
      
      
      
      
      
      
      
####################################################################3

barun = client()
print (barun.identity)

########################################################################    
