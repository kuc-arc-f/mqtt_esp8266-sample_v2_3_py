# -*- coding: utf-8 -*- 
import MySQLdb
import com_appConst
#define

mStr_HARE =u"晴"
mStr_KUMORI =u"曇"
mStr_AME =u"雨"

mCode_HARE ="1"
mCode_KUMORI ="2"
mCode_AME ="3"

#com_news
class wdatClass:

    def __init__(self):
        print ""
        
    def delete_dat(self ):
    	ret=False
    	clsConst = com_appConst.appConstClass()
    	connection = MySQLdb.connect(host=clsConst.mHost, db=clsConst.mDB_NAME, user=clsConst.mUser, passwd=clsConst.mPass, charset="utf8")
    	cursor = connection.cursor()
    	sSql="delete from T_MATRIX_DAT;"
    	cursor.execute(sSql)
    	connection.commit()
    	connection.close()
    	ret=True
    	return ret
    	
    def get_wString(self, sTitile ):
    	sRet=""
    	if (len(sTitile) < 1):
    		return sRet
    	items =sTitile.split(" ")
    	sTmp=""
    	for item in items:
    		sTmp=item
    		sTmp=sTmp[0]
    		#print "sTmp="+ sTmp
    		if sTmp==mStr_HARE:
    			sRet=mCode_HARE
    			return sRet
    		if sTmp==mStr_KUMORI:
    			sRet=mCode_KUMORI
    			return sRet
    		if sTmp==mStr_AME:
    			sRet=mCode_AME
    			return sRet
    	return sRet
    	
    def saveData(self, sCond , sCity):
    	ret=False
    	clsConst = com_appConst.appConstClass()
    	connection = MySQLdb.connect(host=clsConst.mHost, db=clsConst.mDB_NAME, user=clsConst.mUser, passwd=clsConst.mPass, charset="utf8")
    	cursor = connection.cursor()
    	sSql=u"INSERT INTO T_MATRIX_DAT (COND, CITY"
    	sSql=sSql+",created"
    	sSql=sSql+") values ("
    	sSql=sSql+ " \""+ sCond +"\" "
    	sSql=sSql+ ", \""+ sCity +"\" "
    	sSql=sSql+",now() );"
    	#print sSql
    	cursor.execute(sSql)
    	connection.commit()
    	cursor.close()
    	connection.close()
    	ret=True
    	return ret
    	