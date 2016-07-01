# -*- coding: utf-8 -*- 
import xml.dom.minidom
import com_appConst
import com_wdat

#com_parseXml
class parseXmlClass:

	def __init__(self):
		print ""

	def exec_parse(self, sXml  ,sCity):
		ret={}
		clsConst  = com_appConst.appConstClass()
		clsWdat = com_wdat.wdatClass()
		clsWdat.delete_dat()
		iCt=0
		try:
			dom = xml.dom.minidom.parseString(sXml)
			for node in dom.getElementsByTagName('channel'):
				for title in node.getElementsByTagName("title"):
					sTitle = title.firstChild.data
					#print "  " + title.tagName + "=" +sTitle
					#print "  ct="+ str(iCt)+", " + title.tagName + "=" +sTitle
					if(iCt==1):
						#print "  1=" + title.tagName + "=" +sTitle
						sRet= clsWdat.get_wString(sTitle)
						print "sRet="+sRet
						clsWdat.saveData(sRet, sCity)
					iCt=iCt+1
					
		except:
			print "failue, exec_parse"
			raise
		finally:
			print "End ,exec_parse"
		return ret

	def test_parse(self, sXml ):
		ret={}
		clsConst  = com_appConst.appConstClass()
		
		try:
			dom = xml.dom.minidom.parseString(sXml)
			for node in dom.getElementsByTagName('item'):
				for url in node.getElementsByTagName("itemName"):
					print "  " + url.tagName + "=" + url.firstChild.data					
				for item_id in node.getElementsByTagName("itemId"):
					print "  " + item_id.tagName + "=" + item_id.firstChild.data
		except:
			print "failue, test_parse"
			raise
		finally:
			print "End ,test_parse"
		return ret
