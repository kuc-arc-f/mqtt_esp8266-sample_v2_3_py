//------------------------------------
// MQTT-SUB, send TO esp8266 
// @Author  : Kouji Nakashima / kuc-arc-f.com
// @date    : 2016-06-30
//------------------------------------

[summary]

# pyrhon
get_matrixDat: get weather Data, to MYSQL(DB)
pub_matrixDat: MQTT PUB

*) create table, reqquire.
CREATE TABLE IF NOT EXISTS T_MATRIX_DAT (
  id int(11) NOT NULL AUTO_INCREMENT,
  CITY   text DEFAULT NULL,
  COND text DEFAULT NULL,
  COND_TXT int(11) DEFAULT NULL,
  created datetime DEFAULT NULL,
  modified datetime DEFAULT NULL,
  PRIMARY KEY ( id )
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=248 ;

[reference Project]
https://github.com/kuc-arc-f/mqtt_esp8266-sample_v2_3



