# -*- coding: utf-8 -*- 
import MySQLdb
import com_appConst
#define


#com_wdat
class wdatClass:

    def __init__(self):
        print ""
    
    def get_wData(self, sCity):
    	sRet=""
    	sSql="SELECT COND  from T_MATRIX_DAT "
    	sSql=sSql+" where CITY="+ str(sCity)
    	sSql=sSql+" limit 1"
    	
    	clsConst = com_appConst.appConstClass()
    	connection = MySQLdb.connect(host=clsConst.mHost, db=clsConst.mDB_NAME, user=clsConst.mUser, passwd=clsConst.mPass, charset="utf8")
    	cursor = connection.cursor()
    	cursor.execute( sSql )
    	result = cursor.fetchall()
    	for row in result:
    		sRet          =row[0]
    	
    	cursor.close()
    	connection.close()
    	return sRet
    	
    def get_u8code(self, sCode):
    	sRet=""
    	clsConst = com_appConst.appConstClass()
    	
    	if(sCode==clsConst.mCodeHARE ):
    		sRet=clsConst.mHareStr
    	if(sCode==clsConst.mCodeKUMORI ):
    		sRet=clsConst.mKumoriStr
    	if(sCode==clsConst.mCodeAME ):
    		sRet=clsConst.mAmeStr
    	
    	return sRet
    	