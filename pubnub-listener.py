#!/usr/bin/env python
import pubnub_keys
import time
import signal
import sys
#import pyttsx
import os

#print('Initialize speech engine')
#engine = pyttsx.init()

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

pnconfig = PNConfiguration()
 
pnconfig.publish_key = pubnub_keys.PUB_KEY
pnconfig.subscribe_key = pubnub_keys.SUB_KEY
 
pubnub = PubNub(pnconfig)
 
my_listener = SubscribeListener()
pubnub.add_listener(my_listener)
 
pubnub.subscribe().channels('lapChannel').execute()
my_listener.wait_for_connect()
print('connected')
 
while(True):
    result = my_listener.wait_for_message_on('lapChannel')
    print(result.message)

    os.system("say '%s'" % result.message)
    #engine.say(result.message)
    #engine.runAndWait()
    time.sleep(0.05)

