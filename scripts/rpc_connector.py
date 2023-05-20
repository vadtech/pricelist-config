import os
import xmlrpc.client

url = 'https://vad2-stage-7667889.dev.odoo.com'
db = 'vadtech-odoo-main-3533917'
username = 'innocent.mpasi@glace.com'
password = 'Sanna@1#'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
# common.version()
# print(common.version())
uid = common.authenticate(db, username, password, {})
print('uuid', uid)
models_object = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))