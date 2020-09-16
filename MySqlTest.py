import pymysql

db = pymysql.connect("123.59.211.184","root","Hczztest01!","hczz")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version:%s" % data)
db.close()