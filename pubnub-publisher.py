#!/usr/bin/env python
import time
import signal
import sys
import serial


port = serial.Serial("COM6", baudrate=9600, timeout=3.0)

# import pubnub items
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener

# set up graceful exit and disconnect from the subscrbed channel
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        pubnub.unsubscribe().channels('lapChannel').execute()
        my_listener.wait_for_disconnect()
        print('unsubscribed')
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

pnconfig = PNConfiguration()
 
pnconfig.publish_key = 'YOUR-KEY'
pnconfig.subscribe_key = 'YOUR-KEY'
 
pubnub = PubNub(pnconfig)
 
my_listener = SubscribeListener()
pubnub.add_listener(my_listener)
 
pubnub.subscribe().channels('lapChannel').execute()
my_listener.wait_for_connect()
print('connected')
 
while(True):
    rcv = port.readline()
    print("read from serial:" + rcv)
    if rcv:
        pubnub.publish().channel('lapChannel').message({'field1': rcv}).sync()
        print("Published to pubnub channel:" + rcv)




