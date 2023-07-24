# Использование PyMongo вместо mongo shell

from pymongo import MongoClient
from datetime import datetime

from lib import read_config

cfg = read_config(filename='tinyScripts.ini', section='Mongo')
conn = MongoClient('mongodb://' + cfg['user'] + ':' + cfg['password'] + '@' + cfg['ip'] + ':' + cfg['port'] + '/'
                       + cfg['db'])

db = conn.saturn_v
colls = db.Products

finded_date = datetime(2020,4,23).date()
finded_docs = []

for coll in colls.find({'owner_id': 1504, 'product_alias': {'$regex': 'openbank'}}):
    if coll.get('redirect_meta', None):
        if coll['redirect_meta'].get('history', None):
            for history in coll['redirect_meta']['history']:
                if history['redirect_date'].date() == finded_date:
                    finded_docs.append(coll)
                    print(coll['passport_lastname'], coll['passport_name'], coll['passport_middlename'])

pass