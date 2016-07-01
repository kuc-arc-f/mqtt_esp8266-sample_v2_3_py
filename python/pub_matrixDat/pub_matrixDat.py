# -*- coding: utf-8 -*- 
#------------------------------------
# @calling
# @purpose : MQTT Pub, sample
# @date : 2016-06-29
# @Author : 
#------------------------------------
import paho.mqtt.publish as publish
import datetime
import time
import sys
import traceback
import com_appConst
import com_mqttPub
import com_sendString
import com_wdat

mTopic="item-kuc-arc-f/device-1/matrix_sample_v2"
#mCITY="40"
mCITY="13"

mTimeMax=3
mMaxTitle=10

mTyp_MSG =1
mTyp_TIME =2

if __name__ == "__main__":
	#sMsgSample="サンプルもじ123"
	#clsSend= com_sendString.sendStringClass()
	clsPub=com_mqttPub.mqttPubClass()
	clsWdat=com_wdat.wdatClass()
	from datetime import datetime
	tmBef = datetime.now()
	#iTyp=mTyp_MSG
	
	while True:
		tmNow = datetime.now()
		tmSpan = tmNow - tmBef
		iSpan = tmSpan.total_seconds()
		time.sleep(1.0)
		sTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		
		sTemp=""
		print("time=" +sTime)
		if iSpan > mTimeMax:
			tmBef = datetime.now()
			try:
				sCode =clsWdat.get_wData(mCITY)
				sUtf8 =clsWdat.get_u8code(sCode)
				clsPub.send_pubData(sUtf8, mTopic)
			except:
				print "--------------------------------------------"
				print traceback.format_exc(sys.exc_info()[2])
				print "--------------------------------------------"
	


