# -*- coding: utf-8 -*- 
# コンスト

#com_appConst
class appConstClass:
    def __init__(self):
        print ""
        
    mHost = "localhost"
    mDB_NAME= "mqtt_db"
    mUser ="test_user"
    mPass ="password"
    mOK_CODE=1
    mNG_CODE=0
    #mqtt
    mMQTT_HostName="localhost"
    #mMQTT_HostName="test.mosquitto.org"
    
    mMQTT_Port =1883
    mWaitMsec=1060
    #wCode
    mCodeHARE  ="1"
    mCodeKUMORI="2"
    mCodeAME   ="3"
    
    mHareStr="FF0001"
    mKumoriStr="FF0002"
    mAmeStr="FF0003"

    def test(self, sId):
    	print "test"

