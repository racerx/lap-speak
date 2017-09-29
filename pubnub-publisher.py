#!/usr/bin/env python
import time
import signal
import sys

# import pubnub items
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener

# set up graceful exit and disconnect from the subscrbed channel
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        pubnub.unsubscribe().channels('awesomeChannel').execute()
        my_listener.wait_for_disconnect()
        print('unsubscribed')
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

pnconfig = PNConfiguration()
 
pnconfig.publish_key = 'demo'
pnconfig.subscribe_key = 'demo'
 
pubnub = PubNub(pnconfig)
 
my_listener = SubscribeListener()
pubnub.add_listener(my_listener)
 
pubnub.subscribe().channels('awesomeChannel').execute()
my_listener.wait_for_connect()
print('connected')
 
while(True):
	pubnub.publish().channel('awesomeChannel').message({'field1': 'awesome', 'fieldB': 10}).sync()
	time.sleep(10)
	print('I published some data!')

 


