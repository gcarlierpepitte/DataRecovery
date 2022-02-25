import pyodbc
import requests

server = 'GUNOLCARLIE692B'
username = 'admin'
password=''

try :
    cnxn = pyodbc.connect("Driver={HFSQL};DSN=GUNOLCARLIE692B;UID=admin;PWD=;Server Port=4900")
    print("{c} is working".format(c=connect_string))
    cnxn.close()
except pyodbc.Error as ex:
    print("{c} is not working".format(c=connect_string))


