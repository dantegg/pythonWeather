#写入mongo

from pymongo import MongoClient
import random

#conn = pymongo.Connection('127.0.0.1',27017)
conn = MongoClient('127.0.0.1',27017)

db = conn.test

db.pyuser.drop()
db.pyuser.save({"id":1,"name":"kaka","sex":"male"})

for id in range(2,10):
    name = random.choice(["steve","koby","owen","tody","rony"])
    sex = random.choice(["male","female"])
    db.pyuser.insert({
        "id":id,
        "name":name,
        "sex":sex
    })
# content = db.pyuser.find()
#
# for i in content:
#     print i

# usercontent = db.users.find()
#
# for z in usercontent:
#     print z
