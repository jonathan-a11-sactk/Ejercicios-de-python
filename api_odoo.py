import xmlrpc.client

url = "http://localhost:8016"
db = "information_page"
user ="admin"
password = "admin"

common = xmlrpc.client.ServerProxy("{}/xmlrpc/2/common".format(url))
uid = common.authenticate(db,user,password,{})
if uid:
    print("authenticate success")
else:
    print("authenticate failed")
