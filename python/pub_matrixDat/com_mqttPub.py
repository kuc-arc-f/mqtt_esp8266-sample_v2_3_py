# -*- coding: utf-8 -*- 
# Ｐｕｂ

import paho.mqtt.publish as publish
import com_appConst
#import com_weather
import time
import com_sendString

mMaxOne =10

#com_mqttPub
class mqttPubClass:

    def __init__(self):
        print ""
        
    def send_pubw(self, sPay ,sTopic):
		clsConst  = com_appConst.appConstClass()
		iWait=0
#		iAdd=7
		iAdd=10
		if (len(sPay) < 1):
			return
#		if( len(sPay) > 20 ):
#			sPay=sPay[0:20]
		if( len(sPay) > mMaxOne ):
			sPay=sPay[0:mMaxOne]
		if( len(sPay) > 10 ):
			iAdd=(len(sPay) * 1000) * 0.5
			iAdd=iAdd / 1000
		print("sLen=")
		print(len(sPay))
		#print("sPay=" +sPay)
		publish.single(topic=sTopic, payload=sPay, hostname=clsConst.mMQTT_HostName , port=clsConst.mMQTT_Port )
		print("iWait=")
		iWait = (len(sPay) * clsConst.mWaitMsec) / 1000
		iWait = iWait+iAdd
		print(str(iWait) )
		time.sleep(iWait)
		return
    #
    def send_pubData(self, sPay ,sTopic):
		iWait=0
		clsConst  = com_appConst.appConstClass()
		publish.single(topic=sTopic, payload=sPay, hostname=clsConst.mMQTT_HostName , port=clsConst.mMQTT_Port )
		#time.sleep(iWait)
		return
		
